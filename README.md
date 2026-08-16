# NASA APOD Viewer

A simple Flask web app that fetches NASA's Astronomy Picture of the Day (APOD) and displays it in the browser. Built as part of the [Stardance Challenge](https://stardance.hackclub.com/) (NASA x Hack Club).

## Features

- Fetches live data from NASA's public APOD API
- Pick any date (from June 16, 1995 onward) to view that day's picture
- Random date button — jump to a random day in APOD history
- Clean, dark, mobile-responsive UI
- Graceful error handling for invalid dates or API issues

## Tech stack

- Python
- Flask
- NASA APOD API
- HTML/CSS/vanilla JS (no frontend framework)

## Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Newb-OP/nasa-apod-viewer.git
   cd nasa-apod-viewer
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install flask requests python-dotenv
   ```

3. Get a free NASA API key at [api.nasa.gov](https://api.nasa.gov) and create a `.env` file in the project root:
   ```
   NASA_API_KEY=your_key_here
   ```

4. Run the app:
   ```bash
   python app.py
   ```

5. Open `http://127.0.0.1:5000` in your browser.

## Notes

`apod.py` is the original terminal-only version of this project, kept for reference. `app.py` is the full Flask web app.
