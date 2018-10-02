#Homework 03
#Justin Gallicchio
#CSE 2050

import sys
from setdeck import SetDeck
from FindSet import findset

def checkWin():
    global tabledeck

    cardsontable = tabledeck.view()
    if findset(cardsontable):
        return True
    else:
        return False

def turn():
    global currentround
    global currentplayer
    global players
    global playersleft
    global tabledeck
    global playstatus

    numofcards = players[currentplayer].view()
    if len(numofcards) == 0:
        if currentplayer == (numberofplayers - 1):
            currentplayer = 0
        else:
            currentplayer += 1
    elif len(numofcards) > 0:
        tabledeck.addBottom(players[currentplayer].dealTop())
        if checkWin():
            players[currentplayer].addPileBottom(tabledeck)
            currentround += 1
        else:
            numofcards = players[currentplayer].view()
            if len(numofcards) == 0:
                playersleft -= 1
                playstatus.update({currentplayer: 'out'})
            if currentplayer == (numberofplayers - 1):
                currentplayer = 0
            else:
                currentplayer += 1

def winner():
    global playstatus
    global currentplayer

    curwinner = False
    currentplayer = 0
    while curwinner == False:
        if playstatus[currentplayer] == 'in':
            curwinner = True
        else:
            currentplayer += 1
    return currentplayer

def play():
    global playersleft
    global currentround
    global currentplayer

    while playersleft != 1:
        if currentround == 10000:
            print('Draw after 10000 rounds')
            break

        turn()

    currentplayer = winner()
    if currentround == 1:
        print('Player %d won in %d round.' %(currentplayer, currentround))
    elif currentround < 10000:
        print('Player %d won in %d rounds.' %(currentplayer, currentround))


if __name__ == '__main__':
    numplayers = int(sys.stdin.readline())
    cards = []
    for line in sys.stdin:
        for n in line.split():
            cards.append(n)
    numberofplayers = numplayers
    playersleft = numberofplayers
    currentplayer = 0
    currentround = 1
    startdeck = SetDeck(cards)
    tabledeck = SetDeck()
    players = startdeck.deal(numplayers)
    playstatus = {}
    for x in range(numplayers):
        playstatus.update({x: 'in'})
    play()
