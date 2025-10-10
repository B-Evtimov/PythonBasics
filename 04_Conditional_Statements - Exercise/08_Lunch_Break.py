import math

name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
breathing_time = break_time / 4
free_time = break_time - lunch_time - breathing_time

if free_time >= episode_time:
    print(f"You have enough time to watch {name} and left with {math.ceil(free_time - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {math.ceil(episode_time - free_time)} more minutes.")