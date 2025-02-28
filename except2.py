

# try:
#     causeError(0)
# except ZeroDivisionError:
#     print("something to do with zero division errors")
# except TypeError:
#     print("Something to do with type errors")
# except Exception as ex:
#     print(type(ex))
#     print(f"Some error happened: {ex}")

# # 1/0
# print("Hello!")


# # decorator function
# def handleExceptions(func):
#     def wrapper(*args):    
#         try:
#             func(*args)
#         except ZeroDivisionError:
#             print("something to do with zero division errors")
#         except TypeError:
#             print("Something to do with type errors")
#         except Exception as ex:
#             print(type(ex))
#             print(f"Some error happened: {ex}")
        
#     return wrapper


# @handleExceptions
# def myFunction():
#     print("I am in myFunction")


# @handleExceptions
# def causeError(n):
#     1 + n
#     1/n


# myFunction()
# causeError(0)
# causeError('a')


# class CustomException(Exception):
#     pass

# def causeError():
#     raise CustomException("This is a custom exception")

# causeError()
