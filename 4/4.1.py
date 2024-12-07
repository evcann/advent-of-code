infile = open("4/input.txt", 'r')
intext = infile.read()
rows = intext.splitlines()

grid = []

#print(rows)

for row in rows:
    row_list = []
    for letter in list(row):
        row_list.append(letter)
    grid.append(row_list)

def check(type):
    total_for_type = 0
    match (type):
        case 'lr': # Left to right
            for n, row in enumerate(grid): # n is row number
                for i in range(len(row) - 3): # i is column number
                    if (row[i] == 'X' and row[i+1] == 'M' and row[i+2] == 'A' and row[i+3] == 'S') \
                    or (row[i] == 'S' and row[i+1] == 'A' and row[i+2] == 'M' and row[i+3] == 'X'):
                        total_for_type += 1

        case 'du': # Down to up
            for n, row in enumerate(grid[:-3]):
                for i in range(len(row)):
                    if (row[i] == 'X' and grid[n+1][i] == 'M' and grid[n+2][i] == 'A' and grid[n+3][i] == 'S')\
                    or (row[i] == 'S' and grid[n+1][i] == 'A' and grid[n+2][i] == 'M' and grid[n+3][i] == 'X'):
                        total_for_type += 1
        
        case 'ul-dr': # Up left to down right
            for n, row in enumerate(grid[:-3]):
                for i in range(len(row) - 3):
                    if (row[i] == 'X' and grid[n+1][i+1] == 'M' and grid[n+2][i+2] == 'A' and grid[n+3][i+3] == 'S')\
                    or (row[i] == 'S' and grid[n+1][i+1] == 'A' and grid[n+2][i+2] == 'M' and grid[n+3][i+3] == 'X'):
                        total_for_type += 1
        
        case 'ur-dl': # Up right to down left
            for n, row in enumerate(grid[:-3]):
                for i in range(3, len(row)):
                    if (row[i] == 'X' and grid[n+1][i-1] == 'M' and grid[n+2][i-2] == 'A' and grid[n+3][i-3] == 'S')\
                    or (row[i] == 'S' and grid[n+1][i-1] == 'A' and grid[n+2][i-2] == 'M' and grid[n+3][i-3] == 'X'):
                        total_for_type += 1

    return total_for_type

#print(check('ur-dl'))

def add_up_all():
    types = ('lr', 'du', 'ul-dr', 'ur-dl')
    sum = 0
    for type in types:
        sum += check(type)
    return sum

print(add_up_all())