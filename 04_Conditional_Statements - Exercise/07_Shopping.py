Peter_money = float(input())
videocards = int(input())
processors = int(input())
ram = int(input())

videocards_price = videocards * 250
processors_price = (videocards_price * 0.35) * processors
ram_price = (videocards_price * 0.10) * ram

total_price = videocards_price + processors_price + ram_price
if videocards > processors:
    discount = total_price * 0.15
    total_price = total_price - discount
    if total_price <= Peter_money:
        print(f"You have {Peter_money - total_price:.2f} leva left!")
    elif total_price >= Peter_money:
        print(f"Not enough money! You need {total_price - Peter_money:.2f} leva more!")

else:
    if total_price <= Peter_money:
        print(f"You have {Peter_money - total_price:.2f} leva left!")
    elif total_price >= Peter_money:
        print(f"Not enough money! You need {total_price - Peter_money:.2f} leva more!")