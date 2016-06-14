time = 1
while time <=2:
    game = input("Play a game? ")
    if time == 1:
        if game != "chess":
            print("Prefer chess?")
            time = time + 1
    else:
        if game == "chess":
            print("Battle Chess")
            time = time + 1
        else:
            print("fine")
            time = time + 1
