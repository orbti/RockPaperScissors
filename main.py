import random
from enum import IntEnum


class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


victories = {
    Action.Rock: [Action.Scissors, Action.Lizard],
    Action.Paper: [Action.Rock, Action.Spock],
    Action.Scissors: [Action.Paper, Action.Lizard],
    Action.Lizard: [Action.Paper, Action.Spock],
    Action.Spock: [Action.Rock, Action.Scissors],
}


def get_games_played():
    games = int(input("How many rounds to win? "))
    return games


def get_user_action():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"\nEnter value {choices_str}: "))
    action = Action(selection)
    return action


def get_computer_action():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    defeats = victories[user_action]

    if user_action == computer_action:
        print(f"You both chose {user_action.name}! It's a tie!")
        score["ties"] += 1
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
        score["wins"] += 1
    else:
        print(f"{computer_action.name} beats {user_action.name}! You loose.")
        score["losses"] += 1


def main():
    score = dict(ties=0, wins=0, losses=0)
    try:
        game_count = get_games_played()
    except ValueError as e:
        print("Invalid input. Enter an integer.")
        continue

    while game_count > (score["wins"] or score["losses"]):
        try:
            user_action = get_user_action()
        except ValueError as e:
            range_str = f"[0, {len(Action) - 1}]"
            print(f"Invalid input. Enter an integer in range {range_str}")
            continue

        computer_action = get_computer_action()
        print(f"\nYou chose {user_action.name}. Computer chose {computer_action.name}.")
        determine_winner(user_action, computer_action)

    print(f"\n\tFinal Score")
    print(
        f"\n\tTies: {score['ties']} Wins: {score['wins']} Losses: {score['losses']}\n"
    )

    play_again = input("Play again (y/n): ")
    if play_again != "y":
        break
if __main__ == '__name__':
    main()
