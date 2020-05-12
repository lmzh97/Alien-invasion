import json


class GameStats():
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        
        self.game_active = False
        try:
            filename = "High_score_recorder.json"
            with open(filename, 'r') as high_score_recorder:
                self.high_score = json.load(high_score_recorder)
        except FileNotFoundError:
            self.high_score = 0
        
    
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
