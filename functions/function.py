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

# define student(name,course) that prints boht value cal it using keyword argument in reverse order

def student(name,course):
    print(name,course)


student(course="DS-AI",name="adnan")

# Define calculate(a, b, operation) that prints the sum of a and b,
# Call it using a mix of positional and keyword arguments

def calculate(a,b,operation):
    print(a+b,operation)


calculate(20,operation="add",b=10)

# Define show_details(name, age, city) that prints all three values. Call it twice: once using only positional arguments, and once using only keyword arguments in a different order.

def show_details(name,age,city):
    print(name,age,city)

show_details("adnan",23,"japan")
show_details(age=23,city="japan",name="adnan")


# using args to calculate desired numbers of variables

def add_all(*nunnu):
    total = 0
    for numb in nunnu:
        total += numb
    return total
show = add_all(10,20)
print(show)

# Write a function show_numbers(*args) that prints all the arguments it receives. Call it with two numbers, four numbers, and one number.

def show_num(*args):
    print(*args)

show_num(50,20)
show_num(5,9,8,7)
show_num(7)

# write a function multiply_all(*args) that returns the product of all the numbers passed to it. Test it with three numbers and five numbers

def multiply_all(*num):
    result = 1
    for x in num:
        result *= x
    return result

show=multiply_all(1,3,5)
print(show)
show0=multiply_all(2,3,4,5)
print(show0)

# Write a function count_numbers(*args) that counts how many arguments are even. Return the count and test it with a mixture of positive, negative, odd, and even integers



def count_number(*args):
    box = 0
    for x in args:
        if x % 2 == 0:
            box +=1
    return box


show=count_number(1,5,-9,8,6,-2,4,0,20,-5,28,99,37,12)
print(show)