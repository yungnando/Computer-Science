#  Created by Tiago Ferreira on 05/11/2015.
#  Copyright (c) 2015 Tiago Ferreira. All rights reserved.


import random


NumberOne = random.randint(1,5000)
NumberTwo = random.randint(1,5000)

Operation = NumberTwo * NumberOne

print("Your first random number is: " + str(NumberOne))

print("Your second random number is: " + str(NumberTwo))
print("Your random number multiplied are: " + str(Operation))
