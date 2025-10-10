total_floors = int(input())
total_rooms = int(input())

for floor in range(total_floors, 0, -1):
    for room in range(total_rooms):
        if floor == total_floors:
            print(f"L{floor}{room}", end= ' ')

        elif floor % 2 == 0:
            print(f"O{floor}{room}", end= ' ')
        elif floor % 2 != 0:
            print(f"A{floor}{room}", end=' ')

    print()