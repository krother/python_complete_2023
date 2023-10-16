from typing import List


number = 9


def myfunc(a: int, b: List[int], c: str="hello", *args, **kwargs) -> int:
    """
    order of function arguments:
    1. obligatory parameters (a, b)
    2. optional parameter (c)

    dont worry about these in your own functions
    3. extra optional parameters (*args) -> list
    4. extra keyword parameter (**kwargs) -> dict
    """
    # Dont do this!
    # global number
    # number = 99
    print(data)   # looks for variable in the main scope  BAD IDEA
    b.append(10)  # not a great idea either!
    return a + sum(b)


# function call
data = [8,9]
result = myfunc(a=7, b=data)
print(result)
print(number)
print(data)
