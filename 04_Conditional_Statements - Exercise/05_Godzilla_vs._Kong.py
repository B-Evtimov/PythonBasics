film_money = float(input())
statists_count = int(input())
suit_price = float(input())

decor_price = film_money * 0.10
clothing_price = statists_count * suit_price

if statists_count > 150:
    clothing_price *= 0.90

total_cost = decor_price + clothing_price

if total_cost > film_money:
    needed = total_cost - film_money
    print("Not enough money!")
    print(f"Wingard needs {needed:.2f} leva more.")
else:
    left = film_money - total_cost
    print("Action!")
    print(f"Wingard starts filming with {left:.2f} leva left.")