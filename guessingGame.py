import random
import time

print("############################################## Welcome To Guessing Game ##############################################")

numberToGuess = random.randint(1,100)
finish = False
firstTurn = True
guesses = []
playAgain = 0
while True:

	while True:
		guess = int(input("Guess the number between 1 to 100: \r\n"))
		if guess < 1 or guess > 100:
			print("OUT OF BOUNDS")
		else:
			break
	guesses.append(guess)
	
	if numberToGuess == guess:
		print("Correct Answer!!!")
		print("You took {} guesses to Win".format(len(guesses)))
		finish = True
		
	elif firstTurn:
		if abs(numberToGuess-guess) <= 10:
			print("WARM!")
			firstTurn = False
		else:
			print("COLD!")
			firstTurn = False
	else:
		if abs(numberToGuess-guess) < abs(numberToGuess-guesses[-2]):
			print("WARMER!")
		else:
			print("COLDER!")

	while finish:
		playAgain = int(input("Play again? \r\n 1.Yes 2.No\r\n"))
		if playAgain == 1 or playAgain == 2:
			if playAgain == 2:
				break
			if playAgain == 1:
				numberToGuess = random.randint(1,100)
				finish = False
				firstTurn = True
				guesses = []
				playAgain = 0
		else:
			print("Please enter 1 for Yes or 2 for No")
	
	if playAgain == 2:
		print("Thanks for playing. \r\nSee you next time.")
		time.sleep(3)
		break