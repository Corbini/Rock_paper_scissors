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
        return False

    winning_move = ["rs", "sp", "pr"]
    if player + computer in winning_move:
        print("You wins")
        return True

    print("Computer wins")
    return False


def main():



    collective_data = [("rs", 0), ("sp", 0), ("pr", 0)]

    print("Welcome to Rock&Paper&Scissors")
    print("Enter r for rock")
    print("      p for paper")
    print("      s for scissor")
    print("      q to quit")

    moves = ["r", "p", "s"]
    player_input = moves + ["q"]

    print("Games starts: ")
    while True:

        while True:
            print("Enter your move: ", end="")
            player_move = input()
            if player_move in player_input:
                break
            else:
                print("You didn't entered any move")

        if player_move == "q":
            print("Bye")
            return

        print_move("You", player_move)

        computer_move = random.choice(player_input)
        print_move("Computer", computer_move)
        if player_wins(player_move, computer_move):
            pass
            #print(collective_data[player_move+computer_move])


random.seed()
main()
