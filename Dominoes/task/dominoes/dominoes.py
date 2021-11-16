# Write your code here
import random


def create_domino_set():
    full_domino = []
    for i in range(0,7):
        for j in range(i, 7):
            current_piece = [i, j]
            full_domino.append(current_piece)
    return full_domino


def stockpieces(full_domino_set):
    result = []
    fullset = full_domino_set
    random.seed()
    while len(result) < 14:
        rand = random.randint(0, len(fullset)-1)
        piece = fullset.pop(rand)
        result.append(piece)
    return result


def create_player_pieces(fullset):
    result = []
    # fullset = full_domino_set
    random.seed()
    while len(result) < 7:
        rand = random.randint(0, len(fullset)-1)
        piece = fullset.pop(rand)
        result.append(piece)
    return result


def draw_screen(stock, cp, pp, snk, player_turn):
    print("="*70)
    print("Stock size: {}".format(len(stock)))
    print("Computer pieces: {}".format(len(cp)))


    if player_turn:
        # print("Status: player")
        print()
        print("{}".format(" ".join([str(x) for x in snk])))
        print()
        print("Your pieces:")
        for i in range(0, len(pp)):
            print("{}:{}".format(i+1, pp[i]))
        print("\nStatus: It's your turn to make a move. Enter your command.")
    else:
        print()
        print("{}".format(" ".join([str(x) for x in snk])))
        print()
        print("Your pieces:")
        for i in range(0, len(pp)):
            print("{}:{}".format(i+1, pp[i]))
        print("\nStatus: Computer is about to make a move. Press Enter to continue...")
    # print("Your pieces: {}".format(pp))


is_players_turn = False
domino_sneak = []
while len(domino_sneak) == 0:
    full_domino_set = create_domino_set()
    computer_pieces = create_player_pieces(full_domino_set)
    player_pieces = create_player_pieces(full_domino_set)
    stock_pieces = stockpieces(full_domino_set)

    if [6, 6] in player_pieces:
        i = player_pieces.index([6, 6])
        current_piece = player_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = False
    elif [6, 6] in computer_pieces:
        i = computer_pieces.index([6, 6])
        current_piece = computer_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = True
    elif [5, 5] in player_pieces:
        i = player_pieces.index([5, 5])
        current_piece = player_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = False
    elif [5, 5] in computer_pieces:
        i = computer_pieces.index([5, 5])
        current_piece = computer_pieces.pop(i)
        domino_sneak.append(current_piece)
        is_players_turn = True

# print("Stock pieces: {}".format(stock_pieces))
# print("Computer pieces: {}".format(computer_pieces))
# print("Player pieces: {}".format(player_pieces))
# print("Domino snake: {}".format(domino_sneak))
# if is_players_turn:
#   print("Status: player")
# else:
#    print("Status: computer")

draw_screen(stock_pieces,computer_pieces,player_pieces,domino_sneak,is_players_turn)



