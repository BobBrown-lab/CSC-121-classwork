#names.py

from name_function import get_formatted_name

print("enter 'q' at any time to quit")
while True:
    first = input("\nPlease enter your first name: ")
    if first == 'q':
        break
    last = input("\nPlease enter your last name: ")
    if last == 'q':
        break
    middle = input("\nPlease enter your middle name: ")
    if middle == 'q':
        break

    formatted_name = get_formatted_name(first, last, middle)
    print(f"\t\nNeatly formatted name: {formatted_name}")
