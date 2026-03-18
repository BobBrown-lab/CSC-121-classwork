num_tickets = int(input("How many tickets do you want to buy? "))
print("\n")
#num_tickets = 5
#get ages of ticket holders
ages = []
for age in range(num_tickets):
    age = int(input("Enter the age of the person for this ticket: "))
    ages.append(age)

subtot = int() #variable to hold the subtotal of the ticket costs 

for age in ages:
    if age < 3:
        subtot += 0
    elif age <= 12:
        subtot += 10
    else:
        subtot += 15

#total = subtotal
print("\n")

print(f"The total cost of your tickets is ${subtot}.")