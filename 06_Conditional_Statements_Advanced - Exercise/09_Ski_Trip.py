days = int(input())
room_type = input()
grade = input()

nights = days - 1
price_per_night = 0

# Определяне на базова цена на нощувка
if room_type == "room for one person":
    price_per_night = 18.00
elif room_type == "apartment":
    price_per_night = 25.00
elif room_type == "president apartment":
    price_per_night = 35.00

# Изчисляване на общата цена преди оценката
total_price = nights * price_per_night

# Прилагане на отстъпки според типа стая и престоя
if room_type == "apartment":
    if days < 10:
        total_price *= 0.70
    elif 10 <= days <= 15:
        total_price *= 0.65
    else:
        total_price *= 0.50
elif room_type == "president apartment":
    if days < 10:
        total_price *= 0.90
    elif 10 <= days <= 15:
        total_price *= 0.85
    else:
        total_price *= 0.80

# Прилагане на оценката
if grade == "positive":
    total_price *= 1.25
elif grade == "negative":
    total_price *= 0.90

# Отпечатване на крайната сума
print(f"{total_price:.2f}")