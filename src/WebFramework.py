from flask import Flask, render_template, jsonify
from collections import defaultdict
from datetime import datetime
import json


app = Flask(__name__)

@app.route('/')
def index():
    with open('refined_events.json') as f:
        events = json.load(f)

    # Group events by date
    grouped_events = defaultdict(list)
    for event in events:
        if event['date']:  # Only include events with non-empty dates
            grouped_events[event['date']].append(event)

    # Filter and sort events to include only today or future dates
    try:
        today = datetime.today()
        filtered_events = {
            date: evts for date, evts in grouped_events.items()
            if datetime.strptime(date, "%d-%m-%Y") >= today
        }
        sorted_events = sorted(
            filtered_events.items(),
            key=lambda x: datetime.strptime(x[0], "%d-%m-%Y")
        )
    except ValueError as e:
        print(f"Error parsing date: {e}")
        sorted_events = []  # Fallback to an empty list if parsing fails

    return render_template('index.html', grouped_events=sorted_events)

# Custom date filter
@app.template_filter('date')
def format_date(value, format="%A %d"):
    """Format a date string to the specified format."""
    try:
        date_obj = datetime.strptime(value, "%d-%m-%Y")  # Assuming input is in YYYY-MM-DD
        return date_obj.strftime(format)
    except ValueError:
        return value  # Return the original value if parsing fails


if __name__ == '__main__':
    app.run(debug=True)