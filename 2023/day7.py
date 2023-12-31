from io import TextIOWrapper
from collections import Counter

cards_name = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
cards_mapped = {cards_name[len(cards_name) - i - 1]: i for i in range(len(cards_name))}


def part1(f: TextIOWrapper):
    line = f.readline()
    types = [[] for _ in range(7)]
    while line:
        [cards, bid] = line.split()
        joker_cards = cards
        if "J" in cards:
            common = Counter(cards).most_common(2)
            joker = "J"
            if common[0][0] == "J" and len(common) > 1:
                joker = common[1][0]
            else:
                joker = common[0][0]
            joker_cards = joker_cards.replace("J", joker)
        match sorted(Counter(joker_cards).values(), reverse=True):
            case [5]:
                types[0].append([cards, int(bid)])
            case [4, 1]:
                types[1].append([cards, int(bid)])
            case [3, 2]:
                types[2].append([cards, int(bid)])
            case [3, 1, 1]:
                types[3].append([cards, int(bid)])
            case [2, 2, 1]:
                types[4].append([cards, int(bid)])
            case [2, 1, 1, 1]:
                types[5].append([cards, int(bid)])
            case [1, 1, 1, 1, 1]:
                types[6].append([cards, int(bid)])
            case _:
                print(cards)
                raise ValueError
        line = f.readline()
    for i, t in enumerate(types):
        for j, cards in enumerate(t):
            hex_cards = ""
            for card in cards[0]:
                num = cards_mapped[card]
                hex_num = format(int(num), "X")
                hex_cards += hex_num
            types[i][j][0] = int(hex_cards, base=16)
    for i in range(len(types)):
        types[i] = sorted(types[i], key=lambda cards: cards[0], reverse=True)
    flat_types = []
    for t in types:
        flat_types.extend(t)
    total = sum(cards[1] * (i + 1) for i, cards in enumerate(reversed(flat_types)))
    print(total)


with open("day7.txt", "r") as f:
    part1(f)
