query1 = input('Enter the query: ')
defaultsubtr = '"SELECT * FROM users WHERE username ='
msg = 'Potential SQL Injection Vulnerabilities:'
msg_printed = False 

def fstring_detector(q):
    global msg_printed
    if q[0] == 'f' and defaultsubtr in q:
        if not msg_printed:
            print(msg)
            msg_printed = True
        print('f-string detected!!')
        return 1

def fomat_detector(q):
    global msg_printed
    prob = '%s'
    if q.count(prob) > 0:
        if not msg_printed:
            print(msg)
            msg_printed = True
        print('%-formatting string detected!!')
        return 1

def format_fun(q):
    global msg_printed
    prob = '.format'
    if prob in q:
        if not msg_printed:
            print(msg)
            msg_printed = True
        print('.format() method used')
        return 1

fstring_detector(query1)
fomat_detector(query1)
format_fun(query1)
