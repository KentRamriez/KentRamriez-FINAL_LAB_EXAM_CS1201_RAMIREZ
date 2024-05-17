import os
from utils.user import User

class UserManager:
    def __init__(self):
        self.users = []
        self.data_directory = "data"
        self.database_file = os.path.join(self.data_directory, "databaseUsers.txt")
        self.check_directory_existence()
        self.load_users()

    def register(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nRegister an Account (Leave inputs empty to return.)")
            username = input("Enter your username (4 characters minimum): ")
            if not username:
                return
            if not self.validate_username(username):
                continue

            password = input("Enter your password (8 characters minimum): ")
            if not password:
                continue
            if not self.validate_password(password):
                continue

            if self.existing_username(username):
                input("\nUsername already exists. Please select a different one. Press enter to try again...")
            else:
                self.users.append(User(username, password))
                self.save_users()
                input("\nAccount Successfully Registered! Press enter to go back to main menu...")
                break

    def validate_username(self, username):
        if len(username) < 4:
            input("\nUsername must have at least 4 characters. Press enter to try again...")
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            input("\nPassword must have at least 8 characters. Press enter to try again...")
            return False
        return True

    def existing_username(self, username):
        for user in self.users:
            if user.username == username:
                return True
        return False

    def check_directory_existence(self):
        if not os.path.exists(self.data_directory):
            os.makedirs(self.data_directory)

    def save_users(self):
        with open(self.database_file, "w") as file:
            for user in self.users:
                file.write(f"{user.username},{user.password}\n")

    def load_users(self):
        if os.path.exists(self.database_file):
            with open(self.database_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(',')
                    self.users.append(User(username, password))

    def login(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear') 
            print("\nAccount Login (Leave inputs empty to return.)")
            username = input("Please enter your username: ")
            if not username:
                return
            
            password = input("Enter your password: ")
            if not password:
                continue
            
            for user in self.users:
                if user.username == username and user.password == password:
                    input("\nLogin Successful! Press enter to proceed to game menu...")
                    return user
            else:
                input("\nInvalid username or password. Press enter to try again...")
                continue