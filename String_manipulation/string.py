#string_manipulation--[indexing and slicing]--

word="PROGRAMMING"

#Q1. print "G" using indexing
print(word[3])          #G

#Q2. print the first 4 characters 
print(word[0:4])        #PROG

#Q3. print GRAM
print(word[3:7])        #GRAM

#Q4.print the last 4 characters
print(word[7:])         #MING

#Q5. print the string backword
print(word[::-1])       #GNIMMARGORP
#------------------------------------------------------------------------------#
#Q6 print the word "COMPUTER" in 2 parts first line - COM ,next line - PUTER 

word2="COMPUTER"

print(word2[0:3])       #COM
print(word2[3:])        #PUTER

#Q7 only using indexing and slicing 
# print[PYTHON,NOHTYP,PROGRAMMING,GNIMMARGORP]

word3="PYTHONPROGRAMMING"

print(word3[0:6])       #PYTHON {using slicing}
print(word3[5::-1])     #NOHTYP {slicing with steps [strt:stop:step]}
print(word3[6:])        #PROGRAMMING {using slicing }
print(word3[:-12:-1])   #GNIMMARGORP {reversing desired word only}

#Q8 print exactly [ABCD,MLKJ,EFGHI,IJK]

word4="ABCDEFGHIJKLM"

print(word4[0:4])       #ABCD
print(word4[12:8:-1])   #MLKJ
print(word4[4:9])       #EFGHI
print(word4[8:11])      #IJK