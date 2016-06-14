from random import randint

secret = randint(1,20)
user_number = 0

while user_number != secret:
    g = input("Guess the Number between 1-20 ")
    user_number = int(g)
    
    if user_number > 20:
        print("out of range")
    else:
        if user_number > secret:
            print("Guess Lower")
        else:
             if user_number < secret:
                 print("Guess Higher")

print("Right!")




