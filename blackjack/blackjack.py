#!/usr/bin/python3

import os
from Table import Table, State

#Main
def main():
    print("Reading configuration")
    #Read configuration
    #number of decks
    #initial player money
    #money objective to end the game
    #number of hands without shuffle
    config_file = open(os.path.join(os.getcwd(), "config.txt"), 'r')
    config_ndecks = int(config_file.readline())
    print("nDecks: "+str(config_ndecks))
    config_initialmoney = int(config_file.readline())
    print("Initial money: "+str(config_initialmoney))
    config_objectivemoney = int(config_file.readline())
    print("Objective money: "+str(config_objectivemoney))
    config_nhands2shuffle = int(config_file.readline())
    print("nHands2shuffle: "+str(config_nhands2shuffle))
    config_file.close()

    table = Table(config_ndecks,config_initialmoney,config_objectivemoney,config_nhands2shuffle)

    table.printTable()
    while(table.state != State.FINISH):
        table.resolveState()
        table.printTable()
        if table.player.money >= table.player.objective:
            print("Winner winner chicken dinner")
            table.state = State.FINISH

if __name__ == "__main__":
    main()
