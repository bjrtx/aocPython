import itertools
from functools import cache

from aocd.models import Puzzle
from more_itertools import nth

puzzle = Puzzle(year=2023, day=12)
data = [(m, eval(tup)) for m, tup in [line.split() for line in puzzle.input_data.splitlines()]]


@cache
def possibilities(s: str, tup: tuple[int]):
    s = s.lstrip('.')
    if s and tup:
        if s[0] == '#':
            n = tup[0]
            compatible = len(s) >= n and '.' not in s[:n] and nth(s, n) != '#'
            return possibilities(s[n + 1:], tup[1:]) if compatible else 0
        else:  # s[0] == '?'
            return possibilities('#' + s[1:], tup) + possibilities(s[1:], tup)
    else:
        return int(not tup and '#' not in s)


new_data = [('?'.join(m for _ in range(5)), tup * 5) for m, tup in data]
puzzle.answer_a, puzzle.answer_b = [sum(itertools.starmap(possibilities, d)) for d in (data, new_data)]
