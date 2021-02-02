def getMinDiff(a, n, k):
        # code here
        
        arr.sort()
        dif=[]
        dif1=(a[0]+k)-(a[-1]+k)
        for (i, j) in zip(range(0,n-1), range(n-1,0,-1)):
                if (a[i]+k)-(a[j]+k)<dif1 and (a[i]+k)-(a[j]+k)>=0 :
                    dif1=(a[i]+k)-(a[j]+k)
        dif.append(dif1)
        dif2=(a[0]-k)-(a[-1]-k)
        for (i, j) in zip(range(0,n-1), range(n-1,0,-1)):
                if (a[i]-k)-(a[j]-k)<dif2 and (a[i]-k)-(a[j]-k)>=0:
                    dif2=(a[i]-k)-(a[j]-k)
        dif.append(dif2)
        dif3=(a[0]-k)-(a[-1]+k)
        for (i, j) in zip(range(0,n-1), range(n-1,0,-1)):
                if (a[i]-k)-(a[j]+k)<dif3 and (a[i]-k)-(a[j]+k)>=0:
                    dif3=(a[i]-k)-(a[j]+k)
        dif.append(dif3)
        dif4=(a[0]+k)-(a[-1]-k)
        for (i, j) in zip(range(0,n-1), range(n-1,0,-1)):
                if (a[i]+k)-(a[j]-k)<dif4 and (a[i]+k)-(a[j]-k)>=0:
                    dif4=(a[i]+k)-(a[j]-k)
        dif.append(dif4)
        dif.sort()
        return dif[-1]
arr=[2,6,3,4,7,2,10,3,2,1]
k=5
n=4
print(getMinDiff(arr, n, k))