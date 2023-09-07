#FOR LOOP

# fruits = ["apple", "mango", "banana"]

# for items in fruits:
#     print(items)

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆




#Write your code below this row 👇
seq = int(n + 1)
num = 0 
for item in student_heights:
   num += item
result = num/seq
final_result = round(result)

print(f"avrg height of students are:{final_result}")


  