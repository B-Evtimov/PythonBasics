month = input()
time = int(input())

studio_price_per_night = 0
apartment_price_per_night = 0
studio_discount = 0
apartment_discount = 0

if month in ["May", "October"]:
    studio_price_per_night = 50
    apartment_price_per_night = 65
    if time > 14:
        studio_discount = 0.30
        apartment_discount = 0.10
    elif time > 7:
        studio_discount = 0.05

elif month in ["June", "September"]:
    studio_price_per_night = 75.20
    apartment_price_per_night = 68.70
    if time > 14:
        studio_discount = 0.20
        apartment_discount = 0.10

elif month in ["July", "August"]:
    studio_price_per_night = 76
    apartment_price_per_night = 77
    if time > 14:
        apartment_discount = 0.10

# Изчисляване на крайните цени
studio_total = studio_price_per_night * time
apartment_total = apartment_price_per_night * time

studio_total -= studio_total * studio_discount
apartment_total -= apartment_total * apartment_discount

# Извеждане на резултата
print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")