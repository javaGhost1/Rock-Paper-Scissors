from random import choice

possibilities = ['rock', 'paper', 'scissors']

def make_play(possibilities):
    my_choice = choice(possibilities).lower()

    return my_choice


def check_choice(played, ai_choice):
    if ai_choice != played:
        while played == 'rock':
            if ai_choice != 'paper':
                print("You win")
            else:
                print("I win")
            break
        while played == 'paper':
            if ai_choice != 'scissors':
                print("You win")
            else:
                print("I win")
            break
        while played == 'scissors':
            if ai_choice != 'rock':
                print("you win")
            else:
                print("I win")
            break
    else:
        print('Draw')

print("Hello whats Your name?")
name = input()

print(f"Okay! {name.title()} Let us play a game\n rock paper or scissors")
played = input().lower()

ai_choice = make_play(possibilities)

while played in possibilities:
    print(f"I choose {ai_choice}")
    check_choice(played, ai_choice) 
    break