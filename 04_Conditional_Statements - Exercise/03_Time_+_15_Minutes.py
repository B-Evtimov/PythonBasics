hour = int(input())
minute = int(input())

minute += 15

if minute >= 60:
    minute -= 60
    hour += 1

if hour >= 24:
    hour = 0

if minute < 10:
    print(str(hour) + ":0" + str(minute))
else:
    print(str(hour) + ":" + str(minute))