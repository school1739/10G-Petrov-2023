import random

rounds = int(input("How name rounds you want to play"))
p1_score = 0
p2_score = 0

def player_turn(dice):
    result = random.randint(a:1, dice)
    return result
    print(result)

def scoring(p1, p2):
    global p1_score, p2_score
    if p1>p2:
        print("Player 1 wins")
    elif p2>p1:
        print("Player 2 wins")
    else:
        print("Friendship wins")

for player_round in range(rounds):
    player_1 = player_turn(6)
    player_2 = player_turn(6)

    scoring(player_1, player_2)
    print(f"Player 1: {p1_score}, Player 2: {player_2}")
