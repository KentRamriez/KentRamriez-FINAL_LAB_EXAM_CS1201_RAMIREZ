import random
import os
from datetime import datetime
from utils.score import ScoreSystem

class DiceGame:
    def __init__(self):
        self.total_rounds = 3

    def play(self, user):
        total_score = 0
        total_stage_wins = 0
        current_stage = 1

        while True:
            stage_score = 0
            stage_won = 0
            os.system('cls' if os.name == 'nt' else 'clear')

            print(f"\nSTAGE {current_stage}\n")

            for _ in range(self.total_rounds):
                user_roll = random.randint(1, 6)
                computer_roll = random.randint(1, 6)
                print(f"{user.username} rolled: {user_roll}\nCPU rolled: {computer_roll}")

                while user_roll == computer_roll:
                    print("It's a draw! A tiebreaker commences...\n")
                    user_roll = random.randint(1, 6)
                    computer_roll = random.randint(1, 6)
                    print(f"{user.username} rolled: {user_roll}\nCPU rolled: {computer_roll}")

                if user_roll > computer_roll:
                    print(f"{user.username} has won the round.\n")
                    stage_score += 1
                    stage_won += 1
                else:
                    print(f"{user.username} has lost the round.\n")

            total_score += stage_score
            total_stage_wins += stage_won

            print(f"\nYou won {stage_score} points!")
            print(f"\nYou now have a total of {total_score} points!")

            if stage_won == 0:
                input("\nGame Over. You lost on every round and fell off the stage. Press enter to go back to game menu...")
                break

            if total_stage_wins == 3:
                total_score += 3
                print("\nWhat luck you have! You have won every round of the stage and are rewarded with 3 more additional points!")
                print(f"\nYou now have a total of {total_score} points!")

            continue_choice = input("\nDo you wish to keep playing unto the next stage? (1 for yes, 0 for no): ")

            while continue_choice not in ('1', '0'):
                continue_choice = input("Invalid Choice. Do you wish to keep playing unto the next stage? (1 for yes, 0 for no): ")

            if continue_choice == '0':
                break

            current_stage += 1

        print(f"\nTotal Points Earned: {total_score}")
        print(f"\nRounds Won: {total_stage_wins}")

        os.system('cls' if os.name == 'nt' else 'clear')

        score_manager = ScoreSystem()
        score_manager.save_scores(user.username, total_score, total_stage_wins, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def show_leaderboard(self):
        score_manager = ScoreSystem()
        scores = score_manager.load_scores()

        if scores:
            scores.sort(key=lambda x: x['score'], reverse=True)
            os.system('cls')
            print("\nTop 10 Leading Scores:\n")
            for i, score in enumerate(scores[:10], 1):
                print(f"{i}. {score['username']}: Total Score : {score['score']}, Rounds Won: {score['wins']}, Date and Time Acquired: {score['date_achieved']}")
        else:
            os.system('cls')
            print("\nTop 10 Leading Scores:\n")
            print("No scores recorded yet.")

        input("\nPress Enter to go back to the game menu...")

    def logout(self):
        return

    def game_menu(self, user):
        os.system('cls')
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Hello, {user.username}, Welcome to the DICE GAME!")
            print("\n1. Play Dice Game")
            print("\n2. Leaderboards")
            print("\n3. Log Out")

            choice = input("\nWhat would you like to do?: ")

            if choice == "1":
                self.play(user)
            elif choice == "2":
                self.show_leaderboard()
            elif choice == "3":
                self.logout()
                return
            else:
                print("Invalid Input. Please Try Again.")