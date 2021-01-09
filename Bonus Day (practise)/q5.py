
#sum of 2 matrix

#function to create a n*n matrix as required
def matr(n):
    
    for i in range(0,n):
        li=list(range(0,n))
        for j in range(0,n):
            li[j]=list(range(1,n+1))
    return li
#function to assign value to the n*n matrix
def matr_assign(li, n,t):
    print(f"Enter details of list number {t}")
    for a in range(0,n):
        for b in range(0,n):
            li[a][b]=int(input(f"Item at[{a},{b}]"))
    return li
#sum of n*n matrix
def add(a,b):
    li=matr(n)
    for i in range(0,n):
        for j in range(0,n):
            li[i][j]=int(li_1[i][j])+int(li_2[i][j])  
    return li

n=int(input("enter the size of square matricies\n"))
#creating matrix 1
li_1=matr(n)
#creating matrix 2
li_2=matr(n)
#assiging value to matrix 1
li_1=matr_assign(li_1,n,1)
#assiging value to matrix 2
li_2=matr_assign(li_2,n,1)
answer=add(li_1,li_2)
print(f"list 1 is={li_1}\nlist 2 is={li_2}\nsum is={answer}")
