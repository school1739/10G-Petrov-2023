def player_turn(dice):
    return random.randint(a:1, dice)

def scoring(p1, p2):
    if p1 > p2:
        print('player 1')
        p1_score += 1
    if p1 < p2:
        print('player 2')
        p2_score += 1
    else:
        print('')


p1_score = 0
p2_score = 0

player_1 = player_turn(6)
player_2 = player_turn(6)

scoring(player_1, player_2)
print(f'player_1: {p1_score} player_2: {p2_score}')
