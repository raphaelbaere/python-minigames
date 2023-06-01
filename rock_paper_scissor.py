import random;

def get_choices():
    player_choice = input("Choose (rock, paper, scissor)")
    possibleChoices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(possibleChoices)
    print(f"You chose {player_choice}, computer chose {computer_choice}")

    return { "player": player_choice, "computer": computer_choice }

def check_win(player, computer):
    if (player == computer):
        return "It's a tie"
    elif (player == "rock"):
        if (computer == "scissor"):
            return "Rock smashes scissor! You win!"
        else:
            return "Paper envolves rock! You lose!"
    elif (player == "paper"):
        if (computer == "rock"):
            return "Paper envolves rock! You win!"
        else:
            return "Scissor cut paper! You lose!"
    elif (player == "scissor"):
        if (computer == "paper"):
            return "Scissor cut paper! You win!"
        else:
            return "Rock smashes scissor! You lose!"
        

choice = get_choices()

result = check_win(choice["player"], choice["computer"])

print(result)