from player_reader import PlayerReader
from player_statistics import PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def main():
    
    console.print("NHL statistics by nationality\n", style="italic")

    season = Prompt.ask("Select season", choices=["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25"])
    select_nationality(season)

def select_nationality(season):
    
    nationality = Prompt.ask(f"\nSelect nationality", choices=["AUT","CZE","AUS","SWE","GER","DEN","SUI","SVK","NOR","RUS","CAN","LAT","BLR","SLO","USA","FIN","GBR"])

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    players = stats.top_scorers_by_nationality(nationality)

    table = Table(title=f"TOP scorers of {nationality} season {season}")
    table.add_column("Name", style="cyan", no_wrap=True)
    table.add_column("Team", style="magenta")
    table.add_column("Goals", style="green")
    table.add_column("Assists", style="green")
    table.add_column("Points", style="green")

    for player in players:
        table.add_row(f"{player.name}",f"{player.team}",f"{player.goals}", f"{player.assists}", f"{player.points()}")

    console.print(table, justify="left")
    select_nationality(season)


if __name__ == "__main__":
    main()
