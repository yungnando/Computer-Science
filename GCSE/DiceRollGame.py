#Dice Roll Game

#  Created by Tiago Ferreira on 09/11/2015.
#  Copyright (c) 2015 Tiago Ferreira

#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

#Version 2.0

#Script now asks the user if he/she wnats to roll 3 or 6 dices.

#Added support for:

#Italian
#French
#Spanish
#German
#Dutch
#Afrikaans
#Swedish
#Norwegian
#Danish
#Faroese
#Cape-Verdean Creole
#Hebrew(Yiddish)
#Irish
#Esperanto
#Japanese
#Mandarin
#Swahili


import random #import random module.
import sys #import system module.
import time #import time module.
positiveOptions = ["YES","yes","Yes","y","Y","Yup","yup","sim","s", "si", "sí", "Si", "Sí",
                   "Oui", "oui", "Ja", "ja", "Ken", "ken", "sea", "Sea", "Shah", "shah",
                   "Jes", "jes", "Hai", "hai", "Ndiyo", "ndiyo", "是", "Shi", "shi"] #Created Array for possitive options.
WantsToPlay = True #Close the loop.
ComputerTotal = 0 #Declare the computer total for each round.
UserTotal = 0 #Declare the computer total for each round.
ComputerScore = 0 #Declare the computer's points.
UserScore = 0 #Declare the user's points.
dice1 = 0 #Intialize dice1.
dice2 = 0 #Intialize dice2.
dice3 = 0 #Intialize dice3.
dice11 = 0 #Intialize dice11.
dice12 = 0 #Intialize dice12.
dice13 = 0 #Intialize dice13.
dice4 = 0 #Intialize dice4.
dice5 = 0 #Intialize dice5.
dice6 = 0 #Intialize dice6.
dice24 = 0 #Intialize dice24.
dice25 = 0 #Intialize dice25.
dice26 = 0 #Intialize dice26. Yeah, I'm really used to C# :)


while WantsToPlay == True: #Started main loop.
    name = input("Hi! What's your name? ") #Ask input from user.
    time.sleep(0.5) #Wait half of a second.
    print("Welcome " + name + ", to the Dice Roll Game!") #Welcome th user.
    WantsTutorial = input("Would you like to go through the tutorial? ") #Ask the user if he/she wnats to see the tutorial.
    if WantsTutorial in positiveOptions: #If the user gives a positive answer:
        print("""Alright, so basically we'll play Dice Roll, a game in which
each of use gets 3 dices, we throw them and the one who has the biggest sum
wins! There will be 5 rounds... """)
        time.sleep(0.5) #Wait half of a second.
        print() #Blank line.
    else: #Else:
        print("Alright...") #Print Alright.
        time.sleep(0.5) #Wait half of a second.

    dicesToRoll = int(input("Do you want to play with 3 or 6 dices? "))

    IsReady = input("OK, ready? ") #Ask if the user is ready.
    if IsReady in positiveOptions: #If yes then start the countdown.
        print("Starting game in...")
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
    else: #Otherwise:
        print("Goodbye, " + name + ".") #Say Goodbye.
        break #Break the loop.
        sys.exit() #Exit the program.
    for x in range(1,6): #Create loop for 5 rounds.
        print("Rolling dices...") #Give a little bit of info on what the program is doing.
        time.sleep(0.5) #Wait half of a second.
        dice1 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice2 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice3 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice4 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice5 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice6 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice11 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice12 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice13 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice24 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice25 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        dice26 = random.randint(1,7) #Give random values on 1 to 6 for each dice.
        print("Summing...") #Give the info that is summing
        time.sleep(0.5) #Wait half of a second.
        if dicesToRoll == 3:
            ComputerTotal = (dice1 + dice2 + dice3) #Sum the total for the computer.
            UserTotal = (dice4 + dice5 + dice6) #Sum the total for the user.
        else:
            ComputerTotal = (dice1 + dice2 + dice3 + dice11 + dice12 + dice13) #Sum the total for the computer.
            UserTotal = (dice4 + dice5 + dice6 + dice24 + dice25 + dice26) #Sum the total for the user.
        print("Comparing totals....") #Give the info that is comparing.
        time.sleep(0.5) #Wait half of a second.
        if ComputerTotal > UserTotal: #Compare the totals, if the computer wins this round,
            print("I won this round!") #Say that it won the round (the program talks in the first person).
            print("(" + str(ComputerTotal) + " > " + str(UserTotal) + ")") #Print the comparison between the 2 totals.
            ComputerScore = ComputerScore + 1 #Give one point to the computer.
            time.sleep(1) #Wait one second.
        elif ComputerTotal < UserTotal: #else if the user wins this round,
            print("You won this round!") #Say that he/she won.
            print("(" + str(ComputerTotal) + " < " + str(UserTotal) + ")") #Print the comparison between the 2 totals.
            UserScore = UserScore + 1 #Give one point to the user.
            time.sleep(1) #Wait one second.
        elif ComputerScore == UserScore: #Else if the score is equalin this round,
            print("Draw!") #Say that it's a draw.
            time.sleep(1) #Wait one second. (No point is given).
    print("The game is over!") #Print that the game is over.
    if ComputerScore == UserScore: #If the number of points is the same,
        print("It's a draw!") #Say that it's a draw.
        print("(" + str(ComputerScore) + " = " + str(UserScore) + ")") #Print the comparison between the 2 scores.
    elif ComputerScore > UserScore: #Else if the computer won,
        print("I won the game!") #Say that it won the game.
        print("(" + str(ComputerScore) + " > " + str(UserScore) + ")") #Print the comparison between the 2 scores.
    elif ComputerScore < UserScore: #Else if the user won,
        print("You won the game!") #Say that he won the game.
        print("(" + str(ComputerScore) + " < " + str(UserScore) + ")") #Print the comparison between the 2 scores.
    UserWantsToPlay = input("Do you want to play again, " + name + "? ") #Ask if the user wants to play again.
    if UserWantsToPlay in positiveOptions: #If yes then,
        WantsToPlay = True #Set the while loop to run again.
    else: #Else,
        WantsToPlay = False #End the loop.
        print("Goodbye, " + name + ", have a nice day!") #Say goodbye.
        time.sleep(0.5) #Wait half a second.
        sys.exit() #Exit the program script.
