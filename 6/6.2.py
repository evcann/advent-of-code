from time import sleep

infile = open("6/input.txt", 'r')
intext = infile.read()
rows = intext.splitlines()

grid = []

def reset_grid():
    grid.clear()
    for row in rows:
        grid.append(list(row))

reset_grid()

def get_starting_position():
    x, y = 0, 0
    for y, row in enumerate(grid):
        if '^' in row:
            x = row.index('^')
            break
    return [x,y]

first_path = []

position = get_starting_position()
direction = 'U'

while True:
    try:
        first_path.append(tuple(position))
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

first_path = [i for i in first_path if i != get_starting_position()]
stuck_tiles = 0

temp_path = []

for tile in set(first_path):
    reset_grid()
    position = get_starting_position()
    direction = 'U'
    grid[tile[1]][tile[0]] = '#'
    temp_path.clear()

    #print(f"TILE: {tile}")
    while True:
        #if tile == (6,7): print(position); print(direction)
        #sleep(0.1)

        temp_path.append(tuple(position))
        if len(temp_path) == 10_000:
            stuck_tiles += 1
            break
        match (direction):
            case 'U':
                if grid[position[1] - 1][position[0]] == '#':
                    direction = 'R'
                elif position[1] == 0:
                    break
                else:
                    position[1] -= 1
            case 'R':
                if position[0] == len(grid[0]) - 1:
                    break
                elif grid[position[1]][position[0] + 1] == '#':
                    direction = 'D'
                else:
                    position[0] += 1
            case 'D':
                if position[1] == len(grid) - 1:
                    break
                elif grid[position[1] + 1][position[0]] == '#':
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
    
print(stuck_tiles)