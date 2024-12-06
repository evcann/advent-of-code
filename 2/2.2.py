from copy import deepcopy

infile = open("2/input.txt", 'r')
intext = infile.read()
text_lines = intext.splitlines()

def determine_safety(num_list):
    for i in range(len(num_list)):
        num_list_copy = deepcopy(num_list)
        num_list_copy.pop(i)

        ascending = False
        if num_list_copy[0] < num_list_copy[-1]:
            ascending = True
        elif num_list_copy[0] > num_list_copy[-1]:
            ascending = False
        else:
            continue # If the first and last number are the same, it automatically fails
        
        num_list_copy_sorted = sorted(num_list_copy, reverse = not ascending)

        if num_list_copy != num_list_copy_sorted: # Determine if all numbers are in order
            continue
        
        if len(num_list_copy) != len(list(set(num_list_copy))): # Check for duplicates
            continue

        failed = False

        for i, num in enumerate(num_list_copy[0:-1]): # Make sure all the differences are within [1,3]
            # [0:-1] ensures that we don't check the last number and get an out of range error
            if abs(int(num_list_copy[i + 1]) - int(num)) >= 1 and abs(int(num_list_copy[i + 1]) - int(num)) <= 3:
                continue
            else:
                failed = True
                continue
        if failed:
            continue
        return True # Return True if none of the tests failed
    return False # Return False if each combination of level removal failed
        
total_safe = 0

for line in text_lines:
    num_list = line.split(' ')
    num_list_ints = []
    for num in num_list:
        num_list_ints.append(int(num))

    if (determine_safety(num_list_ints)):
        total_safe += 1

print(total_safe)

