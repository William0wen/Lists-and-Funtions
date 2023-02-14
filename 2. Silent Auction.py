bid = 0
highest_bid = 0

# Item entry
item = input("Enter item to be bid upon: ")
reserve = float(input("Enter reserve price: $"))

print(f"The auction for the {item} has started!"
      f"\n(Enter -1 to stop bidding)")

# Bidding loop
while bid > -1:
    print(f"\nThe highest bid so far is ${highest_bid}")
    bid = float(input("What do you bid? $"))
    if bid <= highest_bid and bid != -1:
        print("Please enter a higher bid.")
    elif bid > highest_bid:
        highest_bid = bid

# Win/lose bid
if highest_bid < reserve:
    exit(f"\nYou didn't exceed the reserve price (${reserve}), therefore you lost the {item}.")
else:
    print(f"\nYou won the {item} for ${highest_bid}!")
