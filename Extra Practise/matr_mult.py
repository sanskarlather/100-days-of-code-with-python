#matrix multiplication(under progress)
def create_matrix(flag):
    r=int(input("Enter the rows of matrix"))
    
    li=[[0 for i in range(0,r)] for i in range(0,r)]
            
    if flag==0:    
        return assi_matrix(li,r)
    elif flag==1:
        return li

def assi_matrix(lis,r):
    for i in range(0,r):
        for j in range(0,r):
            lis[i][j]=int(input(f"Enter{i},{j}: "))
    
    return lis
def mutli(lis,li):
    test=create_matrix(1)
    
    for i in range(0,3):
       
        for j in range(0,3):
            for k in range(0,3):
                test[i][j]+=int(lis[i][k]+li[k][j])
            
            
        
    print(test)

list_1=create_matrix(0)
list_2=create_matrix(0)

mutli(list_1,list_2)
