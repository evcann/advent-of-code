infile = open("8/input.txt")
intext = infile.read()

grid = []
for line in intext.splitlines():
    grid.append(list(line))

antenna_locations = {}

for x, line in enumerate(grid):
    for y, character in enumerate(line):
        if character != '.':
            if character not in antenna_locations:
                antenna_locations[character] = [(x, y)]
            else:
                antenna_locations[character].append((x, y))

antinode_locations = []

x_bound = range(len(grid[0]))
y_bound = range(len(grid))

for antenna_type in antenna_locations:
    for antenna in antenna_locations[antenna_type]:
        for other_antenna in antenna_locations[antenna_type]:
            if other_antenna == antenna: continue # Skip if it's the same one

            # antenna[0] is the x position of the current antenna
            # antenna[1] is the y position of the current antenna

            x_dist = antenna[0] - other_antenna[0]
            y_dist = antenna[1] - other_antenna[1]

            x_temp = antenna[0]
            y_temp = antenna[1]

            while x_temp in x_bound and y_temp in y_bound:
                antinode_locations.append((x_temp, y_temp))
                x_temp += x_dist
                y_temp += y_dist


print(len(set(antinode_locations)))