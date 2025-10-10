
age = int(input())
washing_machine_price = float(input())
toy_price = int(input())


saved_money = 0
number_of_toys = 0
money_gift = 10
money_taken_by_brother = 0


for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        saved_money += money_gift
        money_taken_by_brother += 1
        money_gift += 10
    else:
        number_of_toys += 1


saved_money += number_of_toys * toy_price


saved_money -= money_taken_by_brother * 1


diff = abs(saved_money - washing_machine_price)

if saved_money >= washing_machine_price:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
