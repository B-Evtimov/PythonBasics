screen = input()
rows = int(input())
columns = int(input())

if screen == "Premiere":
    price = rows * columns * 12.00
    print(f"{price:.2f} leva")

elif screen == "Normal":
    price = rows * columns * 7.50
    print(f"{price:.2f} leva")

elif screen == "Discount":
    price = rows * columns * 5.00
    print(f"{price:.2f} leva")