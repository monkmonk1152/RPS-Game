import random

def play_game():
    actions = ["Rock", "Paper", "Scissors"]
    
    while True:
        computer_choice = random.choice(actions)
        player_choice = input("Enter your choice (Rock, Paper, or Scissors): ")
        
        if player_choice == "I quit":
            print("Thank you for playing!")
            break
        
        if player_choice not in actions:
            print("Invalid choice. Please try again.")
            continue
        
        print("Computer chose:", computer_choice)
        
        if player_choice == computer_choice:
            print("Game Tied")
        elif (player_choice == "Rock" and computer_choice == "Paper") or (player_choice == "Scissors" and computer_choice == "Rock") or (player_choice == "Paper" and computer_choice == "Scissors"):
            print("You lose")
        else:
            print("You win")

play_game()


