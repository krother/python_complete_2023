"""
Automated test:
  PASSES: there still might be a problem
  FAILS : we know there is a problem

-> automated test proves the presence of bugs or other issues
"""


def add(first: int, second: int) -> int:
    """adds two numbers"""
    return first + second


# test code
assert add(3, 4) == 7  # if True: OK, if False: error
assert add(4, 4) == 8
