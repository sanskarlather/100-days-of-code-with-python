#Rock Paper Scissors game
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game=[rock,paper,scissors]
p_input=int(input("Enter rock(1), paper(2), scissors(3) to begin\n"))-1
c_input=random.randint(0,2)
print(c_input)
if p_input==0:
  print(rock)
elif p_input==1:
  print(paper)
elif p_input==2:
  print(scissors)
else:
  print("please enter a valid input ")

if p_input==1 or 2 or 3:
  print(game[c_input])
  if p_input==c_input:
    print("Nobody wins nobody losses its all fun and games")
  elif p_input==0 and c_input==2 or p_input==1 and c_input==0 or p_input==2 and c_input==1:
    print("Wow you beat a computer you must be happy")
  else:
    print("its not to bad i am a computer after all ")
else:
    print("sorry invalid choice ")

#Alternatively the computer's random choice could be done using the random.choice()function