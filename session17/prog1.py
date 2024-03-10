# # '''this is a comment, 
# # jhbcjmbs
# # gvchnds,
# # gsavj
# # bdjba
# # hi, i am aditi'''


# # # string1 = "this is a string
# # # hi, i am aditi"
# # str2 = 'this is a string'


# # string = '''this is a string, 


# #             hi, i am aditi'''

# # #s = 'aditi\'s favourite lang is python.'
# # print(string)
# # # # 'aditi"s favourite """ lang is python.''


# # # str2 = ''' aditi's\\ lang is\t\n"python" '''
# # # print(str2)

# # # path = "C:\Windows\System32\cmd.exe "



# # list = [6, 81, 8, 2, 9]
# # list[0]
# # print(list[1:3])

# # #indexing
# # #         012345678910
# # string = "apple is a fruit"

# # # string slicing



# # print(string[1:3])
# # print(string[6:10])




# string = "apple"
# print(string[0])

# if('b' not in string):
#     print("yes")
# else:
#     print("not present")

# # string[0] = 'b' # doesnot work (will give an error)
# # print(string)
# #print(string.replace('apple' , 'bpple'))


# print(1+2)
# print("1" + "2")


# greeting = "Good Morning, "
# name = input("Enter your name: ")
# age = 9

# print(greeting + name + "." + " Your age is : " + str(age))



# name = 'Al'
# age = 4000
# location = "India"

# print('My name is %s. I am %s years old, living in %s.' % (name, age, location))


# print(f"My name is {name}. I am {age} years old, living in {location}.")



# # Write a program to fill in a letter template given below with name and date Taken by the user.
# letter = ''' Dear <|NAME|>
#                 You are selected!
#             <|DATE|> '''

# # name = input("enter your name:")

# # letter.replace("<|NAME|>" , name)

# # Write a program to foramt the following letter using escape sequence chararcters

# letter = "Dear harry, course is nice, have a nice day!"


# #Create a program that asks the user for their name, age, and 
# #favorite color. Use f-strings to print a personalized message incorporating these inputs.


# #Create a program that prints the following multiline string and 
# #then extracts and prints the word "Python" using string indexing.

# multiline_string = '''Welcome to
#   Python Programming'''

# print(multiline_string[13:20])


# # Write a program that takes a user's input for a file path 
# #(e.g., C:\Users\John\Documents\file.txt) and converts it into a formatted string using raw strings.


# user = "C:\Users\John\Documents\file.txt"
# print(rf"this is my {user}") 


# var = "Apple"
# var = var.upper()
# print(var)

# str = "apple".upper()



# while True:
#     print('Enter your age:')
#     age = input()
#     if age.isdecimal():
#         break
#     print('Please enter a number for your age.')


# email = input()
# if(email.endswith('.com') or email.endswith('.in') ):
#     print(email)
# else:
#     print("re-enter")


# str = ' and '.join(['cats', 'rats', 'bats'])
# print(str)

# print(str.split(" and "))


# spam = '''Dear Alice,
# How have you been? I am fine.
# There is a container in the fridge
# that is labeled "Milk Experiment."

# Please do not drink it.
# Sincerely,
# Bob'''

# print (spam.split('\n'))

# print('Hello, world!'.partition(','))


# before, sep, after = 'Hello, world!'.partition(' ')

# print(before)



# str= "apple"

# str = str.rjust(10, "*")

# print(str)

# s = '-'.join('There can be only one.'.split())
# print(s)
# str="   hi          avni here " 

# spam = 'SpamSpamBaconSpamEggsSpamSpam'

# print(spam.strip('apS'))

# s = ord('B')
# print(s)


# import pyperclip

# str = "hi, avni here"

# pyperclip.copy(str)
# pyperclip.paste()

# str1 = "my isname isisis jameis isis bond";
# sub = "is";
# print(str1.count("is"  , 4 ))

s1 = str("a")
s2 = "a"
if (s1 == s2):
    print("yes")

str = " hi avni !" 