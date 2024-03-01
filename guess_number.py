import argparse
import random
import sys


def checkPlayAgain(name):
    print(f"{name} do you want to play again ? (y,n)")
    userValue = input("Enter a value: ")

    if userValue == "y":
        return True
    elif userValue == "n":
        return False
    else:
        checkPlayAgain(name)


def play(name):
    gameCount = 0
    playerWinCount = 0

    def checkInput(name):
        nonlocal gameCount
        nonlocal playerWinCount

        print(
            """
                Guess the Number I'm thinking. (1,2 or 3)
        """
        )

        userValue = input("Enter a value: ")
        userValueInt = int(userValue)

        if userValueInt not in [1, 2, 3]:
            checkInput(name)

        computeVaule = random.randint(1, 3)

        gameCount += 1

        if userValueInt == computeVaule:
            playerWinCount += 1
            print(f"game count {gameCount}")
            print(f"{name} wins {playerWinCount}")
            print(f"{name} you are correct I was thinking about number {userValueInt}")
        else:
            print(f"game count {gameCount}")
            print(f"{name} wins {playerWinCount}")
            print(f"{name} you are wrong I was thinking about number {computeVaule}")

        playAgain = checkPlayAgain(name)

        if playAgain:
            checkInput(name)
        else:
            print(f"{name} thanks for playing")
            sys.exit("Bye! 👋")

    checkInput(name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Guess my number menu.")
    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet.",
    )

    args = parser.parse_args()

    print(f"Hello {args.name}")
    play(args.name)
