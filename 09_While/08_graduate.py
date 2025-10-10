student_name = input()
grade = 1
failed_years = 0
total_sum = 0
years_passed = 0

while grade <= 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed_years += 1
        if failed_years > 1:
            print(f"{student_name} has been excluded at {grade} grade")
            break
        continue

    total_sum += annual_grade
    years_passed += 1
    grade += 1

if years_passed == 12:
    average = total_sum / years_passed
    print(f"{student_name} graduated. Average grade: {average:.2f}")
