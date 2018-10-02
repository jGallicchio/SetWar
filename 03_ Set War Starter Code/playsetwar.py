#Homework 03
#Justin Gallicchio
#CSE 2050

import sys
from setdeck import SetDeck
from FindSet import findset

if __name__ == '__main__':
    players = sys.stdin.readline()
    cards = []
    for line in sys.stdin:
        for n in line.split():
            cards.append(n)

def checkWin():
    cardsontable = tabledeck.view()
    if(findset(cardsontable) != -1):
        return True
    else:
        return False

def turn(player):
    tabledeck.addTop(players[currentplayer].dealTop())
    if checkWin():
        players[currentplayer].addPileBottom(tabledeck)
        currentround += 1
        if currentplayer == numberofplayers:
            currentplayer = 0
        else:
            currentplayer += 1


def play():
    while numberofplayers != 1:
        if currentround == 10000:
            print('Draw after 10000 rounds')
            break

        turn(currentplayer)
    if currentround == 1:
        print('Player %d won in %d round.' %(currentplayer, currentround))
    elif currentround < 10000:
        print('Player %d won in %d rounds.' %(currentplayer, currentround))


numberofplayers = players
playersleft = numberofplayers
currentplayer = 0
currentround = 1
startdeck = SetDeck(cards)
tabledeck = SetDeck()
players = startdeck.deal(players)
