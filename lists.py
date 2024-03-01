cars = ["Up", "F40", "Fastback"]

print("Up" in cars)
print(cars.index("Up"))
print(cars[0:2])
print(cars[-3:-1])

print(len(cars))
cars.append("Jetta")
print(cars)

cars += ["Fusca", "Compass"]
print(cars)

cars.extend(["Onix", "TCROSS"])
print(cars)


cars.insert(0, "Uno")
cars.insert(1, "Celta")
print(cars)

cars[2:2] = ["Taos", "Haval"]
print(cars)

cars[1:3] = ["Puma", "GUIA"]
print(cars)

cars.remove("Onix")
print(cars)

cars.sort()
print(cars)

nums = [5, 2, 43, 8, 1]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums))
print(sorted(nums, reverse=True))

copy1 = nums.copy()
copy2 = list(nums)
copy3 = nums[:]

print(type(nums))

# Tuples are like lists but they don't change

mytuple = tuple(("Giu", 27, True))
print(mytuple)
newList = list(mytuple)  # we can convert it to a list to modify it
print(newList)
