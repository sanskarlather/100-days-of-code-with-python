#Tip Calculator

print("Welcome to the tip calculator")
bill=float (input("what is the total bill\n$"))
people=float(input("How many people to split the bill?\n"))
percentage=float (input("what percentage tip would you like to give\n"))
tip=str(round((bill+(bill*(percentage/100)))/people,2))
tipf=round(((bill+(bill*(percentage/100)))/people),2)
print("each person should pay $"+tip)
#alternative using f-string instead of typecasting
print(f"each should pay ${tipf}")



