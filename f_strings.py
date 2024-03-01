person = "giu"
coins = 4
print("\n" + person + " has " + str(coins) + " coins")

message = "\n%s has %s coins" % (person, coins)
print(message)

message = "\n{} has {} coins".format(person, coins)

print(message)


message = "\n{person} has {coins} coins".format(person=person, coins=coins)

print(message)


player = {"person": person, "coins": coins}

message = "\n{person} has {coins} coins".format(**player)

print(message)

message = f"\n{person} has {coins} coins"
print(message)

message = f"\n{person} has {coins * 5} coins"
print(message)

message = f"\n{player['person']} has {coins * 5} coins"
print(message)

# you can pass options
num = 10
print(f"\n 2.2 times {num} is {2.25 *num:.2f}")
