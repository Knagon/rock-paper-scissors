import  random

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

moves = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

rand_computer_move = random.randint(0,2)

numbers = [0,1,2]

if choice not in numbers:
    print("You typed an invalid number!")
else:
    print(f"\nYou chose:\n{moves[choice]}")
    print(f"Computer chose:\n{moves[rand_computer_move]}")

    if choice == rand_computer_move:
        print("it's a draw")
    elif choice == 0 and rand_computer_move == 2:
        print("You have won!")
    elif choice == 1 and rand_computer_move == 0:
        print("You have won!")
    elif choice == 2 and rand_computer_move == 1:
        print("You have won!")
    elif choice == 2 and rand_computer_move == 0:
        print("You lose :(. Computer wins.")
    elif rand_computer_move > choice:
        print("You lose :(. Computer wins.")
