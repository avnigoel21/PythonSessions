# def func1():
#     return None

# ans = func1()
# print(ans)


# def func2():
#     pass

# ans = func2()
# print(ans)


# def func3():
#     return 

# ans = func3()
# print(ans)

# print('8th', end='       ')
# print('period is the worst :(')


# def happy_print(message):
#     print(message + " :)")

# happy_print("hello")
# happy_print("hi")


def collatz(number):
    if (number % 2) == 0 :
        next = number // 2
    else:
        next = number * 3 + 1
    print(next)
    return next

n = int(input())

while n != 1:
    n = collatz(n)


num = 4
if(num % 2):
    print("the number is even")
else:
    print("the number is odd")