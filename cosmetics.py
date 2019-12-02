def print_header():
    print("""
    These are my Solutions for Advent of Code ('https://adventofcode.com/2019'), written in Python.
    The Code was written just for fun and training purposes. If you find mistakes or have suggestions for
    improvement, please contact me.
    """)


def next_day():
    """A generator to format the output between 2 Days"""
    day = 1
    yield f"Day {day:02}: "
    while True:
        day += 1
        yield f"""\n⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄🎄❄🎁⛄
        \nDay {day:02}: """

