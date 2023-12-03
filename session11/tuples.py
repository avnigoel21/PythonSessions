# l = [3 , "apple", 5, 2, 4]

# list = [3]

# print(type(list))

# tuple = (3) # wrong way to declare a tuple with single element
# tuple = (3,) # tuple with single element
# print(type(tuple))

# print(type(l))

# t = (6, 5 , 3, 7, 9)

# t[0] = 7  # throws an error (cannot update values in tuple)
# print(t[0]) # printing of values in tuple using iindexing

# print(type(t))


#tuple methods

# t = (6, 5 , 3, 7, 9 , 5)
#print(t.count(5))
#print(t.index(5))



s = "apple"
print(id(s))

l = [3 , "apple", 5, 2, 4]
t = (6, 5 , 3, 7, 9 , 5)

# print(len(s))
# print(len(l))
# print(len(t))


# list1 = ['cat', 'dog', 5]

# print(tuple(list1))


# print(list(('cat', 'dog', 5)))


# str = "hello"

# print(list(str))


import copy
l1 = ['h', 'e', 'l', 'l', 'o']


l2 = copy.copy(l1)
l3 = copy.deepcopy(l1)
print(l1)
print(l2)
print(l3)

l3[0] = "a"
l2[0] = "a"

print(l1)
print(l2)
print(l3)
