
two_digit_number = input("Type a n digit number: ")

sum=0
for i in range(len(two_digit_number)):
  sum+=int(two_digit_number[i])
print(sum)