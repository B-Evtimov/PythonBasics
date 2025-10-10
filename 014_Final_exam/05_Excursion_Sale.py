sea_packages = int(input())
mountain_packages = int(input())

profit = 0

while True:
    command = input()
    if command == "Stop":
        break

    if command == "sea":
        if sea_packages > 0:
            profit += 680
            sea_packages -= 1
    elif command == "mountain":
        if mountain_packages > 0:
            profit += 499
            mountain_packages -= 1

    if sea_packages == 0 and mountain_packages == 0:
        print("Good job! Everything is sold.")
        break

print(f"Profit: {profit} leva.")
