import random


moves = ["r", "p", "s"]
player_input = moves + ["q"]

winning_moves = [("r", "s"), ("s", "p"), ("p", "r")]
collective_winning_move = {("r", "s"): 0, ("s", "p"): 0, ("p", "r"): 0}


def print_move(character, move):
    if move == "r":
        print("{} chose rock".format(character))
    elif move == "p":
        print("{} chose paper".format(character))
    elif move == "s":
        print("{} chose scissors".format(character))


def check_moves(player, opponent):
    if player == opponent:
        print("Draw")
        return

    if (player, opponent) in winning_moves:
        print("You wins")
        collective_winning_move[(player, opponent)] += 1
        return

    print("Opponent wins")
    collective_winning_move[(opponent, player)] += 1
    return


def get_player_move():
    while True:
        print("Enter your move: ", end="")
        player_move = input()
        if player_move in player_input:
            return player_move
        else:
            print("You entered wrong move")


def main():
    print("Welcome to Rock&Paper&Scissors")
    print("Enter r for rock")
    print("      p for paper")
    print("      s for scissor")
    print("      q to quit")

    print("Game starts: ")
    while True:
        player_move = get_player_move()

        if player_move == "q":
            print("Bye")
            return

        print_move("You", player_move)

        computer_move = random.choice(moves)
        print_move("Computer", computer_move)
        check_moves(player_move, computer_move)

        print("wining strikes: ", collective_winning_move)


random.seed()
main()
