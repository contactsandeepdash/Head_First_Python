from datetime import datetime
import random

odds = [1,3,5,7,9,11,13,15,17,19,
        21,23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,52,55,57,59]

for i in range(5):
    try:
        right_this_random_time = random.randint(1,60)
        print ("right_this_random_time (minutes): " + str(right_this_random_time))

        # get the index of right_this_random_time
        index = odds.index(right_this_random_time)
        print("index of " + str(right_this_random_time) + " in the odds list = " + str(index))
        #print(index)
    except ValueError:
        print("Looks like an even minute; not in the list.")
