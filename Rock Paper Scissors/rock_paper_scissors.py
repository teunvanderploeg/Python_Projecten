import random
import time


def play():
    user = input(
        "Wat is your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    time.sleep(0.5)
    print("---3---")
    time.sleep(0.5)
    print("---2---")
    time.sleep(0.5)
    print("---1---")
    time.sleep(0.5)
    print(f"You: {user}")
    print(f"Computer: {computer}")
    time.sleep(1)

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return 'You Won!'

    print(r"""
                   ._ o o
                   \_`-)|_
                ,""       \ 
              ,"  ## |   ಠ ಠ. 
            ," ##   ,-\__    `.
          ,"       /     `--._;)
        ,"     ## /
      ,"   ##    /
                """)
    return "You los"


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
