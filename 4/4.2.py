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

def check():
    total = 0 
    for n, row in enumerate(grid[:-2]): # n is row number
        for i in range(len(row) - 2): # i is column number
            if ((row[i] == 'M' and grid[n+1][i+1] == 'A' and grid[n+2][i+2] == 'S')\
            or  (row[i] == 'S' and grid[n+1][i+1] == 'A' and grid[n+2][i+2] == 'M'))\
            and((row[i+2] == 'M' and grid[n+1][i+1] == 'A' and grid[n+2][i] == 'S')\
            or  (row[i+2] == 'S' and grid[n+1][i+1] == 'A' and grid[n+2][i] == 'M')):
                #print(f"Row: {n}, Column: {i}")
                total += 1
    return total

print(check())