jury_count = int(input())
total_score = 0
presentation_count = 0

while True:
    presentation_name = input()
    if presentation_name == "Finish":
        break

    current_sum = 0
    for _ in range(jury_count):
        grade = float(input())
        current_sum += grade

    average_grade = current_sum / jury_count
    total_score += average_grade
    presentation_count += 1

    print(f"{presentation_name} - {average_grade:.2f}.")

final_assessment = total_score / presentation_count
print(f"Student's final assessment is {final_assessment:.2f}.")
