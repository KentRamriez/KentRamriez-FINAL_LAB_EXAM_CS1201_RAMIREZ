import os
from datetime import datetime

class ScoreSystem:
    def __init__(self):
        pass

    def save_scores(self, username, score, wins, date_achieved):
        with open("gameScores.txt", "a") as file:
            file.write(f"{username},{score},{wins},{date_achieved}\n")

    def load_scores(self):
        scores = []
        if os.path.exists("gameScores.txt"):
            with open("gameScores.txt", "r") as file:
                for line in file:
                    username, score, wins, date_achieved = line.strip().split(',')
                    scores.append({"username": username, "score": int(score), "wins": int(wins), "date_achieved": date_achieved})
        return scores