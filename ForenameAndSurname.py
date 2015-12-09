#Forename and Surname

#  Created by Tiago Ferreira on 07/12/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.

import random
import sys
import time

High = ["H", "h", "High", "high"]
Low = ["L", "l", "low", "Low"]
Left = ["L", "l", "Left", "left"]
Centre = ["C", "c", "Centre", "centre"]
Right = ["R", "r", "right", "Right"]
ComputerHightOptions = ["High", "Low"]
ComputerWidthOptions = ["Left", "Center", "Right"]
Goals = 0

for x in range(0,4):
    KickHightInput = input(Where to do you want to kick the ball? (High, Low): )
	KickWidthInput = input(Where to do you want to kick the ball? (Left, Centre, Right): )

    if KickHightInput in High:
        KickHight = "High"
    elif KickHightInput in Low:
        KickHight = "Low"
    else:
        print("Don't try to fool me!")
        sys.exit()

    if KickWidthInput in Left:
        KickWidth = "Left"
    elif KickWidthInput in Centre:
        KickWidth = "Centre"
    elif KickWidthInput in Right:
        KickWidth = "Right"
    else:
        print("Don't try to fool me!")
        sys.exit()

    ComputerRanHight = random.randint(0,1)
    ComputerRanWidth = random.randint(0.2)

    ComputerHight = ComputerHightOptions[ComputerRanHight]
    ComputerWidth = ComputerWidthOptions[ComputerRanWidth]

    if ComputerWidth == KickWidth and ComputerHight == KickHight:
        print("Save! Aha!")
    else:
        print("Gooooooal!")
        Goals = Goals + 1

print("End of game!")
print("You made " + Goals + " goals!")