import argparse

import guess_number
import rps

parser = argparse.ArgumentParser(description="Guess my number menu.")

parser.add_argument(
    "-n",
    "--name",
    metavar="name",
    required=True,
    help="The name of the player.",
)

parser.add_argument(
    "-g",
    "--game",
    metavar="language",
    required=True,
    choices=["rps", "guessNumber"],
    help="The game you want to play.",
)

args = parser.parse_args()

if args.game == "rps":
    play = rps.rps(args.name)
    play()
elif args.game == "guessNumber":
    guess_number.play(args.name)
