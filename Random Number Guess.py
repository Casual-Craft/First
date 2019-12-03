import random
Rnum = random.randint(1, 100)
Count = 1
Guess = int(input("Guess the random value from 1-100 >>> "))

while Rnum != Guess:
    print
    if Guess < Rnum:
        print("Too low, try again!")
        Count += 1
        Guess = int(input("Guess the random value from 1-100 >>> "))
    else:
        print("Too high, try again!")
        Count += 1
        Guess = int(input("Guess the random value from 1-100 >>> "))
print("Well done, you guessed correctly!")
if Count == 1:
    print("It took you", Count, "guess. First try, congratulations!")
else:
    print("It took you", Count, "guesses!")
