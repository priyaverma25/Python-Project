# """
# WORKFLOW OF PROJECT:
# 1- input from user(Snake, Water, Gun)
# 2- Computer choice(Computer will choose randomly not conditionally)
# 3- Result printRock

# Cases:
# A- Snake
# Snake - Snake = tie 
# Snake - Water = Snake win
# Snake - Gun = Gun win

# B- Water
# Water - Water = tie
# Water - Snake = Snake win
# Water - Gun = Water win

# C- Gun
# Gun - Gun = tie
# Gun - Snake = Snake
# Gun - Water = Water win

# """

import random
item_list = ["Snake", "Water", "Gun"]

while True:
    user_choice = input("Enter your move = Snake, Water, Gun: ").capitalize()
    computer_choice = random.choice(item_list)

    print(f"User choice = {user_choice}, Computer choice = {computer_choice}")

    if user_choice == computer_choice:
     print("Both chooses same: = Match Tie")
    
    elif user_choice == "Water":
        if computer_choice == "Snake":
            print("Computer wins")
        else:
            print("You win")
    
    elif user_choice == "Gun":
        if computer_choice == "Water":
            print("Computer wins")
        else:
            print("You win")
        
    elif user_choice == "Snake":
        if computer_choice == "Gun":
            
            print("Computer wins")
        else:
            print("You win")  
        

    # Game code

    play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break                
    
    
    
    
    