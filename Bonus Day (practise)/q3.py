#python program to interchange first and last element
li=[]
n=int(input("How many elements you want to add"))
print("Enter the elements you want in the lists")
for i in range(0,n):
    li+=str(input())
temp=li[0]
li[0]=li[n-1]
li[n-1]=temp
print(li)