step 1
#creating a str variable for storing 12 unique letters.

windows_serial_numbers = "abc-def-ghi-jkl"

step 2
#making four new str variables and storing above letters in them equally.
#replacing the existing letters into new letters

leta = windows_serial_numbers[0:3].replace("abc", "aaa")
letb = windows_serial_numbers[4:7].replace("def", "bbb")
letc = windows_serial_numbers[8:11].replace("ghi", "ccc")
letd = windows_serial_numbers[12:15].replace("jkl", "ddd")

#step3
#making a new str variable and storing the altered value of above four variable into it.
#printing the new altered code on the display without changing the value of original str variable

encoded_new_serial_numbers=leta+"-"+letb+"-"+letc+"-"+letd
print(encoded_new_serial_numbers)

#string slicing 
#text=[start:stop]

word= "elephant" 
print("current word -",word)

print("1)after slicing -",word[::-1]) #reverse the string
print("2)after slicing -",word[2:]) #remove the starting alphabate upto the index number -1
print("3)after slicing -",word[::2])
print("4)after slicing -",word[:4])
print("5)after slicing -",word[0:4])

word ="o" + word[1:]
print("after slicing" , word)

word= word.replace("ele","lel")
print(word)