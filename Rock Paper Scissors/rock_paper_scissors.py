import random
import time
import os


def clear(): return os.system('cls')


def play():
    user = input(
        "Wat is your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user == "r" or user == "p" or user == "s":
        time.sleep(0)
    else:
      print("That was not a option")
      time.sleep(2)
      clear()
      print(play())
  

    time.sleep(0.5)
    print("---3---")
    time.sleep(0.5)
    print("---2---")
    time.sleep(0.5)
    print("---1---")
    time.sleep(0.5)


    if user == "r":
      print(f"You: Rock")

    if user == "p":
      print(f"You: Paper")

    if user == "s":
      print(f"You: Scissors")


    if computer == "r":
      print("Computer: Rock")
      time.sleep(1)

    if computer == "p":
      print("Computer: Paper")
      time.sleep(1)

    if computer == "s":
      print("Computer: Scissors")
      time.sleep(1)


    if user == computer:
        print("It's a tie")
        time.sleep(2)
        return ("")

    if is_win(user, computer):
        print("You Won!")
        time.sleep(2)
        return ("")

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
    print("You lose") 
    time.sleep(2)
    return ("")


def is_win(player, opponent):
    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


clear()
print(play())

