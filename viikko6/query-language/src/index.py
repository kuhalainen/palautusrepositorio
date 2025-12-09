from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from src.query_old import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    # matcher = And(
    #     HasAtLeast(5, "goals"),
    #     HasAtLeast(20, "assists"),
    #     PlaysIn("PHI")
    # )

    # matcher = And(
    #     Not(HasAtLeast(2, "goals")),
    #     PlaysIn("NYR")
    # )

    # matcher = And(
    #     HasFewerThan(2, "goals"),
    #     PlaysIn("NYR")
    # )

    # matcher = Or(
    # HasAtLeast(45, "goals"),
    # HasAtLeast(70, "assists")
    # )

    # matcher = And(
    # HasAtLeast(70, "points"),
    # Or(
    #     PlaysIn("COL"),
    #     PlaysIn("FLA"),
    #     PlaysIn("BOS")
    # )
    # )

    query = QueryBuilder()

    matcher = (
    query
        .one_of(
        query.plays_in("PHI")
            .has_at_least(10, "assists")
            .has_fewer_than(10, "goals"),
        query.plays_in("EDM")
            .has_at_least(50, "points")
        )
        .build()
    )


#And(Or(And(PlaysIn("PHI"), HasAtLeast(10, "assists"), HasFewerThan(10, "goals")),
#       And(PlaysIn("EDM"), HasAtLeast(50, "points"))))

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
