# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 14:34:00 2015

@author: Hoang Nguyen
"""

import testUtility
import Dominion

#Get player names
player_names = ["Annie","*Ben"]

#number of curses and victory cards
nV, nC = testUtility.calcNvNc(len(player_names) + 2)  # Introduce bugs

#Define box
box = testUtility.initBox(nV)

supply_order = testUtility.initSupplyOrder()

# Initialize supply
supply = testUtility.initSupply(box, nV, nC, player_names)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.createPlayers(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)