#caeser cypher
period="."
st=input("Enter the string\n")
fst=''
n=input("Enter by how many digits to move")
for i in range(0,len(st)):
    if st[i]!=period and not st[i].isspace():
        
        fst+=(chr((ord(st[i])+1)))
        
    else:
        fst+=st[i]
print(fst)