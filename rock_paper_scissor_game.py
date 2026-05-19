"""
WORKFLOW OF PROJECT:
1. Input from user
2. Computer choice(Computer will choose randomly not conditionally)
3. Result Print

CASES:
A - Rock
Rock - Rock = Tie
Rock - Paper = Paper Win
Rock - Scissor = Rock Win

B - Paper
Paper - Paper = Tie
Paper - Rock = Paper win
Paper - Scissor = Scissor Win

C - Scissor
Scissor - Scissor = Tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor Win 

"""
import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor")
comp_choice = random.choice(item_list)

print(f"User Choice = {user_choice}, Computer Choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Win")
    else:
        print("Rock smashes Scissor = You Win")
    
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper, Computer Win")
    else:
        print("Paper covers rock, You Win")
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper, You Win")
    else:
        print ("Rock smashes scissor, Computer win")
    