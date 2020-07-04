import string


def get_name(name: str) -> list:
    temp = list(name.lower())
    for char in temp:
        if char not in set(string.ascii_lowercase):
            temp.remove(char)
    return temp


if __name__ == "__main__":
    name1 = input("Enter first person's name:")
    first = get_name(name1)
    name2 = input("Enter second person's name:")
    second = get_name(name2)
