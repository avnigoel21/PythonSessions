# functions
# 1) built in function - print, len, range, input
# 2) user-defined functions - a group of statements performing a specific task.


# DRY - DONT REPEAT YOURSELF

# parametrs/arguments

# function creation

# no return & no arguments
def func1 ():
    print("hello")

# no return & with arguments
def func2 (a, b):
    sum = a + b
    print(sum)

# with return & with arguments
def func3 (a, b):
    return a + b 

# with return & no arguments
def func4():
    a = 3
    b = 5
    return a+b


# function calling
func1()

func2(6, 2)

s = func3(6, 2)
print(s)

s1 = func4()
print(s1)


# with return & with arguments
# with return & no arguments
# no return & with arguments
# no return & no arguments