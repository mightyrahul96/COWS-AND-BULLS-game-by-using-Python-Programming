from random import randint
def random():
    while True:
        n = str(randint(100,999))
        if not(n[0] == n[1] or n[1] == n[2] or n[0] == n[2]):
            return n


name = input("Welcome to the cows and bulls game\nPlease enter your name.")
print("Hi",name)
chances = 5
cows = 0
bulls = 0
num = str(random())
while chances > 0:
    print("You have",chances,"chances left.")
    n = str(input("Enter your guess"))
    if num == n:
        print("Great! You got it right.")
        break
    else:
        for i in range(0,3):
            if n[i] == num[i]:
                bulls += 1
            elif n[i] in num:
                cows  += 1
        print("Keep going. You have",bulls,"bulls and",cows,"cows.")
        bulls = 0
        cows = 0
        chances -=1
print("The correct answer is",num)