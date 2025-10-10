import math

record = float(input())
metres = float(input())
seconds = float(input())

total_seconds = metres * seconds
delay_count = math.floor(metres / 15)
delay_time = delay_count * 12.5
total_time = total_seconds + delay_time

if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record
    print(f"No, he failed! He was {diff:.2f} seconds slower.")