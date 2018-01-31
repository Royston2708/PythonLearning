# Playing a game to see how high we can climb up the empire state building if we use the following conditions
# for ever roll of dice depending on out come we move up or down
# Dice (1 or 2) - Take one step Down (step= step -1)
# Dice (3,4 or 5) - Take one step up (step = step +1)
# Dice (6) - Roll dice again and walk resulting number of steps up
# we assume we will fall down 0.1% of the times. Falling down means we start from step number zero
# Cant go below step 0


import numpy as np
import pandas as pd

# We set the seed of the rand function in order to make sure that if someone else wants to test the algorithm
# They can generate the same random numbers by using the same seed

np.random.seed(10)

#This sets the limits of the random generation between 0 and 6. 7 is the high limit and is not included
dice = np.random.randint(1,7)

print(np.random.randint(1,7), "\n")

# For a Random Step
step = 20
if dice <=2:
    step = step -1
elif dice <= 5:
    step = step +1
else:
    step = step+ np.random.randint(1,7)

print("You rolled a", str(dice), "on the dice")
print("you are now on step number", str(step))



