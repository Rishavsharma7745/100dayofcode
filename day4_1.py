rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_input = input("user: ")
if user_input == "rock":
    print(rock)
elif user_input == "paper":
    print(paper)
else:
    print(scissors)

n_option = ["rock", "paper", "scissors"]
option = [rock, paper, scissors]

option_index = random.randint(0, 2)
random_n_option = n_option[option_index]
random_option = option[option_index]


print(f"Computer option is: {random_n_option} {random_option}")

if user_input == random_n_option:
    print("Its tie")
elif (user_input == "rock" and random_n_option== "scissors") or \
         (user_input == "paper" and random_n_option == "rock") or \
         (user_input == "scissors" and random_n_option == "paper"):
        print("You win!")
else:
     print("You lost")

    