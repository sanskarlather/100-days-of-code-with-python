from menu import MENU, resources
money=0
def money_ded(choice):
    quarters=float(input("How Many Quarters?: "))
    dimes=float(input("How Many Dimes?: "))
    nickels=float(input("How Many Nickles?: "))
    pennies=float(input("How Many Pennies?: "))
    total=.25*quarters+.10*dimes+.005*nickels+0.01*pennies
    print(total)
    if MENU[choice]["cost"]<total:
        chnage=round((total-MENU[choice]['cost']),2)
        print(f"Here is ${chnage} in change")
        return MENU[choice]['cost']
    elif MENU[choice]["cost"]>total:
        print("Sorry not enough money you amount is refunded")
        return 0
    
def resource_ded(choice):
    dough=0
    for i in resources:
        if resources[i]<MENU[choice]['ingredients'][i]:
            print (f"Sorry Not Enough {i}")
            return dough
            
        else:
            dough=money_ded(choice)
            if dough!=0:
                for i in resources:
                    resources[i]-=MENU[choice]['ingredients'][i]
        print(f"Here is your {choice}. Enjoy!")
        return dough
choice=input("What would you like? (espresso/latte/cappuccino):")
while choice!="off":
    
    if choice=="report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"Money: {money}")
    elif choice=="espresso":
        
        money+=resource_ded(choice)
    elif choice=="cappuccino":
        
        money+=resource_ded(choice)
    elif choice=="latte":
        
        money+=resource_ded(choice)
    choice=input("What would you like? (esspresso/latte/cappuccino):")