#check user choice is interger, text or image
def user_choice():

    valid = False
    while not valid: 
        
        response = input("file type (interger / text / image): ").lower()

        if response == "text" or response == "t":
            return response

        else:
            print("please choose valid file")
            print() 

#main routine
data_type = user_choice
print("you chose", data_type)
print()