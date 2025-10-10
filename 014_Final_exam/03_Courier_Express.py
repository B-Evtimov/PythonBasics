weight = float(input())
shipment_type = input()
kilometres = int(input())

price_per_km = 0.0
express_markup = 0.0


if weight < 1:
    price_per_km = 0.03
    express_markup = 0.80
elif weight < 10:
    price_per_km = 0.05
    express_markup = 0.40
elif weight < 40:
    price_per_km = 0.10
    express_markup = 0.05
elif weight < 90:
    price_per_km = 0.15
    express_markup = 0.02
elif weight <= 150:
    price_per_km = 0.20
    express_markup = 0.01


base_price = price_per_km * kilometres

if shipment_type == "express":
    surcharge = express_markup * price_per_km * weight * kilometres
    total_price = base_price + surcharge
else:
    total_price = base_price

print(f"The delivery of your shipment with weight of {weight:.3f} kg. would cost {total_price:.2f} lv.")
