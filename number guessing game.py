import random
n=random.randint(1,101)
guesses=0
while True:
    guess=int(input("guess the number:"))
    guesses+=1
    if guess<n:
        print("please enter higher value")
    elif guess>n:
        print("please enter lower value")
    else:
        print(f"congratulations ! you have guess the correct number {n} in {guesses} attempts.")   
        