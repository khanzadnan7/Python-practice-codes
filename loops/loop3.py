# Write a program using nested loop that produces exactly: 1 1,1 2,1 3 till 4 3

for x in range(1,5):
    for y in range(1,4):
        print(x,y)

# Write a program using nested for loops that examines the numbers from 1 to 5 for x and 1 to 5 for y

for x in range(1,6):
    for y in range(1,6):
        if (x+y)%2 == 0:
            print(x,y)
        
# Use nested loops to display every pair of numbers whose product is 16 or less.
# given list :
print("here")
numbers = [2,4,6,8]
for x in numbers:
    for y in numbers:
        if (x*y) <= 16 :
            print(x,y)
