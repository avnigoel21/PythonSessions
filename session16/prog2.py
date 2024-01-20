# my_dict = {'apple' : 3 , 'banana' : 2 , 'orange' : 5}

# # print key-value pairs using a for loop

# for i, j in my_dict.items():
#     print(i, j)

# print(my_dict.items())


# # summing up values in a dict

# expenses = {'groceries' : 100 , 'clothing' : 50 , 'entertainment' : 30}

# total_expenses = 0
# for i in expenses.values():
#     total_expenses  = total_expenses + i
#     #total_expenses += total_expenses

# print(total_expenses)

# expenses.update


# # Delete a list of keys from a dictionary
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }

# # Keys to remove
# keys = ["name", "salary"]


# for i in keys:
#     sample_dict.pop(i)

# print(sample_dict)

#Create a dictionary by extracting the keys from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

new_dict = {}

for i in keys:
    new_dict[i] = sample_dict[i]

print(new_dict)



list = [4 ,8 , 9]
print(list.pop())



