# for loop
# structure 
# for ... in variable:
#   intstruction

# print all fruits from the list 

fruits = ["apple","banana","mango","orange"]

for var in fruits:
    print(var)

# given a list of numbers :

numbers = [4,7,12,15,20,23,30]

# write a for loop that display ont the numbers greater than 15

for var in numbers:
    if var <= 15:
        continue
    print(var)

# given a list :

numbers = [3,8,12,17,21,25,30]

# write a for loop that displays the numbers one by one ,but stops completely when it reaches 21

for var in numbers:
    if var >= 21:
        break
    print(var)

# given a list :

numbers = [5,12,7,20,9,30,14,25]

# write a for loop that displays every number except number divisible by 5

for var in numbers:
    if var%5 == 0:
        continue
    print(var)

# given a list :

numbers = [ 4,7,12,15,18,21,25,28,30]

# write a for loop that :
# skips number divisible by 3
# stops completely when it reahces 25
# displays every other number

for var in numbers:
    if var%3 == 0:
        continue
    if var == 25 :
        break
    print (var)

#----------------------------------------------------------------------------------------------------------

# generate number from 1 to 10 using range()

for x in range(1,11):
    print(x)

# write a for loop using range () that displays all even numbers from 2 through 20

for x in range (2,21,2):
    print(x)

# write a for loop using range() that displays the number from 10 to 1 

for x in range(10,0,-1):
    print(x)

# write a for loop using range()that examines the numbers from 1 through 20 and displays only the numbers that are divisible by 3

for x in range(1,21):
    if x % 3 == 0:
        print(x)

#write a for loop using range()that starts at 1, displays the numbers, and stops completely when it reaches 8

for x in range(1,16):
    if x == 8:
        break
    print(x)

# write a program that examines the numbers from 1 through 30
# display numbers that are divisible by 2
# ignore numbers that are divisible by 3
# stop completely when it reaches a number greater than 25

for x in range(1,31):
    if x > 25:
        break
    if x % 3 == 0:
        continue
    if x % 2 == 0:
        print(x)

