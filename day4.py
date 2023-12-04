def parse_game(winning, card):
    card_total = 0
    matches = 0
    win = []
    select = []
    win = winning.split(" ")
    select = card.split(" ")
    select = [i for i in select if i != '']
    for line in select:
        for line2 in win:
            if line == line2:
                if card_total == 0:
                    card_total = 1
                else:
                    card_total = card_total*2
                matches +=1
    return card_total, matches

def parse_cards(inputs):
    matched_cards = {}
    results = []
    winning = []
    cards = []
    scratch = inputs.split("\n")
    for line in scratch:
        a ,b = line.split("|")
        a = a.split(":")[1]
        winning.append(a)
        cards.append(b)
    for idx, line in enumerate(winning):
        r = []
        m = 0
        mat = 0
        if str(idx+1) in matched_cards:
            matched_cards[str(idx+1)] +=1
        else:
            matched_cards[str(idx+1)] = 1
        while mat < matched_cards[str(idx+1)]:
            r, m = parse_game(line, cards[idx])
            s = 1
            mat +=1
            while s <= m:
                next_card = idx+s+1
                if str(next_card) in matched_cards:
                    matched_cards[str(next_card)] +=1
                else:
                    matched_cards[str(next_card)] = 1
                s+=1
        results.append(r)
    return results, matched_cards

inputs = open("d4in.txt", "r")
scratch_cards = inputs.read()
result, card_total = parse_cards(scratch_cards)
TOTAL = 0
t2 = 0
for m_key in card_total:
    t2 = t2 + card_total[m_key]
for i in result:
    TOTAL+=int(i)
print(TOTAL)
print("Total Number of matches")
print(t2)
