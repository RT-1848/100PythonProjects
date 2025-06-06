import random

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
choices = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
pc_choice = random.randint(0,2)
print(f"You Chose: {choices[user_choice]} \n")
print(f"Computer Chose: {choices[pc_choice]}")

if (user_choice > 2 or user_choice < 0):
    print("Invalid Choice... Exiting")
elif (user_choice == pc_choice):
    print("It was a Tie!!")
elif (user_choice == 0 and pc_choice == 1):
    print("You Lose!!")
elif (user_choice == 0 and pc_choice == 2):
    print("You Win!!")
elif (user_choice == 1 and pc_choice == 0):
    print("You Win!!")
elif (user_choice == 1 and pc_choice == 2):
    print("You Lose!!")
elif (user_choice == 2 and pc_choice == 0):
    print("You Win!!")
elif (user_choice == 2 and pc_choice == 1):
    print("You Lose!!")



