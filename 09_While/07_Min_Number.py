import sys
min_num = sys.maxsize
min_number = None

while True:
    command = input()
    if command == "Stop":
        break

    number = int(command)

    if min_number is None or number > min_number:
        max_number = number

print(min_number)