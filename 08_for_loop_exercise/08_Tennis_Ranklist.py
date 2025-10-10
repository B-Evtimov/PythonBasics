
tournaments = int(input())
starting_points = int(input())


total_points = starting_points
earned_points = 0
wins = 0

for _ in range(tournaments):
    stage = input()
    if stage == "W":
        earned_points += 2000
        wins += 1
    elif stage == "F":
        earned_points += 1200
    elif stage == "SF":
        earned_points += 720


total_points += earned_points
average_points = earned_points // tournaments
win_percent = (wins / tournaments) * 100

# Изход
print(f"Final points: {total_points}")
print(f"Average points: {average_points}")
print(f"{win_percent:.2f}%")
