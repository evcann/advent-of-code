infile = open("5/input.txt", 'r')
intext = infile.read()

rules_unparsed, updates_unparsed = intext.split(sep="\n\n")[0].splitlines(), intext.split(sep="\n\n")[1].splitlines()

rules = []
for rule in rules_unparsed:
    pair_strings = tuple(rule.split("|"))
    pair = (int(pair_strings[0]), int(pair_strings[1]))
    rules.append(pair)

updates = []
for update in updates_unparsed:
    string_list = update.split(',')
    updates.append(list(map(int, string_list)))

passed_updates = []

for update in updates:
    passed = True # Default state is passing, set to false when a rule is violated
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not (update.index(rule[0]) < update.index(rule[1])):
                passed = False
                break
    if passed:
        passed_updates.append(update)

total = 0

for update in passed_updates:
    middle = update[(len(update) // 2)]
    total += middle

print(total)