#10-6 Addition

while True:
    try:
        num_a = int(input("Please enter a number: "))
        break
    except ValueError:
        print("You have not entered a number. Please start again.")

while True:       
    try:    
        num_b = int(input("Please enter a second number: "))
        break
    except ValueError:
        print("You have not entered a number. Please start again.")
     
num_c = int(num_a + num_b)
print(num_c)
