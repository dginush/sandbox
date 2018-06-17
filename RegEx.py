import re

with open('shakespeare_sonnet.txt', 'r') as infile:
    text = infile.read()
print(str(text))
m = re.findall(r'\b[\w\']+\b', str(text))
print(m)
