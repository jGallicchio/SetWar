#Homework 02d
#Justin Gallicchio
#CSE 2050


#mutable(can be modified) vs. immutable(cannot be modified)
#immutable ex: int, float, string, tuple
#mutable ex: lists, dicts, sets

import sys

if __name__ == '__main__':
    numbers = []
    for line in sys.stdin:
        for n in line.split():
            numbers.append(n)

def Dict_create(lst):
    lst_dict = {}
    for x in range(len(lst)):
        lst_dict[lst[x]] = x
    return lst_dict

def third_card(card1, card2):
    card3 = []
    for x in range(len(card1)):
        if (card1[x] == card2[x]):
            card3.insert(x, str(card1[x]))
        elif (int(card1[x]) + int(card2[x]) == 3):
            card3.insert(x, '0')
        elif (int(card1[x]) + int(card2[x]) == 2):
            card3.insert(x, '1')
        elif (int(card1[x]) + int(card2[x]) == 1):
            card3.insert(x, '2')
    return ''.join(card3)

#Time Complexity of Function = O(n^2)
def findset(list):
    cards = Dict_create(numbers)                                            #assignment + dict function = loops n times + 1
    third = ''                                                              #assignment = 1
    num_of_cards = -1                                                       #assignment = 1
    indA = 0                                                                #assignment = 1
    indB = 0                                                                #assignment = 1
    #loops n times
    for indA in range(len(numbers)):
        #loops n times
        for indB in range(1, len(numbers)):
            if (numbers[indA] != numbers[indB]):                            #expression = 1
                third = third_card(numbers[indA], numbers[indB])            #assignment + function = depends on length of card
                if (third in cards):                                        #expession = 1
                    if(num_of_cards == -1):                                 #expression = 1
                        num_of_cards = cards[third] + 1                     #assignment + dictionary access = 2
                    elif(max(cards[third], indA, indB) < num_of_cards):     #expression + max function = 2
                        num_of_cards = max(cards[third], indA, indB) + 1    #assignment + max function + addition = 3
        #print(indB)
    return num_of_cards                                                     #return statement = 1


print(findset(numbers))
