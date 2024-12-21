# This simply detects usage of terms without context. For more advanced implementation, refer to test2.py

while(True):

    error = 0
    user_input = input("Enter the SQL Query : ").upper().split()
    user_input = list(user_input)
    print(user_input)

    for i in user_input:
        if i == "WHERE":
            error = 1
            print("Where found")
        elif i == 'IN':
            error = 1
            print("In found")
        elif i == '+':
            error = 1
            print("+ found")
        elif i.find(".JOIN") != -1:
            error = 1
            print("join operation found")

    print("Exit ? (Yes 1 / No 0) : ", end = "")
    x = int(input())
    
    
    if(x == 1): 
        break
    else:
        x = 0

print("Program Terminated!")