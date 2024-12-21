# Same as test2.py. Here reads from file instead of from the user

import re

# Regex pattern for string joining operations
string_joining_pattern = r'(?<=\w)\s*[\+\.\&]\s*(?=\w)'

# Regex pattern for list comprehension in queries
list_comprehension_pattern = r'\[\s*.*\s*for\s+\w+\s+in\s+\w+\s*(if\s+.*)?\]'

# Regex pattern for dynamic WHERE usage
dynamic_where_pattern = r'(?i)\bWHERE\b\s+.*?(\w+\s*=\s*.*?|\w+\s*IN\s*\(.*?\))'

count = 0
error = 0
print("\nError on lines : ", end = "")

# Read input from the file line by line
with open('test cases.txt', 'r') as file:
    for user_input in file:  # Iterate over each line in the file
        count += 1
        error = 0
        # print("")
        # print(user_input.strip())  # Print the line without leading/trailing whitespace

        # Search for the pattern
        match_1 = re.search(string_joining_pattern, user_input)
    
        if match_1:
            # print("\nString joining operation found:", match_1.group())
            error = 1
        # else:
            # print("\nNo string joining operation found.")

        # Search for the pattern
        match_2 = re.search(list_comprehension_pattern, user_input)
        if match_2:
            error = 1
            # print("\nList comprehension found:", match_2.group())
        # else:
        #     print("\nNo list comprehension found.")

        # Search for the pattern
        match_3 = re.search(dynamic_where_pattern, user_input)
        if match_3:
            error = 1
            # print("\nDynamic WHERE usage found:", match_3.group())
        # else:
        #     print("\nNo dynamic WHERE usage found.")

        if error == 1:
            print(count, end = " ")

print("\nProgram Terminated!")