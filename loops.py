value = 1

# while value <= 10:
#     print(value)
#     value += 1


# while value <= 10:
#     print(value)
#     value += 1
#     break

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)


names = ["Giu", "Gabi", "Mia", "Nami"]

# for x in names:
#     print(x)

# for x in "Giuliano":
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(2, 4):
#     print(x)

for x in range(0, 100, 5):  # go from 0 to 100 incrementing 5 at a time
    print(x)

names = ["Giu", "Gabi", "Mia", "Nami"]
actions = ["Codes", "Eats", "Sleep"]

for name in names:
    for action in actions:
        print(name + " " + action)
