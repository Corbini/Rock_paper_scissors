import random

status = {('win', 1), ('lose', 2), ('tie', 3)}


def print_move(character, move):
    if move == "r":
        print("{} chose rock".format(character))
    elif move == "p":
        print("{} chose paper".format(character))
    elif move == "s":
        print("{} chose scissors".format(character))


def player_wins(player, computer):

    if player == computer:
        print("Tie")
        return status['tie']

    if player == "s" and computer == "r":

        print("Computer wins")
        return status['lose']

    if player == "r" and computer == "p":
        print("Computer wins")
        return status['lose']

    if player == "p" and computer == "s":
        print("Computer wins")
        return status['lose']

    print("You wins")
    return status['win']


def main():

    collective_data = [("rs", 0), ("sp", 0), ("pr", 0)]

    #win_moves = ["rs", "sp", "pr"]
    #print("rs" in win_moves)

    print("Welcome to Rock&Paper&Scissors")
    print("Enter r for rock")
    print("      p for paper")
    print("      s for scissor")
    print("      q to quit")

    moves = ["rock", "paper", "scissor", "quit"]
    player_input = ["r", "p", "s", "q"]

    print("Games starts: ")
    while True:

        while True:
            print("Enter your move: ", end="")
            player_move = input()
            if player_input.count(player_move) != 0:
                break
            else:
                print("You didn't entered any move")

        if player_move == "q":
            print("Bye")
            return

        print_move("You", player_move)

        computer_move = random.choice(player_input)
        print_move("Computer", computer_move)
        player_wins(player_move, computer_move)



random.seed()
main()
