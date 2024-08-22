import random

# Define the options
options = ["rock", "paper", "scissors"]

# Define the illustrations
rock_illustration = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper_illustration = """
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors_illustration = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Define the function to play the game
def play_game():
    # Ask user for the best of option
    best_of = int(input("Choose best of 1, 3, or 5: "))
    if best_of not in [1, 3, 5]:
        print("Invalid input. Please choose 1, 3, or 5.")
        return

    # Initialize scores
    user_score = 0
    computer_score = 0

    # Play until there is a winner
    while user_score < (best_of+1)//2 and computer_score < (best_of+1)//2:
        # Get the user's choice
        user_choice = input("Choose rock, paper, or scissors: ")
        user_choice_index = options.index(user_choice)

        # Get the computer's choice
        computer_choice_index = random.randint(0, 2)

        # Print the illustrations
        print("Your choice:")
        if user_choice == "rock":
            print(rock_illustration)
        elif user_choice == "paper":
            print(paper_illustration)
        else:
            print(scissors_illustration)

        print("Computer's choice:")
        if options[computer_choice_index] == "rock":
            print(rock_illustration)
        elif options[computer_choice_index] == "paper":
            print(paper_illustration)
        else:
            print(scissors_illustration)

        # Determine the winner
        if user_choice_index == computer_choice_index:
            print("It's a tie!")
        elif (user_choice_index == 0 and computer_choice_index == 2) or \
             (user_choice_index == 1 and computer_choice_index == 0) or \
             (user_choice_index == 2 and computer_choice_index == 1):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        # Print the current score
        print(f"Current score: You {user_score}, Computer {computer_score}")

    # Declare the winner
    if user_score > computer_score:
        print("Congratulations! You won!")
    else:
        print("Sorry, the computer won.")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (Y/N)").lower()
    if play_again == "y":
        play_game()

# Play the game
play_game()
