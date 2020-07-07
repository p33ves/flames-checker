import string
from collections import OrderedDict


def get_name(name: str) -> list:
    return [char for char in name.lower() if char in set(string.ascii_lowercase)]


def get_count(name1: list, name2: list) -> int:
    big, small = (name1, name2) if len(name1) > len(name2) else (name2, name1)
    for char in small:
        if char in big:
            small.remove(char)
            big.remove(char)
    return len(big)+len(small)


def show_flames(token: int):
    letters = OrderedDict()
    letters.update([('F', False), ('L', False), ('A', False),
                    ('M', False), ('E', False), ('S', False)])
    display = " F L A M E S "
    result = list()
    counter = 0
    while True:
        for key, val in letters.items():
            if check_last(letters, key) is False:
                if val is False:
                    counter += 1
                    if counter == token:
                        letters[key] = None
                        display = display.replace(key, '\u0336' + key)
                        result.append(display)
                        counter = 0
            else:
                letters[key] = True
                return f"You got {key}"


def check_last(map: dict, this: str) -> bool:
    for key, val in map.items():
        if (val is False) and (key != this):
            return False
    return True


def checker(input1: str, input2: str) -> str:
    """ input1 = input("Enter first person's name:")
    input2 = input("Enter second person's name:")"""
    name1 = get_name(input1)
    name2 = get_name(input2)
    count = get_count(name1, name2)
    return show_flames(count)
