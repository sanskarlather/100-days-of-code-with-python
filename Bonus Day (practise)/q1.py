#Sum of integer Range

def add_it_up(n):
    sum=0
    if not n.is_integer():
        return 0
    else:
        j=int(n)
        for i in range(1,j+1):
           sum+=i 
        print(sum)
    
a=float(input("Enter how many integers you want to add"))
add_it_up(a)
