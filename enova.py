# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:50:13 2013

@author: Oscar
"""

import requests
import json
from time import sleep

def testcode():
    while True:
        sleep(1)
        r = requests.get("http://nolimitcodeem.com/api/players/1ca0b996-e986-4d92-93b5-d89a324d88c8")
        text = r.json()
#        1ca0b996-e986-4d92-93b5-d89a324d88c8
        havePair = False
        wasRaise = False
       
        if text["your_turn"]:
            card1Val = text["hand"][0][0]
            card2Val = text["hand"][1][0]
            card1Suit = text["hand"][0][1]
            card2Suit = text["hand"][1][1]
            
            
            actions = params = discards = None
            numPlayers = text["players_at_table"]
    #        for x in range (0,numPlayers):
            if (text["betting_phase"] == "deal"):
                if card1Val == card2Val:
                    action = "raise"
                    params = text["stack"]/6
                    havePair = True
                elif (card1Suit=='J' or card1Suit=='Q' or card1Suit=='K' or card1Suit=='A') and (card2Suit=='J' or card2Suit=='Q' or card2Suit=='K' or card2Suit=='A'):
                    action = "raise"
                    params = text["stack"]/10
                elif (card1Val <= 7 and (card2Val!='A' or card2Val!='K')) or (card2Val <= 7 and (card1Val!='A' or card1Val!='K')):
                    action = "fold"
                    params = None
                else:
                    action = "check"
                    params = None
            elif (text["betting_phase"] == "flop"):
                comCard1Val = text["community_cards"][0][0]
                comCard2Val = text["community_cards"][1][0]
                comCard3Val = text["community_cards"][2][0]
                comCard1Suit = text["community_cards"][0][1]
                comCard2Suit = text["community_cards"][1][1]
                comCard3Suit = text["community_cards"][2][1]
                for x in range (0,text["total_players_remaining"]):
                    temp = text["players_at_table"]
                    player = temp[x]
                    playerActions = player["actions"]
                    if playerAction["action"]=="raise":
                        wasRaise = True
                if (comCard1Val == card1Val or comCard2Val == card1Val or comCard3Val == card1Val or comCard1Val == card2Val or comCard2Val == card2Val or comCard3Val == card2Val):
                    action = "raise"
                    params = text["stack"]/6
                    havePair = True
                elif havePair:
                    if (wasRaise == True):
                        action = "call"
                        params = None
                    else:
                        action = "check"
                        params = None
                elif (havePair == False):
                    if (wasRaise == True):
                        action = "call"
                        params = None
                    else:
                        action = "check"
                        params = None
                else:
                    if (wasRaise == True):
                        action = "call"
                        params = None
                    else:
                        action = "check"
                        params = None
            else:
                for x in range (0,text["total_players_remaining"]-1):
                        if actions[x]["action"]=="raise":
                            wasRaise = True
                if havePair:
                    if (wasRaise == True):
                        action = "call"
                        params = None
                    else:
                        action = "check"
                        params = None
                elif (havePair == False):
                    if (wasRaise == True):
                        action = "call"
                        params = None
                    else:
                        action = "check"
                        params = None
                else:
                    if (wasRaise == True):
                        action = "call"
                        params = None
                    else:
                        action = "check"
                        params = None
            if (action == "fold"):
                my_action = {"action_name":action}
            else:
                my_action = {"action_name":action, "amount":params}
            r = requests.post("http://nolimitcodeem.com/api/players/1ca0b996-e986-4d92-93b5-d89a324d88c8/action",my_action)
 #   if text[turn]

testcode()