from pathlib import Path

# path = Path('pi_digits.txt')
#contents = path.read_text()
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     #print(line)
#     pi_string += line
# print(pi_string)
# print(len(pi_string))    
# print(contents)

path = Path('programming.txt')
path.write_text("I love programming")
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)