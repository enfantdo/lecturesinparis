# Web Scraper Project

This project is a web scraper built using AutoScraper to extract event data from various websites. The scraper is designed to be flexible and easy to use, allowing users to quickly gather information about events from multiple sources.

## Project Structure

```
web-scraper-project
├── src
│   ├── scraper.py          # Main logic for the web scraper
│   ├── utils
│   │   └── helpers.py      # Utility functions for data handling
│   └── data
│       └── events.json     # JSON file to store scraped event data
├── requirements.txt        # List of dependencies
├── .gitignore              # Files and directories to ignore by Git
└── README.md               # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd web-scraper-project
   ```

2. **Install dependencies:**
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the web scraper, execute the following command:
```
python src/scraper.py
```

The scraped event data will be saved in the `src/data/events.json` file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.