budget = int(input())
season = input()
fishermen = int(input())

# Определяне на базова цена според сезона
if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600

# Отстъпка според броя рибари
if fishermen <= 6:
    rent *= 0.90
elif 7 <= fishermen <= 11:
    rent *= 0.85
else:
    rent *= 0.75

# Допълнителна отстъпка ако са четен брой и не е есен
if fishermen % 2 == 0 and season != "Autumn":
    rent *= 0.95

# Сравнение с бюджета
diff = abs(budget - rent)

if budget >= rent:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")