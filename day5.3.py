# #FOr loop with range 
# num_2 = 0 #intiliaze a number
# for num in range(1, 101):
#     if num % 2 == 0:
#         num_2 += num
# print(num_2)

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
##################################################
random_letters = random.sample(letters, nr_letters)
let_password = ""
for letters in random_letters:
    let_password += letters
##################################################
random_number = random.sample(numbers, nr_numbers)
num_password = ""
for numbers in random_number:
    num_password += numbers
##################################################
random_symbols = random.sample(symbols, nr_symbols)
sys_password = ""
for symbols in random_symbols:
    sys_password += symbols

fake_result = (f"{let_password}{num_password}{sys_password}")

mylist = [let_password, num_password, sys_password]
result = random.shuffle(mylist)
print(fake_result)
print(result) 