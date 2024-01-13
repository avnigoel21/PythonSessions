# from pprint import pprint



# mydict = {
#     "fast" : "in a quick manner",
#     "Aditi" : "a friend",
#      5: 7,
#      7.8 : "a number",
#      "Aditi" : "a dancer",
#      "avantika" : "a friend",
#      "marks": [1, 4, 8],
#      "anotherDict" : {"Aditi" : "a coder"},
#      'apple' : 8 
# }
# # print(mydict)
# pprint(mydict)
# pprint.pformat(mydict)



# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}

# for character in message:
#     count.setdefault(character, 0)
#     count[character] = count[character] + 1

# print(count)
# print(pprint.pformat())

# print(pprint.pformat(mydict))

# format = pprint.pformat(mydict)
# print(format)



# print("hi, I am a dancer \
# thanks")

# list = [5, 8, 8, 4, 7]
# # print(list.sort())
# list.sort()
# print(list)

# a =

str = "AVNI@GMAIL.COM"
# AVNI@GMAIL.COM

# print(str.lower())
# print(str)



# a = 5
# print(a)
# a += 3
# print(a)
# a *= 2
# print(a)
# a //= 1
# print(a)

# list = [5, 8, 8, 4, 7]

# for i in range(1, 3):
#     print(list[i])
#     i+=1


# cat = ['fat', ‘gray’, ‘loud’]
# size = cat[0]
# >>> color = cat[1]
# >>> disposition = cat[2]

# >>> cat = [‘fat’, ‘gray’, ‘loud’]
# >>> size, color, disposition = cat

# The number of variables and the length of the list must be exactly equal, or Python will give you a ValueError

# >>> cat = [‘fat’, ‘gray’, ‘loud’]
# >>> size, color, disposition, name = cat

# >>> x, y = 1, 2
# >>> x, y = y, x


# a , b, c , d = my_tuple
# print(a, b, c , d)

tuple1 = (45, 45, 45, 45)
# print(tuple1)
set1 = set(tuple1)

same = len(set1) == 1
print(same)
# print(set1)

from operator import itemgetter

tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=itemgetter(1)))
print(tuple1)