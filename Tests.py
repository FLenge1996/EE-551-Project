#Frank Lenge
#EE-551: Python
#Project Test

import pytest

from Project import Player
from Project import main

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

def testPlayerReset():
	player = Player()
	player.life = 0 
	player.resetlife()

	assert(player.life == 3)

def testincorrectanswer():
	player = Player()
	player.incorrect()

	assert(player.life == 2)

def testfailissuccess():
	player = Player()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.incorrect()
	player.issuccess()

	assert(player.Pass == False)

def testpassissuccess():
	player = Player()
	player.incorrect()
	player.issuccess()

	assert(player.Pass == True)