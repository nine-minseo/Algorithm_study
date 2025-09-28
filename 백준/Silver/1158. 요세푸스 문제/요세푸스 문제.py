import sys
n, k = map(int, sys.stdin.readline().strip().split())
people = []

for i in range(1, n+1):
    people.append(i)


print("<", end="")

index = k-1
print(f"{people[index]}", end="")
for i in range(2, n+1):

    people.pop(index)
    index += k-1
    if index >= len(people):
        index %= len(people)
    print(f", {people[index]}", end="")

print(">", end="")