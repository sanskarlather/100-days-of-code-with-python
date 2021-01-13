from blackjack_logo import logo
import random

def current_score(card):
    if sum(card)==21 and len(card)==2:
        return 0
          
    if 11 in card and sum(card)>21:
        card.remove(11)
        card.append(1)
    return sum(card)

def draw_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card_pick=random.choice(cards)
    return card_pick

def pick_winner(computer_cards,player_cards):
    if current_score(computer_cards)==current_score(player_cards):
        return "Draw 🙃"
    elif current_score(player_cards)==0:
         return "Win with a Blackjack 😎"
    elif current_score(player_cards)<=21 and current_score(player_cards)>current_score(computer_cards):
          return "You win 😃" 
    elif current_score(computer_cards)<=21 and current_score(computer_cards)>current_score(player_cards):
        return "Lose, opponent has Blackjack 😱"
    elif current_score(player_cards)>21:
         return  "You went over. You lose 😭"


        


def game_play(start):
    while start=='y':
        
        print(logo)
        
        player_cards=[]
        computer_cards=[]
       
    
        for i in range(0,2):
            player_cards.append(draw_cards())
    
        computer_cards.append(draw_cards())
        comp_sum=current_score(computer_cards)
    
        while comp_sum<17:
            computer_cards.append(draw_cards())
            comp_sum=int(current_score(computer_cards))
    
        print(f" Your current cards are: {player_cards} and the current score is {current_score(player_cards)}")
        if current_score(player_cards)==0:
               print(f"You win final cards were: {player_cards} and score was {current_score(player_cards)}, The computer cards were: {computer_cards} and score was {current_score(computer_cards)}")
               flag=0
               break
        print(f"Computer first card is {computer_cards[0]}")
        cho=input("Type 'y' to get another card and 'n' to pass: ")

        flag=1
        if cho=='y':
            while cho=='y':
            
                if current_score(player_cards)==21:
                    print(f" You win the final cards were: {player_cards} and score was {current_score(player_cards)}, The computer cards were: {computer_cards} and score was {current_score(computer_cards)}")
                    flag=0
                player_cards.append(draw_cards())
                print(f" Your current cards are: {player_cards} and the current score is {current_score(player_cards)}")
                print(f"Computer first card is {computer_cards[0]}")
                if current_score(player_cards)>21:
                    print(f" You Loose the final cards were: {player_cards} and score was {current_score(player_cards)}, The computer cards were: {computer_cards} and score was {current_score(computer_cards)}")
                    flag=0
                    break
                cho=input("Type 'y' to get another card and 'n' to pass: ")
    
            if flag==1:    
                if current_score(player_cards)>current_score(computer_cards) or current_score(computer_cards)>21:
                    print(f" You win the final cards were: {player_cards} and score was {current_score(player_cards)}, The computer cards were: {computer_cards} and score was {current_score(computer_cards)}")

        else:
            print(f"{pick_winner(computer_cards,player_cards)}")
        start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
        continue
        start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
start=input("Do you want to play a game of Blackjack? Type 'y' or 'n': " )
game_play(start)

