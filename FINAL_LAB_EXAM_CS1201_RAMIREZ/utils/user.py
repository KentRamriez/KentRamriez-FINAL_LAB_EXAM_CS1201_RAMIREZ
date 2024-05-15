class User:
    def __init__(self, username, password, score = 0, wins = 0): #Initialize data for users
        self.username = username
        self.password = password
        self.score = score
        self.wins = wins