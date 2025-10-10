cake_tall = int(input()) * int(input())  # Обща площ на тортата в парчета
total_taken = 0

while True:
    command = input()
    if command == "STOP":
        print(f"{cake_tall - total_taken} pieces are left.")
        break

    parts = int(command)
    total_taken += parts

    if total_taken > cake_tall:
        print(f"No more cake left! You need {total_taken - cake_tall} pieces more.")
        break

