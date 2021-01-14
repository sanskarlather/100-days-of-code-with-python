#Determinant Of a NxN Matrix
def det_three(a):
    
    if len(a)==2:
        return ((a[0][0]*a[1][1]-a[1][0]*a[0][1]))
    b=[[[0 for i in range(0,len(a))] for j in range(0,len(a))]for i in range(0,len(a))]   
    c=[]
    for i in range(0,len(a)):
        for j in range(0,len(a)):
            for k in range(0,len(a)):
                if k!=0 and j!=i:
                    b[i][k][j]=int(a[k][j])
                if k==0 and j==i:
                    c.append(a[k][j]) 
    for i in range(0,len(a)):
        b[i].remove([0 for f in range(0,len(a))])
       
        for j in range(0,len(a)-1):
            b[i][j].remove(0)
    det=0
    fl=1
    for i in range(0,len(a)):
        det+=c[i]*det_three(b[i])*fl
        fl*=-1
    return det
n=int(input("What is the size of the matrix whose determinant you want to find\n"))
a=[[0 for i in range(0,n)] for j in range(0,n)]
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=int(input(f"Enter {i},{j}: "))
print("The Entred Matrix is:")
for i in range(0,n):
    print(a[i])
print(f"The Determinent is: {det_three(a)}")
                