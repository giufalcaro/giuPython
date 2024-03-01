squred = lambda num: num * num

print(squred(2))

addTwo = lambda num: num + 2

print(addTwo(1))

sum = lambda a, b: a + b

print(sum(3, 2))


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(1))
print(addTwenty(1))


# higher order function (functions that returns functions) or pass into as parameters

squred = lambda num: num * num

numbers = [1, 2, 3, 4, 5, 6, 7, 71, 8]

squredNums = map(lambda num: num * num, numbers)

print(list(squredNums))

### filter

lambda num: num % 2 != 0

oddNums = filter(lambda num: num % 2 != 0, numbers)

print(list(oddNums))

from functools import reduce

lambda acc, curr: acc + curr

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)


names = ["hello", "yay", "iamabigstring"]

charCount = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(charCount)
