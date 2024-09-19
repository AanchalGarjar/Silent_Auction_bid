import os
def find_winner(bidder_details):
    highest_bid=0
    winner=""
    for bidders in bidder_details:
        bidding_price=bidder_details[bidders]
        if bidding_price>highest_bid:
            highest_bid=bidding_price
            winner=bidders
    print(f"The winner is {winner} with bid price {highest_bid}")

bidder={}
end_of_bidding=False
while not end_of_bidding:
    name=input("what is your name: ")
    price=int(input("what is your bid:"))
    bidder[name]=price
    more_bidder=input("Are there more bidder? type yes or no: ").lower()
    if more_bidder=='no':
        end_of_bidding=True
        find_winner(bidder)
    elif more_bidder=='yes':
        os.system('cls')