def hello():
    print("Hello World!")


hello()


def sum(num1=0, num2=0):
    if type(num1) is not int or type(num2) is not int:
        return 0

    return num1 + num2


print(sum(1, 2))
print(sum(1, "a"))
print(sum())


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items(1, 2, 3)


def multiple_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multiple_named_items(first="hello", second="world")
