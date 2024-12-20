import re

infile = open("3/input.txt", 'r')
intext = infile.read()

pattern = r"mul\(\d{1,3},\d{1,3}\)" # wow scary regex

mul_statements = re.findall(pattern, intext)

def mul(a, b):
    return a*b

total = 0

for statement in mul_statements:
    total += eval(statement)

print(total)