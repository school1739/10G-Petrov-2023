import random


def player_turn(dice):
    result = random.randint(1, dice)
    print(f"Player rolled a {result}")
    return result


def scoring(p1, p2):
    global p1_score, p2_score
    if p1 > p2:
        print("Player 1 wins!")
        p1_score += 1
    elif p1 < p2:
        print("Player 2 wins!")
        p2_score += 1
    else:
        print("Draw!")


p1_score = 0
p2_score = 0

rounds = int(input("How many rounds would you like to play? "))

for play_round in range(rounds):
    player_1 = player_turn(6)
    player_2 = player_turn(6)

    scoring(player_1, player_2)
    print(f"Score: Player 1: {p1_score} vs. Player 2: {p2_score}")
