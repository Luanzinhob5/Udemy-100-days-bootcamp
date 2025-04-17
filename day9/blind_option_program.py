audiction = {}
other_bid = "yes"

def dictionary_add(key, value):
    audiction[key] = value

def find_highest_bidder():
    highest_bid = 0
    for bid in audiction:
        if audiction[bid] > highest_bid:
            highest_bid = audiction[bid]
            winner = bid
    
    print(f"The winner is {winner}")
        

while other_bid.lower() == 'yes':
    name = input('Your name:  ')
    bid_price = int(input('Your bid: $'))

    dictionary_add(key = name, value = bid_price)

    other_bid = input('Have another bid "yes" or "no"\n')
    print("\n" * 40)

find_highest_bidder()