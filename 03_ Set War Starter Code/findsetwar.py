def Dict_create(lst):
    lst_dict = {}
    for x in range(len(lst)):
        lst_dict[lst[item]] = x
    return lst_dict

def third_card(card1, card2):
    card3 = [0,0,0,0]
    for x in range(4):
        if (card1[x] == card2[x]):
            card3[x] = card1[x]
        elif (card1[x] + card2[x] == 3):
            card3[x] = 0
        elif (card1[x] + card2[x] == 2):
            card3[x] = 1
        elif (card1[x] + card2[x] == 1):
            card3[x] = 2
    return ''.join(card3)

def findset(list):
    cards = Dict_create(numbers)
    third = ''
    num_of_cards = 0
    indA = 0
    indB = 0
    while indA < len(numbers):
        while indB < len(numbers):
            if (numbers[indA] != numbers[indB]):
                third = third_card(numbers[indA], numbers[indB])
                if (third in cards):
                    num_of_cards = cards[third]
                    print(cards[third])
                    indB = len(numbers)
                else:
                    indB += 1
            else:
                indB += 1
        if(num_of_cards == 0):
            indA += 1
        else:
            indA = len(numbers)
    return num_of_cards
