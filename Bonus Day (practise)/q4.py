#create a n*n matrix
n=int(input('what should be the dimensions of the matrix'))
for i in range(0,n):
    test=list(range(0,n))

    for j in range(0,n):
        test[j]=list(range(1,n+1))
    print(test[i])

