print("...rock...")
print("...paper...")
print("...scissors...")
p1 = input("Player 1, enter your selection: ")
p2 = input("Player 2, enter your selection: ")

if p1 == "rock":
    if p2 == "rock":
        print("DRAW")
    elif p2 == "paper":
        print("Paper beats rock.")
        print("Player 2 wins!")
    elif p2 == "scissors":
        print("Rock beats scissors.")
        print("Player 1 wins!")
    else:
        print("ERROR: Player 2 did not enter a valid response.")
        print(f"Player 2 entry: {p2}")
elif p1 == "paper":
    if p2 == "rock":
        print("Paper beats rock.")
        print("Player 1 wins!")
    elif p2 == "paper":
        print("DRAW")
    elif p2 == "scissors":
        print("Scissors beat paper.")
        print("Player 2 wins!")
    else:
        print("ERROR: Player 2 did not enter a valid response.")
        print(f"Player 2 entry: {p2}")
elif p1 == "scissors":
    if p2 == "rock":
        print("Rock beats scissors.")
        print("Player 2 wins!")
    elif p2 == "paper":
        print("Scissors beat paper.")
        print("Player 1 wins!")
    elif p2 == "scissors":
        print("DRAW")
    else:
        print("ERROR: Player 2 did not enter a valid response.")
        print(f"Player 2 entry: {p2}")
else:
    print("ERROR: Player 1 did not enter a valid response.")
    print(f"Player 1 entry: {p1}")
