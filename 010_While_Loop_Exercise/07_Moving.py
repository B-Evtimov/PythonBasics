width = int(input())
length = int(input())
height = int(input())

free_space = width * length * height
used_space = 0

while True:
    command = input()
    if command == "Done":
        print(f"{free_space - used_space} Cubic meters left.")
        break

    boxes = int(command)
    used_space += boxes

    if used_space > free_space:
        print(f"No more free space! You need {used_space - free_space} Cubic meters more.")
        break
