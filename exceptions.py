try:
    print(x)
except:
    print("basic exception handled")

x = 1

try:
    print(x)
except NameError:
    print("we can choose what exceptions to catch")

try:
    x = 1
    if not type(x) is str:
        raise TypeError("only strings allowed")  # this is equivalent to throw
    print(x / 0)
except NameError:
    print("we can choose what exceptions to catch")
except TypeError:
    print("we can catch different types of errors like this")
else:
    print("No errors!")
finally:
    print("run this after")

# we can create custom Exceptions like this


class JustNotCool(Exception):
    pass


try:
    y = 0
    print(y)
    if not type(y) is str:
        raise JustNotCool("only strings allowed")
except JustNotCool:
    print("we can choose what exceptions to catch")
