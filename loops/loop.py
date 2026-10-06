# structure

# while condition:
#   code to repeat

# Write a program that prints the numbers from 1 to 10 using a loop

num = 1

while num <= 10:
    print(num)
    num +=1

# write a program that print 1 to 10 in reverse and blast off at the end 

count = 10

while count >=1:
    print(count)
    count -= 1
print("Blast off!")

# write a program that calculates the sum of all integers from 1 to 10 and prints the final result

add = 1
box = 0
while add <= 10:
    box += add
    add += 1
print(box)

# write a program that examines numbers from 1 to 10 
# display each number
# Stop the loop as soon as it reaches 6.
# display a message after the loop ends

number = 1

while number <= 10:
    if number == 6:
        break
    print(number)
    number += 1

print("end of the loop")

# write a program that examines numbers from 1 to 30.
# Find the first number that is divisible by both 4 and 7. Display that number and stop searching.

num = 1

while num <= 30:
    if num%4 == 0:
        if num%7 == 0 :
            print(num)

    num += 1

# write a program that examines numbers from 1 to 15
# skip numbers divisible by 3 and display all the remaining numbers

start = 1

while start <= 15:
    if start%3 == 0:
        start += 1
        continue
    print(start)
    start += 1

# write a program that :
# examines every element in the list 
# skips values that are not positive
# display only positive value

number = [12,-5,8,-2,0,15,-7,20,1]
i=0
box=len(number)

while (box>0):
    if number[i]<=0:
        i+=1
        box-=1
        continue

    print(number[i])
    i+=1
    box -=1