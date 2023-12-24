from pprint import pprint



mydict = {
    "fast" : "in a quick manner",
    "Aditi" : "a friend",
     5: 7,
     7.8 : "a number",
     "Aditi" : "a dancer",
     "avantika" : "a friend",
     "marks": [1, 4, 8],
     "anotherDict" : {"Aditi" : "a coder"},
     'apple' : 8 
}
# print(mydict)
pprint(mydict)
pprint.pformat(mydict)



message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# print(count)
# print(pprint.pformat())

# print(pprint.pformat(mydict))

# format = pprint.pformat(mydict)
# print(format)

