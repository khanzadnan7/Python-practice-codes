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

# write a function multiply(a,b) that returns the product of two numbers Store the result of multiply(6, 7) in a variable and print it

def multiply(a,b):
    return(a*b)

result=multiply(6,7)

print(result)

# Write a function square(n) that returns the square of a number. Store the result of square(8) and print that result minus 10


def square(n):
    return n*n

ans = square(8)

print(ans - 10)

# Write a function get_larger(a, b) that returns the larger number. If both numbers are equal, return either one of them
# Call the function with 12 and 20, store the returned value, and use an if/else statement to print whether that value is even or odd

def get_larger(a,b):
    if a>b:
        return(a)
    elif a == b:
        return(a)
    else:
        return(b)

answer = get_larger(12,20)

if answer % 2 == 0:
    print("Even")
else:
    print("Odd") 

# write a function named greet with a parameter name that defaults to "Guest". Call it once with a name and once without any argument.

def greet(name="Guest"):
    print(name)

greet("adnan")
greet()

# Write a function named bill that accepts price and a quantity parameter defaulting to 1. It should print the total bill. Test it with both a default quantity and a specified quantity

def bill(price,quantity=1):
    print(price*quantity)

bill(25)
bill(50,6)

# Write a function named power that accepts a number n and an exponent exp defaulting to 2. Return the result of raising n to exp. Test it with power(5) and power(2, 3)

def power(n,exp=2):
    return(n**exp)

result=power(5)
result0=power(2,3)

print(result)
print(result0)