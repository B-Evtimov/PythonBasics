import math

days = int(input())
first_day_km = float(input())

total_km = first_day_km
daily_km = first_day_km

for _ in range(days):
    percent_increase = int(input())
    daily_km += daily_km * (percent_increase / 100)
    total_km += daily_km

if total_km >= 1000:
    extra_km = math.ceil(total_km - 1000)
    print(f"You've done a great job running {extra_km} more kilometers!")
else:
    missing_km = math.ceil(1000 - total_km)
    print(f"Sorry Mrs. Ivanova, you need to run {missing_km} more kilometers")
