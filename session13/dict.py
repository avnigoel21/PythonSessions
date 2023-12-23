# spam = {'cat' : 42 , "dog" : 35}

# print('cat' in spam)

# print("cat" in spam.keys())




# l1 = [8]
# l3 = ["apple"]
# l2 = [None]

# l = [None] * 10
# print(l)
# print(len(l))


# list1 = ['xyz', 'xara', 'xYnative']
# print (max(list1))



# Write a program to create a dictionary of hindi words with values as their English Translation, 
# Provide user with an option to look it up.

# create a empty dictionary
# allow 4 friends to enter their favourite language as values and use keys as their names.


favlang= {}

a = input("Enter your fav lang Sonali: \n")
b = input("Enter your fav lang Rahul: ")
c = input("Enter your fav lang Rohan: ")
d = input("Enter your fav lang Harshita: ")


favlang['Sonali'] = a
favlang['Rahul'] = b
favlang['Rohan'] = c
favlang['Harshita'] = d

print(favlang)


# mydict = {
#     "fast" : "in a quick manner",
#     "Aditi" : "a friend",
#      5: 7,
#      7.8 : "a number",
#      "Aditi" : "a dancer",
#      "avantika" : "a friend",
#      "marks": [1, 4, 8],
#      "anotherDict" : {"Aditi" : "a coder"},
    
# }

# # update_dict = {
# #     "rahul" : "a friend",
# #     "ritu" : "a friend",
# #     "rohan" : "a friend",
# # }

# # mydict.update(update_dict)
# # print(mydict)


# spam = {'name': 'Pooka', 'age': 5}
# if 'color' not in spam:
#     spam['color'] = 'black'

# print(spam)

# spam = {'color': 'Pooka', 'age': 5}
# print(spam.setdefault('color' , 'black'))
# print(spam)