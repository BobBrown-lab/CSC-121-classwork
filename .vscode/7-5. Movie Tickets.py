# Get number of tickets

num_tickets = int(input("How many tickets do you want to buy? "))
    
tier_1 = int(input("How many tickets for children under 3? "))
tier_2 = int(input("How many tickets for children between 3 and 12? "))
tier_3 = int(input("How many tickets for those over 12? "))

total = (tier_2*10) + (tier_3*15)

print(f"The total cost of your tickets is ${total}.")