def print_range(start: int, end: int, Between: str = '😁'):
    text = ''
    for i in range(start, end + 1):
        if i == end:
            text = text + str(i)
        else:
            text = text + str(i) + Between
    print(text)


def print_text(Text1: str, Text2: str, Text3: str):
    print(Text1 + Text2 + Text3)
