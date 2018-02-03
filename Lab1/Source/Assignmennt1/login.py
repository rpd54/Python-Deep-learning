#password checking function
def pwd_check(pwd):
    #preassigning required symbols
    SpecialSym=['$','@','#',' ']
    return_val=True
    #length of the password
    if len(pwd) <6:
        print('password should be more than  6 chars')
        return_val='Invalid'
    if len(pwd) >16:
        print('password should be less than 16 chars')
        return_val='Invalid'
    #Checking Numbers
    if not any(char.isdigit() for char in pwd):
        print(' password need to be 1 number atleast')
        return_val='Invalid'
    #Checking upper-case
    if not any(char.isupper() for char in pwd):
        print('password need to be atleast one uppercase-letter')
        return_val='Invalid'
    #checking lower-case
    if not any(char.islower() for char in pwd):
        print('password need to be  atleast one lowercase-letter')
        return_val='Invalid'
    #Checking symbols
    if not any(char in SpecialSym for char in pwd):
        print('password need to be at least one of the symbols $@#')
        return_val='Invalid'
    else:
        return_val='valid'
    #If all above conditions satisfies
    if return_val=='valid':
        print("congracts")
    return return_val

#taking input from the user
pwd = input('enter your password : ')
print(pwd_check(pwd))