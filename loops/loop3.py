# Write a program using nested loop that produces exactly: 1 1,1 2,1 3 till 4 3

for x in range(1,5):
    for y in range(1,4):
        print(x,y)

# Write a program using nested for loops that examines the numbers from 1 to 5 for x and 1 to 5 for y
# Display only the pairs where x + y is even.
for x in range(1,6):
    for y in range(1,6):
        if (x+y)%2 == 0:
            print(x,y)
        
# Use nested loops to display every pair of numbers whose product is 16 or less.
# given list :


numbers = [2,4,6,8]
for x in numbers:
    for y in numbers:
        if (x*y) <= 16 :
            print(x,y)

# given list :

numbers = [3, 7, 12, 5, 18, 21, 9, 24, 11]

# find the first number in the list that is greater than 10 and divisible by 3, display it, and then stop searching

for x in numbers:
    if x > 10 and x % 3 == 0:
        print(x)
        break


# given that :

numbers = [4, 25,-3, 10, 7, -8, 15, 2, 21, 6]

# write a program that displays the positive odd numbers in this list, but stops searching when it encounters the number 15

for x in numbers:
    if x == 15:
        break
    if x > 0 and x % 2 != 0:
        print(x)
        
# write a program that:
# Loops through the list.
# Stops when it encounters 25, without printing 25
# Skips negative numbers and numbers divisible by 3
# Prints the remaining numbers
# Counts how many numbers it printed and displays the count at the end

numbers = [12, -5, 7, 18, 4, 21, 10, -3, 25, 8, 30]
count = 0
for x in numbers:
    if x == 25:
        print(count,"numbers are printed")
        break
    if x < 0 or x % 3 ==0:
        continue
    print(x)
    count +=
#---------------------------------------------------------------------------------------------------------------------------------------------