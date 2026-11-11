"""Pakistan ke cities ke aaj ke namaz ke times + agli namaz mein kitna time baqi.
API: https://aladhan.com/prayer-times-api
Install:  pip install requests
Run:      python pakistan_prayer_times.py
"""
import requests
from datetime import datetime, timedelta, timezone

PK_TZ = timezone(timedelta(hours=5))  # Pakistan Standard Time (UTC+5)
PRAYERS = ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]
SHOWN = ["Fajr", "Sunrise", "Dhuhr", "Asr", "Maghrib", "Isha"]

CITIES = [
    "Karachi", "Lahore", "Islamabad", "Rawalpindi", "Faisalabad", "Multan",
    "Peshawar", "Quetta", "Hyderabad", "Gujranwala", "Sialkot", "Bahawalpur",
    "Sargodha", "Sukkur", "Larkana", "Mardan", "Abbottabad", "Gilgit",
    "Skardu", "Muzaffarabad", "Mirpur", "Jhelum", "Gujrat", "Sahiwal",
    "Rahim Yar Khan", "Dera Ghazi Khan", "Mingora", "Kohat", "Nawabshah",
    "Turbat", "Gwadar", "Chiniot", "Okara", "Kasur", "Sheikhupura",
    "Mianwali", "Dera Ismail Khan", "Bannu", "Sadiqabad", "Jacobabad",
    "Khuzdar", "Murree", "Hunza", "Attock", "Chakwal", "Mansehra",
]


def choose_city():
    print("\nPakistan ke cities:\n")
    for i, c in enumerate(CITIES, 1):
        print(f"{i:>2}. {c:<18}", end="\n" if i % 3 == 0 else "")
    print("\n")
    choice = input("City ka number ya naam likhen: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(CITIES):
        return CITIES[int(choice) - 1]
    return choice.title()  # koi aur city bhi likh sakte hain


def get_timings(city, day):
    url = f"https://api.aladhan.com/v1/timingsByCity/{day:%d-%m-%Y}"
    params = {"city": city, "country": "Pakistan",
              "method": 1,   # University of Islamic Sciences, Karachi
              "school": 1}   # 1 = Hanafi (Asr ka time), 0 = Shafi
    try:
        r = requests.get(url, params=params, timeout=15)
        r.raise_for_status()
    except requests.RequestException as e:
        raise SystemExit(f"API se data nahi aaya ({city}): {e}")
    return r.json()["data"]["timings"]


def to_dt(day, hhmm):
    h, m = map(int, hhmm[:5].split(":"))
    return datetime(day.year, day.month, day.day, h, m, tzinfo=PK_TZ)


city = choose_city()
now = datetime.now(PK_TZ)
today = now.date()
timings = get_timings(city, today)

# Terminal par show karo
print(f"\n{city} - {now:%A, %d %B %Y}  (abhi: {now:%I:%M %p})\n")
times = {p: to_dt(today, timings[p]) for p in SHOWN}

next_prayer = None
for p in PRAYERS:
    if times[p] > now:
        next_prayer = (p, times[p])
        break
if next_prayer is None:  # Isha ke baad -> kal ki Fajr
    tomorrow = today + timedelta(days=1)
    t = get_timings(city, tomorrow)
    next_prayer = ("Fajr", to_dt(tomorrow, t["Fajr"]))

for p in SHOWN:
    arrow = "->" if p == next_prayer[0] and times[p] == next_prayer[1] else "  "
    print(f" {arrow} {p:<8} {times[p]:%I:%M %p}")

left = int((next_prayer[1] - now).total_seconds())
hours, rem = divmod(left, 3600)
print(f"\nAgli namaz: {next_prayer[0]} ({next_prayer[1]:%I:%M %p})")
print(f"Baqi time : {hours} ghante {rem // 60} minute\n")
