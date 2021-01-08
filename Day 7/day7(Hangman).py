import random
import os
from hangman_art import stages, logo
from hangman_word import wordlist
print(logo)
hangman_test=random.choice(wordlist)
s=5
guess=[]
lives=6
l_count=0
#creating a list with blanks
for i in range(0,len(hangman_test)):
    guess+="_"

while lives!=0:
    
    #Empty string for printing the list as a string
    st=''
    #varibale to check is the guess was correct
    found=0 
    p_in=input("Enter word\n")
    os.system('cls')
    #if user enter words twice
    if p_in in guess:
        print(f"you already gussed {p_in}")
    else:
        for i in range(0,len(hangman_test)):
                if hangman_test[i]==p_in:
                    guess[i]=p_in
                    l_count+=1
                    found=1
        #if letter is not found in the list the flag found is checked and the lives are reduced can also be done using the condition (if p_in not in guess)            
        if found==0:
            lives-=1
            print(stages[s])
            s-=1
            if lives==0:
                print(f"You Loose the word was'{hangman_test}'")
        #to convert list to string
        for i in range(0,len(hangman_test)):
            st+=guess[i]+" " 
        print(st)   
        if l_count==len(hangman_test):
           print("You win")
           lives=0


