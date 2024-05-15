from utils.user_manager import UserManager
from utils.dice_game import DiceGame
import os

class Main:
    def __init__(self):
        self.user_manager = UserManager()
        self.dice_game = DiceGame()

    def main(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Welcome to DICE GAME")
            print("\n1. Register")
            print("\n2. Log In")
            print("\n3. Exit")

            main_choice = input("\nWhat would you like to do?: ")

            if main_choice == "1":
                self.user_manager.register()
            elif main_choice == "2":
                loggedIn_user = self.user_manager.login()
                if loggedIn_user:
                    self.dice_game.game_menu(loggedIn_user)
            elif main_choice == "3":
                exit()
            else:
                input("\nInvalid Input. Press enter to try again...")

if __name__ == "__main__":
    screen = Main()
    screen.main()