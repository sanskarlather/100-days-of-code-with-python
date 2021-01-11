import os
from silent_auction_logo import logo

print(logo)
cont="yes"
bids={}
os.system('cls')
while cont!="no":
    
    name=input("What is your name?: ")
    bid=int(input("What is your bid?: "))
    cont=input("Are there any other bidder? Type 'yes' or 'no'\n")
    
    bids[name]=bid
max=0
win=""
for i in bids:
    if bids[i]>max:
        max=bids[i]
        win=i

print(win)

