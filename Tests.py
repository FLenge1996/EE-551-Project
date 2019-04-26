#Frank Lenge
#EE-551: Python
#Project Test

#import the pytest module
import pytest

#import the classes and functions from the Project
from Project import Player
from Project import main

#Creating and making sure a test player is initialized correctly
def testplayer():
	player = Player()
	assert(player.name == None)
	assert(player.life == 3)
	assert(player.Pass == False)
	assert(player.addkey == False)
	assert(player.subkey == False)
	assert(player.mulkey == False)
	assert(player.divkey == False)
	assert(player.addtime == 99999)
	assert(player.subtime == 99999)
	assert(player.multime == 99999)
	assert(player.divtime == 99999)

#Test if the Player resets correctly after the default values of life and Pass change
def testPlayerReset():
	player = Player()
	player.life = 0 
	player.Pass = True
	player.resetlife()

	assert(player.life == 3)
	assert(player.Pass == False)

#Test the player life after getting one incorrect answer
def testincorrectanswer():
	player = Player()
	player.incorrect()
	
	assert(player.life == 2)

#Test if a player passed a level after getting 4 incorrect answers
def testfailissuccess():
	player = Player()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == -1)
	assert(player.Pass == False)

#Test if a player passed a level after getting 2 incoorect answers
def testpassissuccess():
	player = Player()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == 1)
	assert(player.Pass == True)

#Test if a player has passed a level after getting 2 incorrect answers after failing the first time
def testpassissuccessafterfail():
	player = Player()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == -1)
	assert(player.Pass == False)

	player.reset()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == 1)
	assert(player.Pass == True)

#Test if a player has passed a level after getting 4 incorrect answers after failing the first time
def testfailissuccessafterfail():
	player = Player()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == -1)
	assert(player.Pass == False)

	player.reset()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == -1)
	assert(player.Pass == False)

#Test reset after passing level
def testfailissuccessafterfail():
	player = Player()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert (player.life == 1)
	assert(player.Pass == True)

	player.reset()

	assert (player.life == 3)
	assert(player.Pass == False)