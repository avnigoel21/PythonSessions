# regualr expresseion
import re

# def isPhoneNumber(phone_numebr):

#     phoneNumberRegex = re.compile(r'\d{3}-\d{3}-\d{4}')

#     if phoneNumberRegex.match(phone_numebr):
#         return True
#     else:
#         return False


# user_input = input("Enter your phone number: ")

# if isPhoneNumber(user_input):
#     print("valid phone number")
# else:
#     print("invalid phone number")



# phoneNumberRegex = re.compile(r'(\d{3}-\d{3}-\d{4})')

# mo = phoneNumberRegex.search('My number is 415-555-424.')

# print('Phone number found: ' + mo.group())
# #print(mo.group(2))

# and or 
# &   |

# regex = re.compile(r'apple | grapes')

# m = regex.search('apple and grapes')
# # print(m)
# print(m.group())

# # ?
# phoneNumberRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')

# a = phoneNumberRegex.search("my number is 455-566-7878")


# b = phoneNumberRegex.search("my number is 555-4242")

# print(a.group())
# print(b.group())



# *

regex = re.compile(r'Bat(wo)*man')

a = regex.search("The Adventures of Batman")
print(a.group())

b = regex.search("The Adventures of Batwoman")
print(b.group())

c = regex.search("The Adventures of Batwowowowoman")
print(c.group())

d = regex.search("The Adventures of manBat")
print(d.group())







