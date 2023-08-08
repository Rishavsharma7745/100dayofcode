#DAY2
#Data types, Numbers, operations, Type conversion, f-strings
# Project - TIP Calculator

# DATA TYPES - Primitive Data types 
#string
# print("Hello"[4]) #subscripting

#INTEGER
# print(123+345)

#FLOAT
# print(3.2+2.3)

#BOOLEAN
#YES OR NO

#FUNCTIONS 
#DATA TYPE CONVERSTION OR TYPE CASTING

# num = len(input("Enter your name "))
# num_new = str(num) #converted int to str
# print("Your name contains " + num_new + " words")

# num = input("enter a decimal number ")
# num_new = str(num)
# print("The number is " + num_new)

# two_digit_number = input("Type a two digit number: ")
# num_a = int(two_digit_number[0])
# num_b = int(two_digit_number[1])
# print(num_a+num_b)

#NUMBERS    
# 7+2
# 7-2
# 6*2
# 6/2
# 2**2

#priority of numbers
# #PEMDAS
# PARAENTHESES    ()
# EXPONENTS       **       
# MULTIPLICATION  *
# DIVSION         /       
# ADDITION        +
# SUBTRACTION     -     

# print(3 * 3 + 3 / 3 - 3) 

# print(round(9/4))
# print(type(8 // 3))
# print(type(8 / 3))


#tip calculation accoorid to the percentage
print("WELCOME TO THE TIP CALCULATOR")
bill = input("Enter the bill amount: ")
people =input("In how many people you want to split: ")
percent = input("How much percent tip you want ot give 12/13/15: ")

people_a = float(people)
per = float(percent)
bill_a = float(bill)

tip_percent = (per / 100)
 
tip_result = (bill_a / people_a) * tip_percent
round_tip_result = round(tip_result, 2)
final_amount = tip_result + bill_a

print(f"Per person need to pay {round_tip_result} and the total bill including tip is ${final_amount}")