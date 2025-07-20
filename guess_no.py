import random

random_number = random.randint(1,10)

attempt = 0 
while True :
    a = int(input("Guess the number between 1 to 10 : "))
    attempt += 1

    if a < random_number:
        print("Higher number please")
    elif a > random_number:
        print("Lower number please")
    else:
        print(f"Great! u choose the correct number : {random_number}")
        print(f"Your total attempts : {attempt}")
        break