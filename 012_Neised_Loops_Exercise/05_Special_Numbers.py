n = int(input())

for number in range(1111, 10000):
    is_special = True
    for digit_char in str(number):
        digit = int(digit_char)
        if digit == 0 or n % digit != 0:
            is_special = False
            break
    if is_special:
        print(number, end=" ")
