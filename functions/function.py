# function
# structure

# def ... ():
#   instruction    

# write a function named show_message that prints "Python is interesting!"
# call it twice

def show_message():
    print("Python is interesting")


show_message()
show_message()

# Write a function named square that accepts a number and prints its square
# Call it with 4, 7, and 10

def square(a):
    print(a*a)

square(4)
square(7)
square(10)

# Write a function named compare that accepts two numbers and prints the larger number

def compare(a,b):
    if a>b:
        print(a,"is greater")
    elif b==a:
        print(a,"and",b,"are Equal")
    else:
        print(b,"is greater")

compare(20,10)
compare(49,58)
compare(77,77)
