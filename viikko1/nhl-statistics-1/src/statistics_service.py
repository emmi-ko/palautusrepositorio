from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3




class StatisticsService:
    def __init__(self, reader):
        self._players = reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, sort_by=SortBy.POINTS):
        if sort_by == SortBy.ASSISTS:
            sorted_players = sorted(self._players, key= self.sort_by_assists, reverse=True)
        elif sort_by == SortBy.GOALS:
            sorted_players = sorted(self._players, key= self.sort_by_goals, reverse=True)
        else:
            sorted_players = sorted(self._players, key= self.sort_by_points, reverse=True)

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result

    def sort_by_points(self, player):
        return player.goals + player.assists
    
    def sort_by_goals(self, player):
        return player.goals
 
    def sort_by_assists(self, player):
        return player.assists
        
        
    

