#Homework 03
#Justin Gallicchio
#CSE 2050

import sys
from setdeck import SetDeck
import findsetwar

if __name__ == '__main__':
    players = sys.stdin.readline()
    cards = []
    for line in sys.stdin:
        for n in line.split():
            cards.append(n)

def checkWin():
    pass

def turn(player):
    players[currentplayer].

def round():
    pass

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
currentplayer = 0
currentround = 1
startdeck = SetDeck(cards)
tabledeck = SetDeck()
players = startdeck.deal(players)
