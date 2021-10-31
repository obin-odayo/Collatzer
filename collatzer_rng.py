import random
import sys
import time as t
from collatzer_main import *


def minMaxRNG():
    userMin = int(input("""
Min
< """))
    userMax = int(input("""\n
Max
< """))
    randomNumber = random.randint(userMin, userMax)
    print("\nGenerated Number: ", randomNumber)


def piValRNG():
    # 3.1415926535 8979323846
    userMin = int(input("""
Min
< """))

    userMax = int(input("""\n
Max
< """))

    evenNumbers = (2, 4, 6, 8)

    oddNumbers = (3, 5, 7, 9)

    randomNumber = random.randint(1, 21)

    if randomNumber in evenNumbers:
        if userMin % 2 == 1:
            userMin += 1
        print(userMin)
        finalRandomNumber = random.randrange(userMin, userMax, 2)
    elif randomNumber in oddNumbers:
        if userMin % 2 == 0:
            userMin += 1
        print(userMin)
        finalRandomNumber = random.randrange(userMin, userMax, 2)
    else:  # if randomNumber == 1
        finalRandomNumber = random.randint(1, 9)

    print("\nGenerated Number: ", finalRandomNumber)


def importCollatzer():
    pass


if __name__ == "__main__":
    while True:
        print("""
Random Number Generator
Created for Collatzer.
[1] - Min - Max RNG
[2] - Pi Digits RNG
[0] - Exit""")
        choice = int(input("\n< "))
        if choice == 1:
            minMaxRNG()
        elif choice == 2:
            piValRNG()
        elif choice == 0:
            print("\nGoodbye...")
            t.sleep(1)
            print("\nHold On...")
            t.sleep(3)
            sys.exit()
