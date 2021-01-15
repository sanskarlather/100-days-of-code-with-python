import art
import os
import random
from game_data import data
print(art.logo)

intiial_player=random.randint(0,len(data)-1)

def info_getter(a):
        return f"{data[a]['name']}, a {data[a]['description']}, from {data[a]['country']}"
score=0
looper=1
def compare(a,b):
    if data[a]['follower_count']>data[b]['follower_count']:
        return 'a'
    else:
        return 'b'
def verify(a,b):
    if a==b:
        return True
    else:
        return False
while looper!=0:
    second_player=random.randint(0,len(data)-1)
   
    print(f"Compare A:{info_getter(intiial_player)}")
    print(art.vs)
    print(f"Against B: {info_getter(second_player)}")
    larger=compare(intiial_player,second_player)
    answer=input("Who has more followers? Type 'A' or 'B': ").lower
    if verify(answer,larger):
        score+=1
        print(f"You are right current score: {score}")
    else:
        print(f"Sorry that is wrong final score: {score}")
        break
    intiial_player=second_player
    os.system("cls")
    print(art.logo)
