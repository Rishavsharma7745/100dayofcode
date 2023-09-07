# #Randomisation - python list
# rock paper siccor game
# Randomisation -
# import random
# random_int = random.randint(10, 20)

# print(random_int)

# random_float = random.random()
# result = round(random_float, 2)
# print(result)

# random_num = random.randint(0, 1)
# if random_num == 0:
#     print("Head")
# else: 
#     print("Tails")

# #list 
# # fruit = ["cherry", "Apple", "Mango"]
# state_of_india = ["Pujab", "Delhi"]

# print(state_of_india[-1])

# names = input("Enter names separated by commas: ").split(", ")
# random_name = random.choice(names)
# print("Randomly selected name:", random_name)

# name = input("Enter the name: ").split(", ")
# count = len(name)

# if count > 0: 
#     random_index = random.randint(0, count -1)
#     random_name= name[random_index]
#     print(random_name)
# else:
#     print("no name added")

# name = input("Enter the name who will play first: ").split(", ")
# count = len(name)

# random_num = random.randint(0, count -1)
# random_name = name[random_num]

# print(random_name)
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
vertical = int(position[0])
horizontal= int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "@"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")






