#day 3.

#CONDITIONAL STATEMENT IF/ELSE/elif

#finding out if the year is leap or not

# year = int(input("Enter the year: "))

# if (year % 4 == 0 and year % 100 != 0) or year %400 == 0 :
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leave year")

#pizza test

# from msilib.schema import Billboard


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")

# if size == "S" or "s":
#     bill = 15
#     if add_pepperoni == "Y" or "y":
#         bill += 2
# elif size == "M" or "m":
#     bill = 20
#     if add_pepperoni == "Y" or "y":
#         bill += 2
# elif size == "L" or "l":
#     bill = 25
#     if add_pepperoni == "Y" or "y":
#         bill +=2

# if extra_cheese == "Y" or "y":
#     bill += 3

# print(f"Your final bill is ${bill}")


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#changed the input to lower letter for our ease
name1_lower = name1.lower()
name2_lower = name2.lower()

#true count
count_t = int(name1_lower.count("t"))
count_r = int(name1_lower.count("r"))
count_u = int(name1_lower.count("u")) 
count_e = int(name1_lower.count("e"))

count_T = int(name2_lower.count("t"))
count_R = int(name2_lower.count("r"))
count_U = int(name2_lower.count("u"))
count_E = int(name2_lower.count("e"))

true_count = count_t + count_r + count_u + count_e + count_T + count_R + count_U + count_E

#Love count
count_l = int(name1_lower.count("l"))
count_o = int(name1_lower.count("o"))
count_v = int(name1_lower.count("v")) 
count_e = int(name1_lower.count("e"))

count_L = int(name2_lower.count("l"))
count_O = int(name2_lower.count("o"))
count_V = int(name2_lower.count("v"))
count_E = int(name2_lower.count("e"))

love_count = count_l + count_o + count_v + count_e + count_L + count_O + count_V + count_E


result1 = str(true_count)
result2 = str(love_count)

# print(type(result1))
# print(type(result2))

str_result = result1 + result2
final_result = int(str_result)

if final_result <= 10 or final_result >= 90 :
    print(f"Your score is {final_result}, you go together like coke and mentos.")
elif 40 <= final_result <= 50:
    print(f"Your score is {final_result}, you are alright together.")
else :
    print(f"Your score is {final_result}")
