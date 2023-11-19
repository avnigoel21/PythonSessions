# def func1():
#     n = 5 # local variable
#     print("n value is: ", n)

# def func2():
#     n = 10  # local variable
#     print("n value is: ", n)
#     func1()

# func2()

p = 10 # global variable

# def func1():
#     n = 4
#     print(n)
#     p = 5
#     print(p)
#     func2()

def func2():
    n = 20 # local variable
    if n < 0:
        print("hello")
    print(n)
    n = n-1 
    func2()
   

# recursion - function calling itself
    
func2()

