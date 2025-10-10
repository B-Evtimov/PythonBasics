total = 0

while True:
    transaction = input()
    if transaction == "NoMoreMoney":
        break

    amount = float(transaction)

    if amount < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {amount:.2f}")
    total += amount

print(f"Total: {total:.2f}")
