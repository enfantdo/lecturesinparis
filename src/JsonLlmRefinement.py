import json
import subprocess
import re

# Load the JSON file
with open('src/events.json', 'r') as f:
    events = json.load(f)


def clean_time_output(llm_output):
    """
    Extract and clean the time from the LLM output.
    Only keep the time in HH:mm format.
    """
    # Define a regex pattern to match time in HH:mm format
    time_pattern = r"\b([01]?\d|2[0-3]):[0-5]\d\b"  # Matches 24-hour time format (e.g., 15:00, 03:45)
    
    # Search for the time in the LLM output
    match = re.search(time_pattern, llm_output)
    
    if match:
        return match.group(0)  # Return the matched time (e.g., "15:00")
    else:
        return ""  # Return an empty string if no valid time is found
    
def clean_date_output(llm_output):
    """
    Extract and clean the date from the LLM output.
    Only keep the date in DD-MM-YYYY format.
    """
    # Define a regex pattern to match dates in DD-MM-YYYY format
    date_pattern = r"\b(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}\b"  # Matches DD-MM-YYYY format
    
    # Search for the date in the LLM output
    match = re.search(date_pattern, llm_output)
    
    if match:
        return match.group(0)  # Return the matched date (e.g., "10-07-2025")
    else:
        return ""  # Return an empty string if no valid date is found

# Function to standardize the date format using Ollama
def standardize_date(date):
    prompt = f"""
    Standardize the following date to the format DD-MM-YYYY. 
    If the date is a range, return only the first date. 
    Return only the formatted date.

    Input: '{date}'
    Output: 
    """
    try:
        # Use subprocess to call the Ollama CLI with the 'run' command
        result = subprocess.run(
            ["ollama", "run", "gemma3"],  # Replace 'llama3' with your model name
            input=prompt,
            text=True,
            capture_output=True
        )
        # Debugging: Print the raw output
        print(f"Prompt: {prompt}")
        print(f"Raw Output: {result.stdout.strip()}")
        print(f"Cleaned Raw Output: {clean_date_output(result.stdout)}")
        return clean_date_output(result.stdout.strip())  # Clean the LLM output
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return "Error"


def standardize_time(time):
    prompt = f"""
    Extract the time from the following string. 
    If the string contains both a date and a time, return only the time. 
    Format the time in 24-hour format (HH:mm). 
    Return only the formatted time, with no extra text.
    Input: '{time}'
    Output: 
    """
    try:
        # Use subprocess to call the Ollama CLI with the 'run' command
        result = subprocess.run(
            ["ollama", "run", "mistral"],  # Replace 'llama3' with your model name
            input=prompt,
            text=True,
            capture_output=True
        )
        # Debugging: Print the raw output
        print(f"Prompt: {prompt}")
        print(f"Raw Output: {result.stdout}")
        print(f"Cleaned Raw Output: {clean_time_output(result.stdout)}")
        return clean_time_output(result.stdout.strip()) 
    except Exception as e:
        print(f"Error calling Ollama: {e}")
        return "Error"

# Refine the JSON
for event in events:
    event['date'] = standardize_date(event['date'])
    if event['time']:  # Only refine time if it's not empty
        event['time'] = standardize_time(event['time'])

# Sort events by date and time
events.sort(key=lambda x: (
    x['date'],  # Sort by date first
    x['time'] if x['time'] else "99:99"  # Sort by time, empty times go to the end
))

# Save the refined JSON
with open('refined_events.json', 'w') as f:
    json.dump(events, f, indent=4)

print("Dates and times have been standardized and events sorted.")