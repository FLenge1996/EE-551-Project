
# Frank Lenge 
# EE-551: Python
# Project

#importing the time function for time trials later in the code
import time

#player defined as a class to keep track of several attributes in the game
class Player(object):

	#defining all the attributes of the player
	def __init__(self):
		self.name = None
		self.life = 3 
		self.Pass = False
		self.addkey = False
		self.subkey = False
		self.mulkey = False
		self.divkey = False
		self.addtime = 99999
		self.subtime = 99999
		self.multime = 99999
		self.divtime = 99999

	#class function to reset player attributes for each level
	def resetlife(self):
		self.life = 3
		self.Pass = False


	#when incorrect lower the player's life 
	def incorrect(self):
		self.life -= 1 


	#function that determines if a player has passed a level
	def issuccess(self):
		if self.life <= 0 :
			self.Pass = False
		else:
			self.Pass = True


	#function used to get and store a players name
	def get_name(self):

		#Will first ask the user for their name
		name = input("What is your name?\n")

		while True:

			#double checking their name
			choice = input("\nAre you sure {} is your name?\n".format(name))

			#When player name is confirmed continue
			if choice.lower() == "yes":
				self.name = name
				break

			#If the player wants to change their name from what they originally put
			elif choice.lower() == "no":
				self.get_name()

			#Making sure there is a yes or no answer
			else:
				print("Please put yes or no")
				continue


#main function
def main():


	#Function that plays when failing a level
	def failed(why):
		print("Sorry " + player.name +". You have gotten 3 or more wrong in " + f"{why}"  + ". It seemes you need more work with " + f"{why}" + ". Feel free to try again.\n")
		
		#return to level select
		levelsel()


	#Function that allows the player to complete the game
	def win():

		#Finding the total time it took to beat the game in seconds
		EndGame = time.time()
		Gametime = EndGame - GameStart 
		print("\nCongratulations " + player.name +", you have completed the test in " + '{0:0.2f}'.format(Gametime) + " seconds.\n" )
		
		#Also printing the individual time status for each level as well as the sum of best times.
		timestatus()

		#end the game
		exit(0)


	#function that tells the player how fast they have completed each level
	def timestatus():

		#When the player has not completed the addition room successfully, then the time will not change
		if player.addtime == 99999:
			print("\nYou have not completed the Addition Room")
		
		#when the addition room has been complete the time would be updated
		else:
			print("\nThe fastest you have completed the Addition Room was " + '{0:0.2f}'.format(player.addtime) + " seconds.")
		

		#When the player has not completed the subtraction room successfully, then the time will not change
		if player.subtime == 99999:
			print("You have not completed the Subtraction Room")
		
		#when the subtraction room has been complete the time would be updated
		else:
			print("The fastest you have completed the Subtraction Room was " + '{0:0.2f}'.format(player.subtime) + " seconds.")
		

		#When the player has not completed the multiplication room successfully, then the time will not change
		if player.multime == 99999:
			print("You have not completed the Multiplication Room")

		#when the multiplication room has been complete the time would be updated
		else:
			print("The fastest you have completed the Multiplication Room was " + '{0:0.2f}'.format(player.multime) + " seconds.")


		#When the player has not completed the division room successfully, then the time will not change	
		if player.divtime == 99999:
			print("You have not completed the Division Room\n")

		#when the division room has been complete the time would be updated
		else:
			print("The fastest you have completed the Division Room was " + '{0:0.2f}'.format(player.divtime) + " seconds.\n")


		#If any of the rooms havent been completed there will not be a sum of best times
		if player.addtime == 99999 or player.subtime == 99999 or player.multime == 99999 or player.divtime == 99999:
			pass

		#When all the rooms have been completed Sum of best times will be updated
		else:
			total_time = player.addtime + player.subtime + player.multime + player.divtime
			print("Sum of Best Times: " + '{0:0.2f}'.format(total_time) + " seconds.\n")


	#function that tells the player which levels they have completed
	def status():

		#When all the keys to the exit have been collected the message will change 
		if player.addkey & player.subkey & player.mulkey & player.divkey:
			print("\nYou have all of the keys!")

			#also print the times of the completed rooms 
			timestatus()
		
		#Messages the player if they have completed a level
		else:
			if player.addkey:
				print("\nYou have the Addition Key!")
			if player.subkey:
				print("You have the Subtraction Key!")
			if player.mulkey:
				print("You have the Multiplication Key!")
			if player.divkey:
				print("You have the Division Key!")

			#also prints the time of the completed rooms
			timestatus()


	#this function acts as a level select and lets the player pick a level to complete
	def levelsel():

		#explaining which levels that the player can go into
		print("In the hallway you see doors labeled: Addition, Subtraction, Multiplication, Division, and Exit.")
		
		#Tells the user about the status screen
		print("\nTo see which rooms you have completed type status")
		
		#tells the user how to exit the game if they dont want to finish
		print("To quit the test without finishing type quit")
		
		#ask the user which level they want to do 
		level = input("\nWhich door will you pick? \n")

		#The possible level choices:

		#Addition Level
		if level.lower() == "addition":
			addition()

		#Subtraction Level
		elif level.lower() == "subtraction":
			subtraction()

		#Multiplication Level
		elif level.lower() == "multiplication":
			multiplication()

		#Division Level
		elif level.lower() == "division":
			division()

		#How to Win the game 
		elif level.lower() == "exit":

			#only let the player win if they have completed all of the levels
			if player.addkey & player.subkey & player.mulkey & player.divkey:
				win()

			#otherwise send the player back to level select
			else:
				print("\nYou need all of the keys before you can exit.\n")
				levelsel()

		#Quit the game
		elif level.lower() == "quit":
			print("Goodbye")
			exit(0)

		#lets the player check their status
		elif level.lower() == "status":
			status()
			levelsel()

		#tells the user to select one of the options
		else:
			print("\nPlease pick one of the doors.\n")
			levelsel()

	#The Addition Level
	def addition():

		#Start the level timer
		begin = time.time()

		#resets the player life and passing flag
		player.resetlife()

		#question key
		questionkey = {1:"1+1", 2:"2+3", 3:"12+24", 4:"15+27", 5:"83+47", 6:"21+136", 7:"325+76", 8:"812+289", 9:"1321+1678", 10:"3251+2895"}

		#answer key
		answerkey = {1:2, 2:5, 3:36, 4:42, 5:130, 6:157, 7:401, 8:1101, 9:2999, 10:6146}
		
		print("\nWelcome to the Addition room. Solve 10 Addition problems to get the Addition Key. To return to the hallway type hallway anytime.")
		
		#Asking all the questions in the key and comparing the answers
		for i in range(1,11): 

			print("\nQuestion "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			#if the answer is correct tell them
			if answer == str(answerkey[i]):
				print("That is correct. \n")

			#if the player wants to quit the game let them
			elif answer.lower() == "quit":
				exit(0)

			#allows the player to go back to level select if they went into the wrong room
			elif answer.lower() == "hallway":
				print("\nYou have left the Addition room. \n")
				levelsel()

			#if the player is incorrect then subtract a life and tell them.
			else:
				player.incorrect()
				print("That is incorrect.\n")

		#check if the play has passed
		player.issuccess()

		#if they have passed give them the key and tell them how fast they completed the level in
		if player.Pass:
			player.addkey = True
			end = time.time()
			addtime = end - begin

			#if the completed time if faster then the last recorde quickest time remember that time
			if addtime <= player.addtime:
				player.addtime = addtime

			#report the time they have passed the level in and return to level select
			print("Congratulations you have completed the Addition room in " + '{0:0.2f}'.format(addtime) + " seconds.\n")
			levelsel()

		#if the player has failed then send them a failed message before returning to level select
		else:
			failed("addition")

	#The Subtraction Level
	def subtraction():

		#Start the level timer
		begin = time.time()

		#resets the player life and passing flag
		player.resetlife()

		#question key
		questionkey = {1:"1-1", 2:"9-4", 3:"15-8", 4:"85-36", 5:"124-83", 6:"527-286", 7:"1593-964", 8:"9-15", 9:"27-85", 10:"167-671"}

		#answer key
		answerkey = {1:0, 2:5, 3:7, 4:49, 5:41, 6:241, 7:629, 8:-6, 9:-58, 10:-504}
		
		print("Welcome to the Subtraction room. Solve 10 Subtraction problems to get the Subtraction Key. To return to the hallway type hallway anytime.")
		
		#Asking all the questions in the key and comparing the answers
		for i in range(1,11): 

			print("Question "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			#if the answer is correct tell them
			if answer == str(answerkey[i]):
				print("That is correct.\n")

			#if the player wants to quit the game let them
			elif answer.lower() == "quit":
				exit(0)

			#allows the player to go back to level select if they went into the wrong room
			elif answer.lower() == "hallway":
				print("You have left the Subtraction room.\n")
				levelsel()

			#if the player is incorrect then subtract a life and tell them.
			else:
				player.incorrect()
				print("That is incorrect.\n")

		#check if the play has passed
		player.issuccess()

		#if they have passed give them the key and tell them how fast they completed the level
		if player.Pass:
			player.subkey = True
			end = time.time()
			subtime = end - begin

			#if the completed time if faster then the last recorde quickest time remember that time
			if subtime <= player.subtime:
				player.subtime = subtime

			#report the time they have passed the level in and return to level select
			print("Congratulations you have completed the Subtraction room in " + '{0:0.2f}'.format(subtime) + " seconds.\n")
			levelsel()

		#if the player has failed then send them a failed message before returning to level select
		else:
			failed("subtraction")

	#The multiplication level
	def multiplication():
		
		#Start the level timer
		begin = time.time()

		#resets the player life and passing flag
		player.resetlife()

		#question key	
		questionkey = {1:"1*1", 2:"5*4", 3:"6*9", 4:"12*5", 5:"8*19", 6:"21*7", 7:"23*12", 8:"64*15", 9:"125*21", 10:"543*128"}

		#answer key
		answerkey = {1:1, 2:20, 3:54, 4:60, 5:152, 6:147, 7:276, 8:960, 9:2625, 10:69504}
		
		print("Welcome to the Multiplication room. Solve 10 Multiplication problems to get the Multiplication Key. To return to the hallway type hallway anytime.")
		
		#Asking all the questions in the key and comparing the answers
		for i in range(1,11): 

			print("Question "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			#if the answer is correct tell them
			if answer == str(answerkey[i]):
				print("That is correct.\n")

			#if the player wants to quit the game let them
			elif answer.lower() == "quit":
				exit(0)

			#allows the player to go back to level select if they went into the wrong room
			elif answer.lower() == "hallway":
				print("You have left the Multiplication room.\n")
				levelsel()

			#if the player is incorrect then subtract a life and tell them.
			else:
				player.incorrect()
				print("That is incorrect.\n")

		#check if the play has passed
		player.issuccess()

		#if they have passed give them the key and tell them how fast they completed the level in
		if player.Pass:
			player.mulkey = True
			end = time.time()
			multime = end - begin

			#if the completed time if faster then the last recorde quickest time remember that time
			if multime <= player.multime:
				player.multime = multime

			#report the time they have passed the level in and return to level select
			print("Congratulations you have completed the Multiplication room in " + '{0:0.2f}'.format(multime) + " seconds.\n")
			levelsel()

		#if the player has failed then send them a failed message before returning to level select			
		else:
			failed("multiplication")

	#The division level
	def division():
		
		#Start the level timer
		begin = time.time()

		#resets the player life and passing flag
		player.resetlife()

		#question key
		questionkey = {1:"1/1", 2:"16/4", 3:"36/9", 4:"325/5", 5:"162/18", 6:"192/24", 7:"288/12", 8:"490/35", 9:"546/26", 10:"1376/43"}

		#answer key
		answerkey = {1:1, 2:4, 3:4, 4:65, 5:9, 6:8, 7:24, 8:14, 9:21, 10:32}
		
		print("Welcome to the Division room. Solve 10 Division problems to get the Division Key. To return to the hallway type hallway anytime.")
		
		#Asking all the questions in the key and comparing the answers
		for i in range(1,11): 

			print("Question "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			#if the answer is correct tell them
			if answer == str(answerkey[i]):
				print("That is correct.\n")
			
			#if the player wants to quit the game let them
			elif answer.lower() == "quit":
				exit(0)
			
			#allows the player to go back to level select if they went into the wrong room
			elif answer.lower() == "hallway":
				print("You have left the Division room.\n")
				levelsel()

			#if the player is incorrect then subtract a life and tell them.
			else:
				player.incorrect()
				print("That is incorrect.\n")

		#check if the play has passed
		player.issuccess()

		#if they have passed give them the key and tell them how fast they completed the level in
		if player.Pass:
			player.divkey = True
			end = time.time()
			divtime = end - begin

			#if the completed time if faster then the last recorde quickest time remember that time
			if divtime <= player.divtime:
				player.divtime = divtime

			#report the time they have passed the level in and return to level select
			print("Congratulations you have completed the Division room in " + '{0:0.2f}'.format(divtime) + " seconds.\n")
			levelsel()
	
		#if the player has failed then send them a failed message before returning to level select
		else:
			failed("division")

	#Actual start of the game 
	#Starting the overall Game timer
	GameStart =  time.time()

	#Welcome Statement
	print("Hello and welcome to my project.")

	#Creating the player and getting their name
	player = Player()
	player.get_name()
	
	#Explaining the concept of the game and sending them to level select
	print("\nHello " + player.name + ", today I will be testing your math skills in the form of a fun game")
	print("You will find yourself in a corridor with many doors. Each door will have a mathmatical operation on it. By entering each room and solving 10 corresponding equations you will recieve a key. Get all the keys and you can exit the hallway. Be careful not to get 3 incorrect answer for any given room.")
	print("\nGood luck and have fun!")
	print("\nSuddenly you realize that you are in a corridor with many doors.\n")
   
	levelsel()

#run the main function at the begining of the start up
if __name__ == "__main__":
	main()

