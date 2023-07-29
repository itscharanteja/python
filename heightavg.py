# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sums = 0
for student in student_heights:
    sums += student
print(sums)
num=0
for l in student_heights:
    num += 1
print(l)
avg = round(sums/num)
print(avg)