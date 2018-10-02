#Homework 02d
#Justin Gallicchio
#CSE 2050


#mutable(can be modified) vs. immutable(cannot be modified)
#immutable ex: int, float, string, tuple
#mutable ex: lists, dicts, sets

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
def findset(lst):
    cards = Dict_create(lst)                                            #assignment + dict function = loops n times + 1
    third = ''                                                              #assignment = 1
    res = False                                                      #assignment = 1
    indA = 0                                                                #assignment = 1
    indB = 0                                                                #assignment = 1
    #loops n times
    for indA in range(len(lst)):
        #loops n times
        for indB in range(1, len(lst)):
            if (lst[indA] != lst[indB]):                            #expression = 1
                third = third_card(lst[indA], lst[indB])            #assignment + function = depends on length of card
                if (third in cards):                                        #expession = 1
                    res = True
        #print(indB)
    return res                                                   #return statement = 1
