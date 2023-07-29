student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for stud in student_scores:
    s = student_scores[stud]
    if s>90:
        student_grades[stud] = "Outstanding"
    elif s>80:
        student_grades[stud] = "Exceeds Expectations"
    elif s>70:
        student_grades[stud] = "Acceptable"
    else:
        student_grades[stud] = "Fail"
        
#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇
print(student_grades)

student_scores[1] = 1
print(student_scores)