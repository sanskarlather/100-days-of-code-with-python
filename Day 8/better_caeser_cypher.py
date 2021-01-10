from caeser_cypher_logo import logo 
print(logo)
n=0

def salad(n):
	
	test=""
	if n==3:
		print("Thank You for trying this out")
	elif n==1:
		s=input("Enter the string\n")
		a=int(input("by how much\n"))
		for i in range(0,len(s)):
			if ord(s[i])+a>122:
				test+=chr(ord(s[i])+a-26)
			else:
				test+=chr(ord(s[i])+a)
			
	elif n==2:
		s=input("Enter the string\n")
		a=int(input("by how much\n"))
		
		for i in range(0,len(s)):
			if ord(s[i])-a<96:
				test+=chr(ord(s[i])-a+26)
			else:
				test+=chr(ord(s[i])-a)
	
	return(test)
while n!=3:
	n=int(input("Enter\n1. for Encoding\n2. for Decoding\n3. to quit\n"))
	
	print(salad(n))

