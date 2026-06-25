# ##Part 1 — Basics: while loop, break, continue, looping over lists and dicts

# # stap 1
# i = 1
# while i <= 5:
#     print(i)
#     i = i +1

# #stap 2
# i = 10
# while i >= 1:
#     print(i)
#     i = i -1

# #stap 3
# total = 0
# i = 1
# while i <= 10:
#     total = total + i
#     i = i + 1
# print(total)

# #stap 4
# items = [2, 4, 6, 8]
# index = 0
# while index < len(items):
#     current_number = items[index]
#     if current_number >5:
#         print(current_number)
#         break
#     index = index + 1

# #stap 5
# i = 0
# while i < 10:
#     i = i +1
#     if i % 2 == 1:
#         continue
#     print(i)

# #stap 6
# agents = ['Alpha', 'Bravo', 'Charlie']
# index = 0 
# while index < len(agents):
#     print(agents[index])
#     index += 1

# #stap 7
# scores = {'Alpha': 80, 'Bravo': 95, 'Charlie': 70}
# scores_list = list(scores.items())
# index = 0
# while index < len(scores_list):
#     current_item = scores_list[index]
#     name = current_item[0]
#     score = current_item[1]
#     print(name, score)
#     index = index + 1

# #stap 8
# naber = 1
# while naber <= 100:
#     naber = naber * 2
#     print (naber)

# #stap 9
# data = [3, 7, 2, -1, 5]
# total_sum = 0
# index = 0

# while index < len(data):
#     current_value = data[index]
#     if current_value == -1:
#         break
#     total_sum = total_sum + current_value
#     index = index + 1
# print(total_sum)

# #stap 10
# n = 10
# i = 1
# while i <= 10:
#     result = n * i
#     print(n, "x", i, "=", result)
#     i =i + 1

# ##Part 2 — Optional Advanced Basics
#  #step 1
# items = ['a', 'x', 'b', 'x', 'x']
# i = 0
# while i < len(items):
#     current_item = items[i]
#     if current_item == "x":
#         items.remove(current_item)
#         print(items)
#     else:
#         i = i + 1

# #step 2
# matrix = [[1, 2, 4, 5], [3, 4], [5, 6]]
# x = 0
# y = 0
# while x < len(matrix):
#     while y < len(matrix[x]):
#         current_value = matrix[x][y]
#         print(current_value)
#         y += 1
#     y = 0
#     x += 1  

# #step 3

# my_list = [10, 20, 30, 40, 50]
# current_list = []
# i = len(my_list) - 1
# while i >= 0:
#     current_list.append(my_list[i])
#     i -= 1
# print(current_list)

#step 4
# data = [10, 30, 55, 20, 80]
# i = 0
# while i < len(data) and data[i] <= 50:
#     i += 1
# print(i)

#step 5
secret = 42
guesses = [10, 30, 42]
index = 0
attempts = 1
while index < len(guesses) and guesses[index] != secret:
    attempts += 1
    index += 1
print(attempts)








    