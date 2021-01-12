from calc_logo import logo

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mult(n1,n2):
    return n1*n2
def divi(n1,n2):
    return n1/n2

out=0

opt={
    "+":add,
    "-":sub,
    "*":mult,
    "/":divi

    }


def calcu():
    print(logo)
    flag=1
    number_1=int(input("Enter the first number: "))
       
    while flag!=0:
          operation=input("Enter Operation \n'+'\n'-'\n'*'\n'/'\n")   
          number_2=int(input("Enter the next number: "))
          funct=opt[operation]
          out=funct(number_1,number_2)
          
          flag=int(input(f"Continue with {out}? Yes:1 or No:0 :"))
          if flag==0:
                calcu()
          else:
              number_1=out
  

       
           


calcu()
