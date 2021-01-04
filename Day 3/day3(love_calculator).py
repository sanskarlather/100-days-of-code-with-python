print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

s1=0
s2=0
name3=(name1+name2).lower()

if name3.count('t')>0 or name3.count('r') or name3.count('u')>0 or name3.count('e')>0:
  s1+=name3.count('t')+name3.count('r')+name3.count('u')+name3.count('e')
if name3.count('l')>0 or name3.count('o')>0 or name3.count('v')>0 or name3.count('e')>0:
  s2+=name3.count('l')+name3.count('o')+name3.count('v')+name3.count('e')
s3=s1*10+s2
#alternative way to combine the 2 digits
s4=int(str(s1)+str(s2))
if s3<10 or s3>90:
  print(f"Your score is {s3}, you go together like coke and mentos.")
elif s3>40 and s3<50:
  print(f"Your score is {s3}, you are alright together.")
else:
  print(f"Your score is {s3}.")

