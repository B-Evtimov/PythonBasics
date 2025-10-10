holiday_price = float(input())
puzzles = int(input())
speaking_dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

# Prices
total = puzzles * 2.60 + speaking_dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
toys_count = puzzles + speaking_dolls + bears + minions + trucks

# Apply discount if applicable
if toys_count >= 50:
    total *= 0.75  # 25% discount

# Deduct rent
total *= 0.90  # 10% rent

# Compare with holiday price
difference = total - holiday_price

if difference >= 0:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {abs(difference):.2f} lv needed.")