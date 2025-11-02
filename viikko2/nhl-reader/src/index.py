#import rich
from rich.console import Console
from rich.table import Table
import requests
from .player import Player

# pylint: disable=too-few-public-methods
class PlayerReader:
    def __init__(self, url):
        self.url = url
        try:
            self.response = requests.get(url, timeout=10).json()
        except requests.exceptions.Timeout:
            print("Timed out")
        self.players = []

        for player_dict in self.response:
            player = Player(player_dict)
            self.players.append(player)

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def bypoints(self, given_player):
        return given_player.goals + given_player.assists

    def top_scorers_by_nationality(self, nationality):
        players_by_nationality = []

        for player in self.reader.players:
            if player.nationality == nationality:
                players_by_nationality.append(player)

        return sorted(players_by_nationality, reverse=True, key= self.bypoints)

def choose_season():
    print("Choose a season!")
    seasons = ["2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26"]
    while True:
        season = str(input("[2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/2025-26]: "))
        if season not in seasons:
            print("")
            print("not a valid season")
        else:
            return season

def choose_country():
    print("Choose a country!")
    countries = ["USA", "FIN", "CAN", "SWE", "CZE", "RUS",
                 "SLO", "FRA", "GBR", "SVK", "DEN", "NED",
                 "AUT", "BLR", "GER", "SUI", "NOR", "UZB", "LAT", "AUS"]
    while True:
        maa = str(input("[USA/FIN/CAN/SWE/CZE/RUS/SLO/FRA/GBR/SVK/DEN/NED/AUT/BLR/GER/SUI/NOR/UZB/LAT/AUS]: "))
        if maa not in countries:
            print("")
            print("not a valid country/region")
        else:
            return maa

def get_players(season, country):
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats.top_scorers_by_nationality(country)

def print_table(players, season, maa):

    table = Table(title=f"Top players from {maa} in the {season} season")

    table.add_column("nimi", justify="left", style="cyan", no_wrap=True)
    table.add_column("tiimi", style="magenta")
    table.add_column("statsit", justify="left", style="green")

    if len(players) == 0:
        print("No valid players!\n")
        return
    for player in players:
        table.add_row(player.nimi, player.tiimi_ja_maa, player.statsit)

    console = Console()
    console.print(table)


def main():
    print("")
    season = choose_season()
    print("")
    maa = choose_country()

    players = get_players(season, maa)
    print("")
    print_table(players, season, maa)


if __name__ == "__main__":
    main()
