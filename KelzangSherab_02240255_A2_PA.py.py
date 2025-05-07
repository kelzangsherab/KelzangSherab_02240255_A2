import random

class GuessNumberGame:
    def __init__(self):
        self.number_to_guess = random.randint(1, 10) 
        self.attempts = 0

    def play(self):
        print("Welcome to the Guessing Game! Guess any numbers (1-10).")
        while True:
            try:
                guess = int(input("Enter any number: "))
                self.attempts += 1
                if guess < self.number_to_guess:
                    print("Bit low")
                elif guess > self.number_to_guess:
                    print("Bit high")
                else:
                    print(f"Congrats! You have guess number  {self.number_to_guess} in {self.attempts} tries.")
                    return max(0, 10 - self.attempts)
            except ValueError:
                print("Please enter a number in given range.")

class RockPaperScissors:
    def play(self):
        choices = ["rock", "paper", "scissors"]
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Have another go.")
            return
        bot_choice = random.choice(choices)
        print(f"Bot: {bot_choice}")
        if user_choice == bot_choice:
            print("Draw")
        elif (user_choice == 'rock' and bot_choice == 'scissors') or \
             (user_choice == 'paper' and bot_choice == 'rock') or \
             (user_choice == 'scissors' and bot_choice == 'paper'):
            print("You won!")
        else:
            print("You lose!")

class TriviaQuiz:
    def __init__(self):
        self.question = {
            "What is the capital city of Bhutan?": ["a) Trongsa", "b) Punakha", "c) Thimphu", "d) Gelephu", 'c'],
            "What is 9 + 18?": ["a) 30", "b) 41", "c) 29", "d) 27", 'd'],
            "How many days are there in a year?": ["a) 366", "b) 365", "c) 367", "d) 368", 'b']
        }

    def play(self):
        score = 0
        for question, options in self.question.items():
            print(question)
            for option in options[:-1]:
                print(option)
            answer = input('Your answer (a/b/c/d): ').lower()
            if answer == options[-1]:
                print("Well Done!")
                score += 1
            else:
                print("Sorry.")
        print(f"Your score: {score}/{len(self.questions)}")

class PokemonCardManager:
    def __init__(self):
        self.cards = []

    def manage(self):
        while True:
            action = input("Would you like to add a card (s), view all cards (c), or exit (o)? ").lower()
            if action == 's':
                name = input("Enter the Pokemon names: ")
                type_ = input("Enter the Pokemon types: ")
                self.cards.append({'name': name, 'type': type_})
                print(f"Card for {name} added.")
            elif action == 'c':
                if self.cards:
                    print("Your Pokémon Cards:")
                    for card in self.cards:
                        print(f"{card['name']} - Type: {card['type']}")
                else:
                    print("There's no cards in your binder.")
            elif action == 'o':
                break
            else:
                print("Invalid option.")

class OverallScoringSystem:
    def __init__(self):
        self.total_score = 0

    def manage(self):
        while True:
            score = input("Enter the score for this round (or type 'exit' to finish): ")
            if score.lower() == 'exit':
                break
            try:
                self.total_score += int(score)
            except ValueError:
                print("Please enter a valid number.")
        print(f"Your total score is: {self.total_score}")

class MainMenu:
    def __init__(self):
        self.games = {
            '1': GuessNumberGame(),
            '2': RockPaperScissors(),
            '3': TriviaQuiz(),
            '4': PokemonCardManager(),
            '5': OverallScoringSystem()
        }

    def display_menu(self):
        while True:
            print('\nMenu:')
            print('1/ Guess Number Game')
            print('2/ Rock Paper Scissors')
            print('3/ Trivia Quiz')
            print('4/ Pokémon Card Binder Manager')
            print('5/ Overall Scoring System')
            print('6/ Exit')
            
            choice = input("choose a Game (1-6): ")
            if choice == '1':
                score = self.games[choice].play()
                print(f"Your score for Guessing Game: {score}")
            elif choice in self.games:
                self.games[choice].play() if choice != '4' else self.games[choice].manage()
            elif choice == '6':
                print("Exiting the program. Come Back Stronger!")
                break
            else:
                print("Invalid choice. Please select a number (1-6).")

if __name__ == "__main__":
    MainMenu().display_menu()