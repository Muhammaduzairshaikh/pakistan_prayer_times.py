# Pakistan Prayer Times (Terminal)

A simple Python program that fetches **today's prayer times** for cities in Pakistan from the
[AlAdhan Prayer Times API](https://aladhan.com/prayer-times-api) and shows **how much time is left until the next prayer**.

## Features

- Choose from 46 Pakistani cities (or type any other city name)
- Live data fetched from the AlAdhan API using the `requests` library
- Shows Fajr, Sunrise, Dhuhr, Asr, Maghrib and Isha
- Marks the next prayer and shows the time remaining
- After Isha, counts down to tomorrow's Fajr
- Uses Pakistan time (UTC+5), Karachi calculation method and Hanafi Asr

## API used

`GET https://api.aladhan.com/v1/timingsByCity/{DD-MM-YYYY}?city=Lahore&country=Pakistan&method=1&school=1`

No API key is required.

## Installation

1. Install [Python 3.9+](https://www.python.org/downloads/).
2. Clone this repository:
   ```
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```
3. (Optional) Create a virtual environment:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install the dependency:
   ```
   python -m pip install requests
   ```

## Run

```
python pakistan_prayer_times.py
```

Enter a city number from the list (for example `2` for Lahore) or type a city name.

## Sample output

> Replace this with the real output from your own run.

```
Lahore - Wednesday, 11 November 2026  (abhi: 04:15 PM)

    Fajr     05:20 AM
    Sunrise  06:42 AM
    Dhuhr    11:55 AM
 -> Asr      03:45 PM
    Maghrib  05:08 PM
    Isha     06:28 PM

Agli namaz: Asr (03:45 PM)
Baqi time : 0 ghante 30 minute
```

## Project structure

```
.
├── pakistan_prayer_times.py   # main program
├── .gitignore
└── README.md
```

## Notes

Prayer times may differ slightly from your local mosque, as mosques often adjust the calculated times.

## Author

<Your Name>
