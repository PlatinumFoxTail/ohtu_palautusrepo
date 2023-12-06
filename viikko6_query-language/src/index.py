from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    print("v6t3 Or test2")
    matcher = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)

    print("v6t3 Or test1")
    matcher = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
        )

    for player in stats.matches(matcher):
        print(player)

    print("v6t2 All test")
    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

    print("v6t2 Not test")
    matcher = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)

    print("v6t2 HasFewerThan test")
    matcher = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    for player in stats.matches(matcher):
        print(player)

    print("given assignment test")
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

if __name__ == "__main__":
    main()
