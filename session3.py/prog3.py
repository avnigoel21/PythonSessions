# def average(n1, n2, n3):
#     return (n1+n2+n3)/3.0


# # num1 = int(input("enter the number 1: "))
# # num2 = int(input("enter the number 2: "))
# # num3 = int(input("enter the number 3: "))


# result = average(2, 4 , 6)
# print(result)
# result = average(n3 = 2, n1 = 4 , n2 =  6)
# print(result)

#---------------------------------------------------------

def average(n1, n2, n3 = 6):
    return (n1+n2+n3)/3.0


num1 = int(input("enter the number 1: "))
num2 = int(input("enter the number 2: "))
num3 = int(input("enter the number 3: "))

result = average(num1, num2)
print(result)
result = average(num1, num2, num3)
print(result)



