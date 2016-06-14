from random import randint

secret = randint(1,20)
user_number = 0
user_guesses = 1

# testing -- print("secret is ", secret)
while user_number != secret:
    g = input("Guess the Number between 1-20 ")
    user_number = int(g)
    
    if user_number > 20:
        print("out of range")
        user_guesses = user_guesses + 1
    else:
        if user_number > secret:
            print("Guess Lower")
            user_guesses = user_guesses + 1
        else:
             if user_number < secret:
                 print("Guess Higher")
                 user_guesses = user_guesses + 1

print("Right!")
# testing -- print(user_guesses)
if user_guesses == 1:
    print("Excellent")
else:
    if user_guesses >= 20:
        print("Bad")
    else:
        print("OK")



