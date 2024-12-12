import random
import game_data

# DECLARING VARIABLES FOR THE GAME DATA, SCORE AND GAME(to be used in the while loop)
database = game_data.data
score = 0
game = True

b = database[random.randint(0,49)]

while game:
    a = b
    b = database[random.randint(0, 49)]
    while a == b:
        b = database[random.randint(0, 49)]

    more_follower_count = 0
    if a['follower_count'] > b['follower_count']:
        more_follower_count = 'a'
    elif b['follower_count'] > a['follower_count']:
        more_follower_count = 'b'

    print(
        f"\nCurrent score: {score}\n"
        "\nCompare A:"
        f"\n{a['name']}, a/an {a['description']}, from {a['country']}"
        "\nAnd B"
        f"\n{b['name']}, a/an {b['description']}, from {b['country']}"
    )
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_choice == more_follower_count:
        score+=1
    else:
        print(f"\nGAME OVER\nYour final score is {score}")
        game = False
