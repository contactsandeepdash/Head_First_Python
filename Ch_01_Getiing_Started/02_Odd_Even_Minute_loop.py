from datetime import datetime
import time

odds = [1,3,5,7,9,11,13,15,17,19,
        21,23,25,27,29,31,33,35,37,39,
        41,43,45,47,49,51,52,55,57,59]

for i in range(5):
    time.sleep(5)   # imported from time package
    right_this_time = datetime.today().minute
    print ("right_this_time (minutes): " + str(right_this_time))

    if right_this_time in odds:
        print ("This minute seems a little odd.")
    else:
        print ("Not an odd minute.")

