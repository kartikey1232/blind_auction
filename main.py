# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


bidders={}
max=""
while(True):
    name=input("What is your name?\n")
    max=name
    bid=int(input("What is your bid?\n"))
    bidders[name]=bid
    if input("Are there any more bidders?\n").lower()=="yes":
        continue
    else:
        break

for key in bidders:
    if bidders[max] < bidders[key]:
        max=key
    else:
        continue
print(f"The winner is {max} with a bid of ${bidders[max]}")

