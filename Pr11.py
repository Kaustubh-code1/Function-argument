# Function to check input aannnnddd, umm... do some other stuff as well :D
def ShutDown(inputinfo):
    if inputinfo=="Yes":
        print("Shutting down.")
    elif inputinfo=="No":
        print("Shutdown cancelled.")
    else:
        print("Sorry, please enter in form of 'Yes' or 'No'.")
command=str(input("Do you want to initiate Shut Down? "))
ShutDown(command)