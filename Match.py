class Match:
    def __init__(self, player_1, player_2) -> None:
        self.player_1 = player_1
        self.player_2 = player_2

    def set_table(self, table):
        self.table = table

    def get_table(self):
        return self.table
    
    def get_match_terrain(self):
        return self.table.get_terrain_name()
    
    def get_players(self):
        return (self.player_1, self.player_2)
    
    def match_played(self):
        self.player_1.play_match(self)
        self.player_2.play_match(self)

        return self.player_1, self.player_2
    
    def player_was_in_match(self, player):
        return (player.get_name() == self.player_1.get_name()) or (player.get_name() == self.player_2.get_name())
