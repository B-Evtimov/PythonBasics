
groups_count = int(input())


musala = 0
monblan = 0
kilimanjaro = 0
k2 = 0
everest = 0

total_climbers = 0

for _ in range(groups_count):
    climbers = int(input())
    total_climbers += climbers

    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        monblan += climbers
    elif climbers <= 25:
        kilimanjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    else:
        everest += climbers


print(f"{musala / total_climbers * 100:.2f}%")
print(f"{monblan / total_climbers * 100:.2f}%")
print(f"{kilimanjaro / total_climbers * 100:.2f}%")
print(f"{k2 / total_climbers * 100:.2f}%")
print(f"{everest / total_climbers * 100:.2f}%")
