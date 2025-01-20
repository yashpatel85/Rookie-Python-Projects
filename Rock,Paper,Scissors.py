import random

rock = """

---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

"""

paper = """

---'   ____)____
          ______)
          _______)
         _______)
---.__________)

"""

scissors = """

---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

"""

print("Lets Play Rock Paper Scissors!!!")
game_images = [rock, paper, scissors]

user_choice = int(input("What wll you choose? Enter 0 for Rock, 1 for Paper & 2 for Scissors.\n"))
print("You Chose:\n")
print(game_images[user_choice])


computers_choice = random.randint(0, 2)

print("Computer Chose: ")
print(game_images[computers_choice])

if user_choice >= 3 or user_choice < 0:
    print("Invalid Choice, Try Again!")
elif user_choice == 0 and computers_choice == 2:
    print("You Win!")
elif computers_choice == 0 and user_choice == 2:
    print("You Lose!")
elif computers_choice > user_choice:
    print("You Lose!")
elif user_choice > computers_choice:
    print("You Win!")
elif computers_choice == user_choice:
    print("It's a Draw!")






