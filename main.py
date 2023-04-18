from replit import clear
from art import logo
# Create an empty dictionary
bids = {}

def find_highest_bid(data):
	# data = {"izza": 123, "karina": 321}
	highest = 0
	# Loop through dictionary
	for bid_data in data: # untuk semua key di data; 1."izza"; 2."karina"
		bid_amount = data[bid_data] # bid_amount = data["izza"] = 123
		if highest < bid_amount:
			highest = bid_amount
	print(f"The highest bid is {bid_data}: {highest} ")
		
continue_game = True
while continue_game:
	print(logo)
	name = input("What's your name? ")
	bid = int(input("Bid price: $"))
	# Add new value to dictionary
	bids[name] = bid
	
	user = input("Are there any other bidders who want to bid. Type 'y' or 'n'\n")
	if user == 'y':
		clear()
	else:
		continue_game = False
		find_highest_bid(bids)		
