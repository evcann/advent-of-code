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
    int_list = []
    for string in string_list:
        int_list.append(int(string))
    updates.append(int_list)

def check(update):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if not (update.index(rule[0]) < update.index(rule[1])):
                return False
    return True

passed_updates = []
failed_updates = []

for update in updates:
    passed = True # Default state is passing, set to false when a rule is violated
    for rule in rules:
        if rule[0] in update and rule[1] in update: # Disregard rule if it doesn't apply
            if not (update.index(rule[0]) < update.index(rule[1])):
                passed = False
                break
    if passed:
        passed_updates.append(update)
    else:
        failed_updates.append(update)

total = 0

for update in failed_updates:
    while not check(update):
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                if not (update.index(rule[0]) < update.index(rule[1])):
                    update.remove(rule[0])
                    i = update.index(rule[1])
                    update.insert(i, rule[0])

    middle = update[len(update) // 2]
    total += middle

print(total)