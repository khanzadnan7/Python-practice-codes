# Q1 print from the given list:
# print Python
# print PHP
# print ["java","C++","JavaScript"]
# print the list in backward ["PHP", "JavaScript", "C++", "Java", "Python"]
# print only ["Python", "C++", "PHP"]

languages = ["Python","Java","C++","JavaScript","PHP"]

print(languages[0])
print(languages[-1])
print(languages[1:4])
print(languages[::-1])
print(languages[0:5:2])

# changing the elements of the list :
# at index 1 put kotlin
# at index 4 put Ruby
# at index 2 put C 
# print the new list 

languages[1] = "Kotlin"
languages[4] = "Ruby"
languages[2] = "C"

print(languages)

# adding elements to the list 

language =["Python","Java","C++"]

language.append("JavaScript")
language.append("PHP")
language.append("Ruby")

print(language)

# inserting elements to the desired index

language.insert(2,"JavaScript")
language.insert(1,"Kotlin")
language.insert(0,"Ruby")
print(language)

# given list lang 

lang = ["Python", "Java", "C++", "PHP"]

# produce this result :

['JavaScript', 'Python', 'Java', 'Kotlin', 'C++', 'Ruby', 'PHP']

lang.insert(0,"JavaScript")
lang.insert(3,"Kotlin")
lang.insert(5,"Ruby")

print(lang)

# removing items from the list by value

# given list :

lang = ["Python", "Java", "C++", "JavaScript", "PHP", "Ruby"]

# remove "C++"
# remove "Python"
# remove "Ruby"

lang.remove("C++")
lang.remove("Python")
lang.remove("Ruby")

print(lang)

# produce result from the given list ['Python', 'C++', 'JavaScript', 'Ruby']

lang = ["Python", "Java", "C++", "JavaScript", "PHP", "Ruby"]

lang.remove("Java")
lang.remove("PHP")
print(lang)

# removing items from the list using index

program = ["Python", "Java", "C++", "JavaScript", "PHP", "Ruby"]

program.pop(2)
program.pop(0)
program.pop(3)

print(program)