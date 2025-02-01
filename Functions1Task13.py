import random

print("Hello! What is your name?")
uname = input()

print(f"Well, {uname}, I am thinking of a number between 1 and 20.")

num = randint(1,20)
count = 0
while(True):
  guess = input("Take a guess.")
  if guess < num:
    print("Too low.")
    count++
  if guess > num:
    print("Too High.")
    count++
  if guess == num:
    print(f"Good job, {uname}! You guessed my number in {count} guesses!")
    break
