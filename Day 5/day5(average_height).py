#average height
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sums=0
lens=0
for i in student_heights:
  sums+=i
  lens+=1
  
print(round(sums/lens))