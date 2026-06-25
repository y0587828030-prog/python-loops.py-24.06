#part 1 Basics: for loop, 
# step 1

fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

#step 2
x = range(1,6)
for n in x:
 print(n)

 #step 3
 x = range(0, 10, 2)
 for n in x:
    print(n)

#step 4
fruits = ['apple', 'banana', 'cherry']
for i , v in enumerate(fruits):
   print(i , v)


list = ["yehoshua", "josh", "zalts"]
for i in enumerate(list):
    print(i)