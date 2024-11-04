# def factorial(a):
#     if a < 0:
#         return "negative numbers"
#     elif a == 0:
#         return 1
#     else:
#         result = 1
#         for i in range(1, a + 1):
#             result *= i
#         return result


# print(factorial(1)) 
# # print(factorial(0))   
# # print(factorial(5))  
n = 10
num1 = 0
num2 = 1
next_number = num2 
count = 1
 
while count <= n:
    print(next_number, end=" ")
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2
print()
