#created by GHaxZ

#importing stuff
import os
from time import sleep
import sys
import random

#define stuff
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

random_numbers = range(0, 10001)

number = random.choice(random_numbers)

#introduction
line1 = "\n This is a number guessing game."

for x in line1:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)

line2 = "\n\n That means I'm gonna think of a number in the range of 1 - 10000, and you have to guess it."

sleep(1.5)

for x in line2:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)

line3 = "\n\n You can do this by entering a number, and I'm gonna tell you if you should go higher or lower."

sleep(1.5)

for x in line3:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)

line4 = "\n\n Pretty easy right?"

sleep(1)

for x in line4:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)

sleep(1)

line5 = "\n\n Then let's start!"

for x in line5:
    print(x, end='')
    sys.stdout.flush()
    sleep(0.05)

sleep(3)
clear()

#main part
while True:
    try:
        user_number = int(input("\n Enter a number: "))

        if user_number > number:
            print("\n lower")
        elif user_number < number:
            print("\n higher")
        else:
            clear()
            print("\n Congratulations! You guessed the number.")
            input(" ")
            break
    except:
        print("\n This is not a valid number.")