# closure is a function that has access to the scope of it's parent function


def parent_function(person, coins):

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin")
        else:
            print("\n" + person + "is out of coins")

    return play_game


tommy = parent_function("tommy", 2)
abi = parent_function("abi", 3)


tommy()
abi()
tommy()
