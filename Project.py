
# Frank Lenge 
# EE-551: Python
# Project


class Player(object):
	def __init__(self):
		self.name = None
		self.life = 3 
		self.Pass = False
		self.addkey = False
		self.subkey = False
		self.mulkey = False
		self.divkey = False

	def resetlife(self):
		self.life = 3
		self.Pass = False

	def correct(self):
		self.life = self.life

	def incorrect(self):
		self.life -= 1 

	def issuccess(self):
		if self.life <= 0 :
			self.Pass = False
		else:
			self.Pass = True

	def get_name(self):
		name = input("What is your name?\n")
		while True:

			choice = input("\nAre you sure {} is your name?\n".format(name))

			if choice.lower() == "yes":
				self.name = name
				break
			elif choice.lower() == "no":
				self.get_name()
			else:
				print("Please put yes or no")
				continue


def main():
	def failed(why):
		print("Sorry " + player.name +". You have gotten 3 or more wrong in " + f"{why}"  + ". It seemes you need more work with " + f"{why}" + ". Feel free to try again.\n")
		levelsel()

	def win():
		print("Congratulations " + player.name +", you have won!")
		exit(0)

	def levelsel():
		print("In the hallway you see doors labeled: Addition, Subtraction, Multiplication, Division, and Exit.")
		level = input("\nWhich door will you pick? \n")

    	# Pick a door and we go to a room and something else happens
		if level.lower() == "addition":
			addition()
		elif level.lower() == "subtraction":
			subtraction()
		elif level.lower() == "multiplication":
			multiplication()
		elif level.lower() == "division":
			division()
		elif level.lower() == "exit":
			if player.addkey & player.subkey & player.mulkey & player.divkey:
				win()
			else:
				print("\nYou need all of the keys before you can exit.\n")
				levelsel()
		elif level.lower() == "quit":
			exit(0)
		else:
			print("\nPlease pick one of the doors.\n")
			levelsel()

	#Rooms#
	def addition():

		player.resetlife()

		questionkey = {1:"1+1", 2:"2+3", 3:"12+24", 4:"15+27", 5:"83+47", 6:"21+136", 7:"325+76", 8:"812+289", 9:"1321+1678", 10:"3251+2895"}

		answerkey = {1:2, 2:5, 3:36, 4:42, 5:130, 6:157, 7:401, 8:1101, 9:2999, 10:6146}
		
		print("\nWelcome to the Addition room. Solve 10 Addition problems to get the Addition Key. To return to the hallway type hallway anytime.")
		
		for i in range(1,11): 

			print("\nQuestion "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			if answer == str(answerkey[i]):
				player.correct()
				print("That is correct. \n")
			elif answer.lower() == "quit":
				exit(0)
			elif answer.lower() == "hallway":
				print("\nYou have left the Addition room. \n")
				levelsel()
			else:
				player.incorrect()
				print("That is incorrect.\n")

		player.issuccess()

		if player.Pass:
			player.addkey = True
			print("Congratulations you have completed the Addition room.\n")
			levelsel()
		else:
			failed("addition")

	def subtraction():
		player.resetlife()

		questionkey = {1:"1-1", 2:"9-4", 3:"15-8", 4:"85-36", 5:"124-83", 6:"527-286", 7:"1593-964", 8:"9-15", 9:"27-85", 10:"167-671"}

		answerkey = {1:0, 2:5, 3:7, 4:49, 5:41, 6:241, 7:629, 8:-6, 9:-58, 10:-504}
		
		print("Welcome to the Subtraction room. Solve 10 Subtraction problems to get the Subtraction Key. To return to the hallway type hallway anytime.")
		
		for i in range(1,11): 

			print("Question "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			if answer == str(answerkey[i]):
				player.correct()
				print("That is correct.\n")
			elif answer.lower() == "quit":
				exit(0)
			elif answer.lower() == "hallway":
				print("You have left the Subtraction room.\n")
				levelsel()
			else:
				player.incorrect()
				print("That is incorrect.\n")

		player.issuccess()

		if player.Pass:
			player.subkey = True
			print("Congratulations you have completed the Subtraction room.\n")
			levelsel()
		else:
			failed("subtraction")

	def multiplication():
		player.resetlife()

		questionkey = {1:"1*1", 2:"5*4", 3:"6*9", 4:"12*5", 5:"8*19", 6:"21*7", 7:"23*12", 8:"64*15", 9:"125*21", 10:"543*128"}

		answerkey = {1:1, 2:20, 3:54, 4:60, 5:152, 6:147, 7:276, 8:960, 9:2625, 10:69504}
		
		print("Welcome to the Multiplication room. Solve 10 Multiplication problems to get the Multiplication Key. To return to the hallway type hallway anytime.")
		
		for i in range(1,11): 

			print("Question "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			if answer == str(answerkey[i]):
				player.correct()
				print("That is correct.\n")
			elif answer.lower() == "quit":
				exit(0)
			elif answer.lower() == "hallway":
				print("You have left the Multiplication room.\n")
				levelsel()
			else:
				player.incorrect()
				print("That is incorrect.\n")

		player.issuccess()

		if player.Pass:
			player.mulkey = True
			print("Congratulations you have completed the Multiplication room.\n")
			levelsel()
		else:
			failed("multiplication")

	def division():
		player.resetlife()

		questionkey = {1:"1/1", 2:"16/4", 3:"36/9", 4:"325/5", 5:"162/18", 6:"192/24", 7:"288/12", 8:"490/35", 9:"546/26", 10:"1376/43"}

		answerkey = {1:1, 2:4, 3:4, 4:65, 5:9, 6:8, 7:24, 8:14, 9:21, 10:32}
		
		print("Welcome to the Division room. Solve 10 Division problems to get the Division Key. To return to the hallway type hallway anytime.")
		
		for i in range(1,11): 

			print("Question "+ str(i) + ":")
			answer = input("What is " + questionkey[i] + "?\n")

			if answer == str(answerkey[i]):
				player.correct()
				print("That is correct.\n")
			elif answer.lower() == "quit":
				exit(0)
			elif answer.lower() == "hallway":
				print("You have left the Division room.\n")
				levelsel()
			else:
				player.incorrect()
				print("That is incorrect.\n")

		player.issuccess()

		if player.Pass:
			player.divkey = True
			print("Congratulations you have completed the Division room.\n")
			levelsel()
		else:
			failed("division")


	print("Hello and welcome to my project.")

	player = Player()
	player.get_name()

	print("\nHello, " + player.name + " today I will be testing your math skills in the form of a fun game")
	print("You will find yourself in a corridor with many doors. Each door will have a mathmatical operation on it. By entering each room and solving 10 corresponding equations you will recieve a key. Get all the keys and you can exit the hallway. Be careful not to get 3 incorrect answer for any given room.")
	print("\nTo quit without finishing the test type quit anywhere.")
	print("\nGood luck and have fun!")
	print("\nSuddenly you realize that you are in a corridor with many doors.\n")
    
	levelsel()


if __name__ == "__main__":
	main()

