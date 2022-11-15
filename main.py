import random


#akármi = 10


print("""
__      ___ __  __       __      __         ___ 
/ _`|  ||__ /__`/__`||\ |/ _`   / _` /\ |\/||__  
\__>\__/|___.__/.__/|| \|\__>   \__>/~~\|  ||___ 

""")
print("Welcome to the Number guessing game!\n ")
print("I thinking of a number between 1 and 100\n ")

choose_diff = input('Choose the difficulty of the game. Type easy or hard: ')
if choose_diff == "easy":
    print('Remember! You have only 10 tipp!')
elif choose_diff == "hard":
    print('Remember! You have only 5 tipp!')
attempt_easy = 10
attempt_hard = 5
n = random.randint(1, 99)
end_of_game = True


# easy = 10 tipp max, hard = 5 tipp max
def easy_game(attempt_easy, n):
    attempt_easy = 10
    n


def hard_game(attempt_hard, n):
    attempt_hard = 5
    n


def easy_GAME():
    if choose_diff == "easy":
        attempt_easy = 10
        easy_game(attempt_easy, n)
        attempt_easy = 10
    for i in range(10):
        easy_game(attempt_easy, n)
        tipp = int(input("Make a guess: "))
        if attempt_easy == 0:
            print('You lose')
        if tipp == n:
            print("You win")
        if tipp < n:
            print('Too low')
            attempt_easy -= 1
            print(f"You have {attempt_easy} remaining to guess the number")
        if tipp > n:
            print('Too high')
            attempt_easy -= 1
            print(f"You have {attempt_easy} remaining to guess the number")
        if attempt_easy == 0:
            print('You lose')
    while tipp != n:
        attempt_easy -= 1


# hardgame
def hard_GAME():
    if choose_diff == "hard":
        attempt_hard = 5
        hard_game(attempt_hard, n)
        attempt_hard = 5
    for i in range(5):
        hard_game(attempt_hard, n)
        tipp = int(input("Make a guess: "))
        if attempt_hard == 0:
            print('You lose')
        if tipp == n:
            print("You win")
        if tipp < n:
            print('Too low')
            attempt_hard -= 1
            print(f"You have {attempt_hard} remaining to guess the number")
        if tipp > n:
            print('Too high')
            attempt_hard -= 1
            print(f"You have {attempt_hard} remaining to guess the number")
        if attempt_hard == 0:
            print('You lose')
    while tipp != n:
        attempt_hard -= 1


if choose_diff == "hard":
    hard_GAME()
if choose_diff == "easy":
    easy_GAME()