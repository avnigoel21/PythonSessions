# '''this is a comment, 
# jhbcjmbs
# gvchnds,
# gsavj
# bdjba
# hi, i am aditi'''


# # string1 = "this is a string
# # hi, i am aditi"
# str2 = 'this is a string'


# string = '''this is a string, 


#             hi, i am aditi'''

# #s = 'aditi\'s favourite lang is python.'
# print(string)
# # # 'aditi"s favourite """ lang is python.''


# # str2 = ''' aditi's\\ lang is\t\n"python" '''
# # print(str2)

# # path = "C:\Windows\System32\cmd.exe "



# list = [6, 81, 8, 2, 9]
# list[0]
# print(list[1:3])

# #indexing
# #         012345678910
# string = "apple is a fruit"

# # string slicing



# print(string[1:3])
# print(string[6:10])




string = "apple"
print(string[0])

if('b' not in string):
    print("yes")
else:
    print("not present")

# string[0] = 'b' # doesnot work (will give an error)
# print(string)
#print(string.replace('apple' , 'bpple'))


print(1+2)
print("1" + "2")


greeting = "Good Morning, "
name = input("Enter your name: ")
age = 9

print(greeting + name + "." + " Your age is : " + str(age))



name = 'Al'
age = 4000
location = "India"

print('My name is %s. I am %s years old, living in %s.' % (name, age, location))


print(f"My name is {name}. I am {age} years old, living in {location}.")



# Write a program to fill in a letter template given below with name and date Taken by the user.
letter = ''' Dear <|NAME|>
                You are selected!
            <|DATE|> '''


# Write a program to foramt the following letter using escape sequence chararcters

letter = "Dear harry, course is nice, have a nice day!"


#Create a program that asks the user for their name, age, and 
#favorite color. Use f-strings to print a personalized message incorporating these inputs.


#Create a program that prints the following multiline string and 
#then extracts and prints the word "Python" using string indexing.

multiline_string = '''Welcome to
  Python Programming'''


# Write a program that takes a user's input for a file path 
#(e.g., C:\Users\John\Documents\file.txt) and converts it into a formatted string using raw strings.

#print(rf"thiis is my {string}") -> just an example