""" 
This is an application with the basic statements or Python
it should be run as a daemonset on my kubernetes cluster
It creates a game of 6 numbers betwee 1 and 60 and compare with old lottery finding 
how many games could be wan with more than 4 numbers.
"""
import logging
import random
import results
import time
logging.basicConfig(level=logging.DEBUG)


def createGame():
    numbers = {random.randint(1, 60), random.randint(1, 60), random.randint(1, 60),
               random.randint(1, 60), random.randint(1, 60), random.randint(1, 60)}
    while(len(numbers) < 6):
        numbers.add(random.randint(1, 60))
    return numbers


def compareGame():
    logging.debug("Game compared")


logging.info("Application started")
logging.info("Loading all games")
gameResults = results.Results("./files/export.csv")
logging.info("%d games loaded", len(gameResults.gamedic))
seq = 1
while(True):
    game = createGame()
    for key, value in gameResults.gamedic.items():
        accert = game.intersection(value["game"])
        if (len(accert) > 3):
            logging.info(
                "%s - %s - %s - %s - %s", seq, key, len(accert), game, value["game"])
    seq = seq + 1
    time.sleep(1)
