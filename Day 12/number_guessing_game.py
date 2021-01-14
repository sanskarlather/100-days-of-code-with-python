from number_guessing_game_logo import logo
import random
print(logo)
print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100 can you guess which one")
diff=input("Choose a difficulty type. Type 'easy' or 'hard'")
guess=1
def difficulty(diff):
    if diff=='easy':
        return 10
    else:
        return 5
num=random.randint(1,101)
def guess_func(a):
    guess=int(input("Make a guess: "))
    if guess==num:
        print(f"You got it! the answer was {guess}")
        return 0
    elif guess<num:
        print("Too low")
        return a-1
    elif guess>num:
        print("Too high")
        return a-1
def guesses():
    attempt=difficulty(diff)
    while attempt!=0:
        print(guess)
        print(f"You have {attempt} guesses left")
        attempt=guess_func(attempt)
guesses()
        

        
        