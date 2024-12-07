infile = open("2/input.txt", 'r')
intext = infile.read()
text_lines = intext.splitlines()

def determine_safety(num_list):
    ascending = False
    if num_list[0] < num_list[-1]:
        ascending = True
    else:
        return False # If the first and last number are the same, it automatically fails
    
    num_list_sorted = sorted(num_list, reverse = not ascending)

    if num_list != num_list_sorted: # Determine if all numbers are in order
        return False
    
    if len(num_list) != len(list(set(num_list))): # Check for duplicates
        return False

    for i, num in enumerate(num_list[0:-1]): # Make sure all the differences are within [1,3]
        # [0:-1] ensures that we don't check the last number and get an out of range error
        if abs(int(num_list[i + 1]) - int(num)) >= 1 and abs(int(num_list[i + 1]) - int(num)) <= 3:
            continue
        else:
            return False
        
    return True # Return true if none of the tests failed
        
total_safe = 0

for line in text_lines:
    num_list = line.split(' ')
    num_list_ints = []
    for num in num_list:
        num_list_ints.append(int(num))

    if (determine_safety(num_list_ints)):
        total_safe += 1

print(f"Part 1: {total_safe}")

