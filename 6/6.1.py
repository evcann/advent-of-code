infile = open("6/input.txt", 'r')
intext = infile.read()
rows = intext.splitlines()

grid = []

for row in rows:
    grid.append(list(row))

def get_starting_position():
    x, y = 0, 0
    for y, row in enumerate(grid):
        if '^' in row:
            x = row.index('^')
            break
    return [x,y]

visited_locations = []

position = get_starting_position()
direction = 'U'

while True:
    try:
        visited_locations.append(tuple(position))
        match (direction):
            case 'U':
                if grid[position[1] - 1][position[0]] == '#':
                    direction = 'R'
                elif position[1] == 0:
                    break
                else:
                    position[1] -= 1
            case 'R':
                if position[0] == len(grid[0]):
                    break
                elif grid[position[1]][position[0] + 1] == '#':
                    direction = 'D'
                else:
                    position[0] += 1
            case 'D':
                if grid[position[1] + 1][position[0]] == '#':
                    direction = 'L'
                else:
                    position[1] += 1
            case 'L':
                if position[0] == 0:
                    break
                elif grid[position[1]][position[0] - 1] == '#':
                    direction = 'U'
                else:
                    position[0] -= 1
    except IndexError:
        break

print(len(set(visited_locations)))