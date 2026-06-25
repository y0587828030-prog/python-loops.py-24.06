#part 1 Basics: for loop, 
# step 1

# fruits = ['apple', 'banana', 'cherry']
# for x in fruits:
#     print(x)

# #step 2
# x = range(1,6)
# for n in x:
#  print(n)

#  #step 3
#  x = range(0, 10, 2)
#  for n in x:
#     print(n) 

# #step 4
# fruits = ['apple', 'banana', 'cherry']
# for i , v in enumerate(fruits):
#    print(i , v)

# #step 5
# scores = {'Alpha': 80, 'Bravo': 95}
# for name ,score, in scores.items():
#     print(name , score )

# #step 6
# numbers = [1, 2, 3, 4, 5]
# sum = 0
# for number in  numbers:
#    sum +=number
# print(sum)  

#step 7 
#while
# i = 1
# while i <= 5:
#    print(i)
#    i += 1
# for n in range(1,i):
#    print(n)

#for
# x = range(1,6)
# for n in x:
#     print(n)

# #step 8
# matrix = [[1, 2, 3], [4, 5, 6]]
# for x in matrix:
#    for y in x:
#       print(y)

# #step 9
# list = [x ** 2 for x in range(1,11)]
# print(list)

# #step 10
# list = [x for x in range(0, 21, 2)]
# print(list)
# #option
# list = [x for x in range(1,21) if x % 2 == 0 ]
# print(list)

##Part 2 — Optional Advanced Basics
#step 1
names = ['Alpha', 'Bravo']
scores = [80, 95]
x = zip(names, scores)
print (list(x))

#step 2
list = [( x , x ** 2) for x in range(1, 6)]
print (list)