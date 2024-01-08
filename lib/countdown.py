# your code goes here!
# import ipdb
import time


def countdown(int):
    while int >= 1:
        print(f"{int} SECOND(S)!")
        int -= 1
        # countdown_with_sleep(1)
    print('HAPPY NEW YEAR!')

countdown(4)


def countdown_with_sleep(int):
    while int >= 1:
        print(f"{int} SECOND(S)!")
        int -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')
countdown_with_sleep(5)
    

# countdown_with_sleep()
# Our Python program executes so quickly that it doesn't actually count down 
# at the speed of one second per number. Write a second function
# called countdown_with_sleep() that also 
# takes one integer argument for the countdown and makes the loop pause for
#  one second each trip around (hintLinks to an external site.).