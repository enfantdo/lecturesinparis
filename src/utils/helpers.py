def clean_event_data(event):
    # Function to clean and format event data
    cleaned_event = {
        'title': event.get('title', '').strip(),
        'date': event.get('date', '').strip(),
        'location': event.get('location', '').strip(),
        'description': event.get('description', '').strip()
    }
    return cleaned_event

def format_event_list(events):
    # Function to format a list of events
    return [clean_event_data(event) for event in events]