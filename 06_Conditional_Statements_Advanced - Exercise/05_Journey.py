money = float(input())
season = input()
if season == "summer":
    if money <= 100:
        money = money * 0.30
        print("Somewhere in Bulgaria")
        print(f"Camp - {money:.2f}")

    elif money <= 1000:
        money = money * 0.40
        print("Somewhere in Balkans")
        print(f"Camp - {money:.2f}")

    elif money > 1000:
        money = money * 0.90
        print("Somewhere in Europe")
        print(f"Hotel - {money:.2f}")


elif season == "winter":
    if money <= 100:
        money = money * 0.70
        print("Somewhere in Bulgaria")
        print(f"Hotel - {money:.2f}")

    elif money <= 1000:
        money = money * 0.80
        print("Somewhere in Balkans")
        print(f"Hotel - {money:.2f}")

    elif money > 1000:
        money = money * 0.90
        print("Somewhere in Europe")
        print(f"Hotel - {money:.2f}")