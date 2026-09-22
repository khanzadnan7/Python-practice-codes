# Q1 convert the given word in uppercase and lowecase
word = "PyThOn PrOgRaMmInG"

print(word.upper())
print(word.lower())

#Q2 capitalize the given word
word2 = "pYTHON iS fUN"

print(word2.capitalize())

#Q3 capitalize first letter of each word in the sentence 
sentence= "learning python is interesting"

print(sentence.title())

#Q4 remove the white spaces from the left,right and both
username = "   python_user   "

print(username.lstrip())
print(username.rstrip())
print(username.strip())

#Q5 replace the word coconut with python
sentence2 = "i am starting to like coconut"

print(sentence2.replace("coconut","python"))

#Q6 count the I S P in given sentence
 
sentence3 = "i like mississippi"

print(sentence3.count("i"))
print(sentence3.count("s"))
print(sentence3.count("p"))

#Q7 find the index number of first P O GRAM in the given word 

word3 = "PYTHONPROGRAMMING"

print(word3.find("P"))
print(word3.find("O"))
print(word3.find("GRAM"))

#Q8 check if sentence ,starts with-"python", ends with -".py",ends with -".txt"
sentence4 = "python_notes.py"

print(sentence4.startswith("python"))
print(sentence4.endswith(".py"))
print(sentence4.endswith(".txt"))

#Q9 character checking 

value = "12345"
value0 = "123abc"
value1 = "python"
value2 = "python123"

print(value.isalpha())
print(value.isdigit())
print(value0.isalpha())
print(value0.isdigit())
print(value1.isalpha())
print(value1.isdigit())
print(value2.isalpha())
print(value2.isdigit())

#---------------------------------------------------------------------------------

#bonus question 
#Your program must produce: "Python Programming Is Fun"
text = "   pYtHoN pRoGrAmMiNg Is FuN   "
print(text.strip().title())

#program must:
#Count how many times "Python" appears.
#Find the index of the first "Python".
#Check whether the sentence starts with "I".
#Check whether it ends with "interesting".
#Replace "Python" with "Java".

sentence0 = "I am learning Python and Python is interesting"

print(sentence0.count("Python"))    #counts how many times python appears
print(sentence0.find("Python"))     #finds the index of first python
print(sentence0.startswith("I"))    #check if sentence starts with "I"
print(sentence0.endswith("interesting"))    #chek if sentence ends with "interesting"
print(sentence0.replace("Python","Java"))   #replacing the word python with java 