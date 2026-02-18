guests = ["hedy","ludwig","jack","don"]
guests.append("den")
guests.insert(0,"tom")
guests.insert(2,"bill")
guests.sort()

print ("The first three items on the list are:")
print(guests[0:3])

print ("\nThree items from the middle of the the list are:")
print (guests[2:5])

print("\nThe last three items on the list are:")
print (guests[4:7])