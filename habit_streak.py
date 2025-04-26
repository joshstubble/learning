# habit_streak.py
"""Compute the longest consecutive 'Y' streak in a list of Y/N entries.

Example
-------
$ python3 habit_streak.py
Paste Y/N list (e.g. Y,N,Y): Y,N,Y,Y,Y,N
✅  Your longest streak is 3 day(s)!
"""

from typing import List


def longest_streak(entries: List[str]) -> int:
    """
    Return the length of the longest consecutive run of "Y" in `entries`.

    Parameters
    ----------
    entries : list[str]
        List containing 'Y' or 'N' (case-insensitive).

    Examples
    --------
    >>> longest_streak(["Y", "Y", "N", "Y"])
    2
    """
    best = current = 0
    for val in entries:
        if val.upper() == "Y":
            current += 1
            best = max(best, current)
        else:
            current = 0
    return best


if __name__ == "__main__":
    raw = input("Paste Y/N list (e.g. Y,N,Y): ")
    # Split on commas, strip whitespace, ignore empty strings
    cleaned = [s.strip() for s in raw.split(",") if s.strip()]
    streak = longest_streak(cleaned)
    print(f"\n✅  Your longest streak is {streak} day(s)!\n")
