import art

# Title and logo
print("Welcome to the Blind Auction Program")
print(art.logo)

# Function to compare bids and determine highest bidder
def highest_bidder(bid_dictionary):
    # Blank winner and highest bid values that will update when function runs
    winner = ""
    highest_bid = 0

    #Update each bidder with bid amount to the dictionary
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]

        # If bid amount is higher than current highest bid, values get updated
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}.")


# Add user inputs into dictionary
bid_list = {}

# Sets loop condition
continue_bidding = True

# Runs through loop while condition is true
while continue_bidding:
    # Ask for user inputs
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? $"))

    # Add user inputs into dictionary
    bid_list[user_name] = user_bid

    # Checks for new users and whether loop condition remains the same
    new_bidder = input("Is there another bidder? Type 'yes' or 'no'. ").lower()

    # If condition changes to no, function to determine highest bidder runs
    if new_bidder == "no":
        continue_bidding = False
        highest_bidder(bid_list)

    # If conditions stays the same, 20 new lines show to "clear the screen" (*need to learn better way of doing this*)
    elif new_bidder == "yes":
        print("\n" * 20)
