import re

infile = open("3/input.txt", 'r')
intext = infile.read()

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)" # wow scary regex

statements = re.findall(pattern, intext)

#print(statements)

def mul(a, b):
    return a*b

enabled = True
total = 0

for statement in statements:
    match (statement):
        case "do()":
            enabled = True
        case "don't()":
            enabled = False
        case _:
            if enabled:
                total += eval(statement)

print(total)