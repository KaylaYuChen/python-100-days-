import random

# ASCII art for Rock, Paper, Scissors
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

game_images = [rock, paper, scissors]

# Player choice
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: \n"))
if 0 <= user_choice <= 2:
    print(game_images[user_choice])
else:
    print("You typed an invalid number. You lose!")

# Bunny's choice (computer)
bunny_choice = random.randint(0, 2)
print("Your bunny chose:")
print(game_images[bunny_choice])

# Determine winner
if user_choice == bunny_choice:
    print("It's a draw!")
elif (user_choice == 0 and bunny_choice == 2) or \
     (user_choice == 1 and bunny_choice == 0) or \
     (user_choice == 2 and bunny_choice == 1):
    print("You win!")
elif 0 <= user_choice <= 2:
    print("You lose!")
