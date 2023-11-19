# a = 6
# if (a == 7):
#     print("yes")
# elif(a>56):
#     print("no and yes")
# elif(a>56):
#     print("no and yes")
# else: 
#     print("I am optional")

#while loops
#initiazing a value, condition, increment
# i = 0
# while i<=10:
#     print("yes " + str(i))
#     i = i + 1

# print("Done")


# a = 2
# print(a)
# a += 4 # a = a + 4
# print(a)


fruits = ["mango", "watermelon" , "grapes" , "apple"]

# print(type(fruits))

# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i = i + 1


# for item in fruits:
#     print(item)



if(4 > 2):
    pass

# for i in range(10):
#     if i == 5:
#         continue # it instructs the program to skip this iteration
#     print(i)``

# i = 10
# while i>6:
#     pass

# print("done")


# Write a program to find whether a given number is prime or not entered the user
# using for loops
# 4 = 2 , 3, 

# 100 = 2 , 3 , 4, 5......99

num = int(input("Enter the number: "))
prime = True
for i in range(2, num):
    if(num % i == 0):
        prime = False
        break

if prime == True:
    print("number is prime")
else:
    print("not prime")


# Write a program to calculate the factorial of a given number using for loop
