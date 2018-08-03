#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
f = open("dictionary.txt","r")


print("Can your password survive a dictionary attack?")

my_list = []
for line in f:
    my_list.append(line.strip())


#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords 
var = "bad"

while var == "bad":
    test_password = input("[Type in a trial password]: ")

    x = test_password.split(" ")
    for password in x:
        password = password.lower()

        if len(password) < 6:
            print("[Password is too short! Try again.]")
        elif len(password) > 6:
            print("[Password length ok.]")
            if password in my_list:
                print("'" + password + "'" + " is too weak! Try again!")
            else:
                print("[You have entered a strong password.]")
                var = "good"
    
 


    

#Write logic to see if the password is in the dictionary file below here:
