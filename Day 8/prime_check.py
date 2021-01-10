def prime_checker(number):
  num_check=2
  while num_check!=number-1:
        
        if number%num_check==0:
            flag=0
            break
        else:
            flag=1
        num_check+=1
  if flag==0:
            print("It's not a prime number.")
  else:
            print("It's a prime number.")
  


n = int(input("Check this number: "))
prime_checker(number=n)