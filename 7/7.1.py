from itertools import product

infile = open("7/input.txt", 'r')
intext = infile.read()

results = []

for line in intext.splitlines():
    results.append(int(line.split(':')[0]))

expressions = []

for line in intext.splitlines():
    temp = []
    for num in line.split(':')[1].split():
        temp.append(int(num))
    expressions.append(temp)

def get_operator_combinations(input_count):
    input_count -= 1 # Three inputs means two operators (ex. 81 _ 41 _ 27)
    operator_types = "+*"
    return tuple(product(operator_types, repeat = input_count))

total = 0

for n in range(len(results)):
    for operator_combo in get_operator_combinations(len(expressions[n])):
        temp_result = expressions[n][0]
        for j, operator in enumerate(operator_combo):
            match (operator):
                case '+':
                    temp_result += expressions[n][j + 1]
                case '*':
                    temp_result *= expressions[n][j + 1]
        if temp_result == results[n]:
            total += results[n]
            break

print(total)