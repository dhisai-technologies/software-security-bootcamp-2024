import re

# Regex pattern for string joining operations
string_joining_pattern = r'(?<=\w)\s*[\+\.\&]\s*(?=\w)'

# Regex pattern for list comprehension in queries
list_comprehension_pattern = r'\[\s*.*\s*for\s+\w+\s+in\s+\w+\s*(if\s+.*)?\]'

# Regex pattern for dynamic WHERE usage
dynamic_where_pattern = r'(?i)\bWHERE\b\s+.*?(\w+\s*=\s*.*?|\w+\s*IN\s*\(.*?\))'

while(True):

    user_input = input("\nEnter the SQL Query : ")
    print(user_input)

    # Search for the pattern
    match_1 = re.search(string_joining_pattern, user_input)
    
    if match_1:
        print("\nString joining operation found:", match_1.group())
    else:
        print("\nNo string joining operation found.")

    # Search for the pattern
    match_2 = re.search(list_comprehension_pattern, user_input)
    if match_2:
        print("\nList comprehension found:", match_2.group())
    else:
        print("\nNo list comprehension found.")

    # Search for the pattern
    match_3 = re.search(dynamic_where_pattern, user_input)
    if match_3:
        print("\nDynamic WHERE usage found:", match_3.group())
    else:
        print("\nNo dynamic WHERE usage found.")


    print("\nExit ? (Yes 1 / No 0) : ", end = "")
    x = int(input())
    
    
    if(x == 1): 
        break
    else:
        x = 0

print("Program Terminated!")
