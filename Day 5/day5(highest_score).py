student_score=input("Enter the score").split()
for i in range(0,len(student_score)):
    student_score[i]=int(student_score[i])

high=0
for j in range(0,len(student_score)):
    if student_score[j]>high:
        high=student_score[
print(f"The highest score in the class is: {high}")