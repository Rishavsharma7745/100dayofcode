#For loop / find out the maximum number 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

num = 0
for items in student_scores:
  num = items
  if num > items:
    result = num
print(num)