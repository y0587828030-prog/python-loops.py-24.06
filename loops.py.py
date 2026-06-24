##Part 1 — Basics: while loop, break, continue, looping over lists and dicts
# stap 1
i = 1
while i <= 5:
    print(i)
    i = i +1

#stap 2
i = 10
while i >= 1:
    print(i)
    i = i -1

#stap 3
total = 0
i = 1
while i <= 10:
    total = total + i
    i = i + 1
print(total)

#stap 4
items = [2, 4, 6, 8]
index = 0
while index < len(items):
    current_number = items[index]
    if current_number >5:
        print(current_number)
        break
    index = index + 1

#stap 5
i = 0
while i < 10:
    i = i +1
    if i % 2 ==1:
        continue
    print(i)

#stap 6
agents = ['Alpha', 'Bravo', 'Charlie']
index = 0 
while index < len(agents):
    print(agents[index])
    index += 1