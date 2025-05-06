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

answer_choice = [rock, paper, scissors]
user_input = input("Your turn\nType: rock, paper, or scissors\n").lower()

# Validate input
if user_input not in ["rock", "paper", "scissors"]:
    print("Invalid input. Please choose rock, paper, or scissors.")
else:
    # Assign visuals
    if user_input == "rock":
        user_answer = rock
    elif user_input == "paper":
        user_answer = paper
    else:
        user_answer = scissors

    computer_choice = random.randint(0, 2)
    computer_answer = answer_choice[computer_choice]

    print(f"\nYou chose:\n{user_answer}")
    print(f"Computer chose:\n{computer_answer}")

    # Determine winner
    if user_answer == computer_answer:
        print("It's a draw!")
    elif (user_answer == rock and computer_answer == scissors) or \
         (user_answer == paper and computer_answer == rock) or \
         (user_answer == scissors and computer_answer == paper):
        print("You win!")
    else:
        print("You lose.")
