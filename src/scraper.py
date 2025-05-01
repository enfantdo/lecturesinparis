import json
from requests_html import HTMLSession

session = HTMLSession()

# List of websites and their respective selectors
websites = [
    {
        # Institut du Monde Arabe
        "url": "https://www.imarabe.org/fr/agenda/rencontres-et-debats",
        "selectors": {
            "titles": ".text-wrapper h3 a",
            "descriptions": "",  # Leave empty if not available
            "dates": ".dates",
            "time": "", # Leave empty if not available
            "locations": "",  # Static location or leave empty if not available
            "links": ".text-wrapper h3 a"
        },
        "static_location": "Institut du Monde Arabe"  # Optional static location
    },
    {
        # IRCAM
        "url": "https://www.ircam.fr/agenda/tag/rencontres",
        "selectors": {
            "titles": ".event-line-box__title",
            "descriptions": ".event-line-box__desc",
            "dates": ".page__meta-date",
            "time": "", # Leave empty if not available
            "locations": ".page__meta-title",
            "links": ".button.mt1.event__meta__btn"
        },
        "static_location": ""  # Leave empty if location is dynamic
    },
    {
    # Guimet
    "url": "https://www.guimet.fr/fr/agenda?date_start=&date_end=&field_taxo_event_type_expo_target_id%5B178%5D=178&field_taxo_event_type_expo_target_id%5B180%5D=180&date_datepicker=",
    "selectors": {
        "titles": ".left h3",
        "descriptions": ".field--name-field-teaser p",
        "dates": ".field--name-field-dates-text p",
        "time": ".field--name-field-dates-text p",
        "locations": "",
        "links": ".read-more-link"
    },
    "static_location": "Guimet"
    },
    {
    # Centre Wallonie-Bruxelles
    "url": "https://cwb.fr/agenda?dispositifs-cycles=rencontre,conference",
    "selectors": {
        "titles": ".eventblock__title",
        "descriptions": "",
        "dates": ".eventblock__date",
        "time": ".eventblock__hour",
        "locations": "",
        "links": ".eventblock__title"
    },
    "static_location": "Centre Wallonie-Bruxelles"
},
{
    # Cité de l'architecture et du patrimoine
    "url": "https://www.citedelarchitecture.fr/fr/agenda/type_evenement/colloque-conference-debat-15?date=tout",
    "selectors": {
        "titles": ".right h3",  # Targets the event title
        "descriptions": ".right p.field--name-field-chapo",  # Targets the description
        "dates": ".agenda-date div",  # Targets the date and time
        "time": ".agenda-date div",  # Same as dates since time is included
        "locations": "",  # Leave empty as the location is static
        "links": ".right h3 a"  # Targets the link to the event
    },
    "static_location": "Cité de l'architecture et du patrimoine"  # Static location
},
{
    # Musée de l'Homme
    "url": "https://www.museedelhomme.fr/fr/agenda?f%5B0%5D=activites%3A20&f%5B1%5D=activites%3A30&f%5B2%5D=activites%3A34",
    "selectors": {
        "titles": ".card__heading a",  # Targets the event title
        "descriptions": ".card__content p",  # Targets the event description
        "dates": ".card__date .field--name-field-dates-text",  # Targets the date
        "time": "",  # Leave empty if not available
        "locations": "",  # Leave empty as the location is static
        "links": ".card__heading a"  # Targets the link to the event
    },
    "static_location": "Musée de l'Homme"  # Static location
},
{
    # BnF (Bibliothèque nationale de France)
    "url": "https://www.bnf.fr/fr/agenda?quand=&quoi%5B%5D=2585&Appliquer=Appliquer",
    "selectors": {
        "titles": ".views-field-title a",  # Targets the event title
        "descriptions": "",  # Leave empty if no description is available
        "dates": ".views-field-field-daterange1 .field-content",  # Targets the date and time
        "time": ".views-field-field-daterange1 .field-content",  # Same as dates since time is included
        "locations": ".views-field-field-entref1 .field-content",  # Targets the location
        "links": ".views-field-title a"  # Targets the link to the event
    },
    "static_location": "François-Mitterrand"  # Static location
}  
]

# List to store all events
all_events = []

# Loop through each website
for site in websites:
    url = site["url"]
    selectors = site["selectors"]
    static_location = site.get("static_location", "")

    # Fetch the page
    response = session.get(url)

    # Extract data using the selectors
    titles = response.html.find(selectors["titles"])
    descriptions = response.html.find(selectors["descriptions"]) if selectors["descriptions"] else []
    dates = response.html.find(selectors["dates"])
    time = locations = response.html.find(selectors["time"]) if selectors["time"] else []
    locations = response.html.find(selectors["locations"]) if selectors["locations"] else []
    links = response.html.find(selectors["links"])

    # Loop through the titles and construct event data
    for i in range(len(titles)):
        all_events.append({
            "title": titles[i].text,
            "description": descriptions[i].text if i < len(descriptions) else "",
            "date": dates[i].text if i < len(dates) else "",
            "time": time[i].text if i < len(time) else "",
            "location": locations[i].text if i < len(locations) else static_location,
            "link": links[i].attrs['href'] if i < len(links) else ""
        })

# Save all events to a JSON file
with open('events.json', 'w') as f:
    json.dump(all_events, f, indent=4)