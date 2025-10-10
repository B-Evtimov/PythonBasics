needed_money = float(input())
available_money = float(input())

days_counter = 0
spend_streak = 0

while available_money < needed_money and spend_streak < 5:
    action = input()
    amount = float(input())
    days_counter += 1

    if action == "spend":
        available_money -= amount
        if available_money < 0:
            available_money = 0
        spend_streak += 1
    elif action == "save":
        available_money += amount
        spend_streak = 0

if spend_streak == 5:
    print("You can't save the money.")
    print(days_counter)
else:
    print(f"You saved the money for {days_counter} days.")
