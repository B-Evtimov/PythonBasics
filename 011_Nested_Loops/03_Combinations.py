n = int(input())
counter = 0

for n1 in range(n + 1):
    for n2 in range(n + 1):
        for n3 in range(n + 1):
            if(n1 + n2 + n3 == n):
                counter += 1

print(counter)