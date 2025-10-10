product = input()
day = input()
count = float(input())

is_valid_day = day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
is_valid_product = product in ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]

if not is_valid_day or not is_valid_product:
    print("error")
else:
    if day == "Saturday" or day == "Sunday":
        if product == "banana":
            print("{:.2f}".format(count * 2.70))
        elif product == "apple":
            print("{:.2f}".format(count * 1.25))
        elif product == "orange":
            print("{:.2f}".format(count * 0.90))
        elif product == "grapefruit":
            print("{:.2f}".format(count * 1.60))
        elif product == "kiwi":
            print("{:.2f}".format(count * 3.00))
        elif product == "pineapple":
            print("{:.2f}".format(count * 5.60))
        elif product == "grapes":
            print("{:.2f}".format(count * 4.20))
    else:
        if product == "banana":
            print("{:.2f}".format(count * 2.50))
        elif product == "apple":
            print("{:.2f}".format(count * 1.20))
        elif product == "orange":
            print("{:.2f}".format(count * 0.85))
        elif product == "grapefruit":
            print("{:.2f}".format(count * 1.45))
        elif product == "kiwi":
            print("{:.2f}".format(count * 2.70))
        elif product == "pineapple":
            print("{:.2f}".format(count * 5.50))
        elif product == "grapes":
            print("{:.2f}".format(count * 3.85))