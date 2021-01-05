import random
names_string = input("Give me everybody's names, separated by a comma. ")
#split names via comma
names = names_string.split(", ")
#print who is going to pay
print(f"{names[random.randint(0,(len(names)-1))]} is going to buy the meal today!")