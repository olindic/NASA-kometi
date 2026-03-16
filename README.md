# 🌍 Near-Earth Asteroid Tracker

A simple web app built with Python and Flask that uses the NASA NeoWs API to search for near-Earth asteroids by date range and displays whether they are potentially hazardous.

---

## Features

- Search for asteroids between any two dates
- Displays asteroid name, closest approach date, and hazard status
- Clean table view powered by Flask and Jinja2 templates

---

## Requirements

- Python 3.x
- Flask
- Requests

Install dependencies:
```bash
pip install flask requests
```

---

## Setup

1. Get a free API key at [https://api.nasa.gov](https://api.nasa.gov)
2. Paste it into `nasa.py` where indicated in the comments
3. Run `python nasa.py`
4. Open your browser and go to `http://localhost:8080/asteroids`

---

## Usage

1. Enter a start date and end date (max 7 day range — NASA API limit)
2. Click **Search**
3. The table will show all near-Earth asteroids in that period, including whether they are potentially hazardous