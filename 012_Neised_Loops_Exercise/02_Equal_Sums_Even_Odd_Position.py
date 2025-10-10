start = int(input())
end = int(input())

for number in range(start, end + 1):
    even_sum = 0
    odd_sum = 0
    number_str = str(number)

    for index, digit in enumerate(number_str):
        digit = int(digit)
        if index % 2 == 0:  # нечетна позиция (индекси 0, 2, 4)
            odd_sum += digit
        else:               # четна позиция (индекси 1, 3, 5)
            even_sum += digit

    if even_sum == odd_sum:
        print(number, end=" ")