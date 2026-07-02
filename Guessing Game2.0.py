import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
score = 0

def generateRandomNumber():
    return random.choice(numbers)

def readScore():
    try:
        with open("myfile.txt", "r") as file:
            return int(file.read())
    except:
        return 0

def writeScore(new_score):
    with open("myfile.txt", "w") as file:
        file.write(str(new_score))
        
randomNumber = generateRandomNumber()

def startGame():
    global score
    global randomNumber
    Guess = int(input("Guess a number: "))
    
    if Guess == randomNumber:
        print("Correct!")
        randomNumber = generateRandomNumber()
        score = readScore() + 1
        writeScore(score)
        print("Score:", score)
        playAgain = input("Would you like to play again?(y/n): ")
        if playAgain == "y":
            startGame()
        else:
            print("Closing...")
    else:
        print("Incorrect, try again!")
        startGame()


def main():
    startGame()

main()
