# Logical operators(and ,or, not)

# write and if statement that prints "Eligible" only if age is 18 or above and 60 or below

age = 25

if age >= 18 and age <= 60 :
    print("Eligible")
else :
    print("Not Eligible")

# print "Weekend" if the day is "Saturday" or "Sunday" other wise "weekday"

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print(day,"is Weekend")
else:
    print(day,"is Weekday")

# if given list doesnt have "Ruby" print "Ruby is not available"

languages = ["Python","Java","C++"]

if "Ruby" not in languages:
    print("Ruby is not available")
else:
    print("Ruby is available")

# print "Allowed" only if age is 18 or above and the person has an id otherwise not allowed

age = 22
id = True

if age>=18 and id:
    print("Allowed")
else:
    print("Not Allowed")

# A person cna enter a competition if : 
# if their age is 18 or above
# and they either have student or employee status

age = 18
status = "Employee"

if age >= 18 and (status == "Student" or status == "Employee"):
    print("Allowed")
else:
    print("Not Allowed")

# using not operator

# write an if/else statement that :
# print "Access denied" if the username is not "admin"
# otherwise prints "Access granted"

username = "admin"

if not username  == "admin":
    print("Access denied")
else:
    print("Access granted")

# A website allows login only when:
# the username is "admin" or "user" 
# and the account is not blocked

username= "user"
is_blocked = False 

if (username == "admin" or username == "user") and not is_blocked : #the code inside the parantheses will get executed first
    print("Login successfull")
else:
    print("Login failed")

# A student qualifies for a scholarship if :
# their marks are at least 80
# and they belong to either "Science" or "Computer Science"
# and they have not been disqualified

marks = 85
stream = "Computer Science"
disqualified = False

if (stream == "Science" or stream == "Computer Science") and marks >= 80 and not disqualified :
    print("Qualified")
else:
    print("Not qualified")

#-----------------------------------------------------------------------------------------------------------------------------------

# A cinema offers free entry to customers who satisfy it eligibility policy
# customer aged 18 or older can enter
# customer aged 13-17 can enter if accompanied by a parent
# customer below 13 cannot enter
# customers who have been banned cannot enter regardles of age 

age = 16
with_parent = True
is_banned = False 

if not is_banned:
    if age < 13 :
        print("Entry Denied, age is below 13")
    elif (age >=13 and age <=17) and with_parent:
        print("Entry Allowed")
    elif age >=18:
        print("Entry Allowed")
    else:
        print("Entry Denied")
else:
    print("Entry denied ,You Are Banned")