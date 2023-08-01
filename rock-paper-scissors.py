import random

def get_choices():
    options = ['rock', 'paper', 'scissors']
    player_choice = random.choice(options)
    computer_choice = random.choice(options)
    choices = {'player': player_choice, 'computer': computer_choice}
    return choices

def check_win(player, computer, P, C):
    print(f'You chose {player}, computer chose {computer}')
    if player == computer:
        P += 1
        C += 1
        print(f"It's a tie. Player: {P} vs Computer: {C}")
    elif player == 'rock':
        if computer == 'scissors':
            P += 1
            print(f'Rock smashes scissors! You win. Player: {P} vs Computer: {C}')
        else:
            C += 1
            print(f'Paper covers rock! You lose. Player: {P} vs Computer: {C}')
    elif player == 'paper':
        if computer == 'rock':
            P += 1
            print(f'Paper covers rock! You win. Player: {P} vs Computer: {C}')
        else:
            C += 1
            print(f'Scissors cuts paper! You lose. Player: {P} vs Computer: {C}')
    elif player == 'scissors':
        if computer == 'paper':
            P += 1
            print(f'Scissors cuts paper! You win. Player: {P} vs Computer: {C}')
        else:
            C += 1
            print(f'Rock smashes Scissors! You lose. Player: {P} vs Computer: {C}')
    return P, C

def main():
    P = 0  # Initialize player's wins
    C = 0  # Initialize computer's wins
    num_rounds = 10  # Change this to the desired number of rounds for the simulation

    for _ in range(num_rounds):
        choices = get_choices()
        player_choice = choices['player']
        computer_choice = choices['computer']

        P, C = check_win(player_choice, computer_choice, P, C)

    print("Simulation finished.")

main()
