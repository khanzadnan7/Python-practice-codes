#Structure

# if condition1:
    # if condition1 is True
# elif condition2:
    # if condition2 is True
# else:
    # if none of the above are True


# write an if statement that print Positive if number is greater tha 0

number = 10

if number > 0:
    print("Positive")

# write an if else that print Positive if the number is greater than 0,otherwise Negative

number = -5

if number > 0 :
    print("Positive")
else:
    print("Negative")

# print Eligible if age is 18 or greater ,otherwise Not Eligible
 
age = 20

if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")

# write a program that checks whether 
# password is "Python123" if yes print Correct Password
# if not print Wrong Password

password = "Python123"

if password == "Python123":
    print("Correct Password")
else:
    print("Wrong Password")

# Write an if/elif/else that prints:
# if greater than 0, positive 
# if less than 0 , Negative
# if equals to 0 , zero

number = 0

if number > 0:
    print("Positive")
elif number < 0: 
    print("Negative")
else:
    print("Zero")

# Create this grading system:
# 90 or above - A
# 80-89 - B
# 70-79 - C
# 60-69 - D
# below 60 - F

marks = 85

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# Age category
# if age is below 13,Child
# if age is 13-19 ,Teenage
# if age is 20 or above ,Adult

age = 20

if age < 13:
    print("Child")
elif age <=19:
    print("Teenage")
elif age >=20:
    print("Adult")
else :
    print("Inavlid number")

# temprature

temprature = 21

if temprature >= 30:
    print("Hot")
elif temprature >=20:
    print("Warm")
elif temprature >=10:
    print("Cool")
else:
    print("Cold")