class Player:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id
        self.match_history = []

    def play_match(self, match):
        self.match_history.append(match)

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_tables(self):
        tables = []
        for match in self.match_history:
            tables.append(match.get_table())
        return tables
