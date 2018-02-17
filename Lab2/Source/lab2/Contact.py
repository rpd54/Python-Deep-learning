#List of Contacts in the user contact list stored in list with each contact in directory
cntct_list = [{"name":'Rakesh', "number":3467173853, "email":"p.rakesh153@gmail.com"},
                {"name":"John", "number":8167262175, "email":"john@gmail.com"},
                {"name":"Mary","number":8165762435,"email":"mary@gmail.com"}]

#forming a switch statement indirectly for giving an options to the user
while True:
    #User need to Select an Input from list
    print('''Hi, Get any contact details form Telephone-Directory:
                1.) Get by name 
                2.) Get by contact-No:
                3.) Update Contact details
                4.) Exit
                ''')
    choice = input("Select an option: ")
    #Extracting the contact details by prompting name given by user
    if choice == "1":
        nm = input("Enter name to get contact: ")
        for i in cntct_list:
            if nm in i.values():
                print(i)
    # Extracting the contact details by prompting phone number given by user
    elif choice == "2":
        num = int(input("enter contact: "))
        for j in cntct_list:
            if num in j.values():
                print(j)
    # Updating the contact details by prompting name given by user
    elif choice == "3":
        nme = input("enter name to edit:")
        for k in cntct_list:
            if nme in k.values():
                print(k)
                newnum = int(input("enter number to edit"))
                #inserting new number given by user
                k["number"] = newnum
                print(k)
    elif choice == "4":
        #to exit from the loop
        print("Program quit!")
        break
    else:
        #invalid Inputs for string or other nos
        print("Invalid Input! Try again.")
        break
