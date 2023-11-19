#spam  = ['a', 'b', 'c', 'd']
# # spam[2] = 'hello'
# # print(spam)

# print(spam[int(int('3' * 2) // 11)]) 

# print( spam[-2])

# print(spam[:2])

# bacon = [3.14, 'cat', 11, 'cat', True]
# print(bacon.index('cat'))

# bacon.append(99)
# print(bacon)

# bacon.remove('cat')

# bacon.pop(3)
# print(bacon + spam)


# print(spam * 3)


# spam = "cat"
# print(len(spam))


spam = ['cat', 'bat', 'rat', 'elephant']

# a = len(spam)

# for i in range(a):
#     print(i)

# print("bat" in spam)

# print("bat" not in spam)


# enumerate() is used to iteratee over a list along with the index of the element 
for index, i in enumerate(spam):
    print(index , i)

for i in range(len(spam)):
    print(i)

for i in spam:
    print(i)

# del spam[1]
# print(spam)

# a = 2
# print(a)
# a  = a + 1
# print(a)



# catNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +
#       ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]  # list concatenation
# print('The cat names are:')
# for name in catNames:
#     print(name)


