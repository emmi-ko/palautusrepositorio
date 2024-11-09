class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nation):
        sorted_players = sorted(self._players, key=lambda x: (self.sort_by_points(x), self.sort_by_goals(x), self.sort_by_assists(x)), reverse=True)

        result = []
        for player in sorted_players:
            if player.nationality == nation:
                result.append(player)
        
        return result

    def sort_by_points(self, player):
        return player.goals + player.assists
    
    def sort_by_goals(self, player):
        return player.goals
    
    def sort_by_assists(self, player):
        return player.assists
