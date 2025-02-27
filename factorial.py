# def factorial(n):
#     if type(n) != int:
#         return None
#     if n < 0:
#         return None

#     fact = 1
#     count = 1
#     while count <= n:
#         fact = fact * count
#         count = count + 1
#     return fact

def factorial(num):
    if type(num) != int:
        return None
    if num < 0:
        return None

    if num == 0:
        return 1

    return num * factorial(num-1)
    

print('factorial of 5 is: ' + str(factorial(5)))
