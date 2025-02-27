
# def causeError():
#     1/0

# def callCauseError():
#     causeError()

# # callCauseError()


# try:
#     1/0
#     1 + 'a'
# except ZeroDivisionError:
#     print("Zero division error happened")
# except TypeError:
#     print("TypeError occurred")
# except Exception as e:
#     print("Some error occurred", type(e))


# print("hello")


def handleExceptions(func):
    def wrapper(*args):
        try:
            func(*args)
        except ZeroDivisionError:
            print("Zero division error happened")
        except TypeError:
            print("TypeError occurred")
        except Exception as e:
            print("Some error occurred", type(e))
    return wrapper


@handleExceptions
def causeError(n):
    print(1 + n)

causeError('a')
causeError(1)
causeError(2.0)
causeError(True)


