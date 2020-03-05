import aiml

newusername = ""
def register():
    global newusername
    newusername = input("Enter your username: ")
    password = input("Enter password: ")
    email = input("Enter Email: ")
    contact = input("Enter PhoneNumber: ")
    file = open("username and password.txt", "a")
    file.write(newusername)
    file.write(" ")
    file.write(password)
    file.write(" ")
    file.write(email)
    file.write(" ")
    file.write(contact)
    file.write("\n")
    file.close()
    print("\nAccount Created Successfully!\n")


fname = ""


def checklogin():
    global fname
    print("Enter Username And Password! \n")
    fname = input("username : ")
    password = input("password : ")

    for line in open("username and password.txt", "r").readlines():
        info = line.split()
        if info[0] == fname and info[1] == password:
            print("\nLogin Successful\n")
            return True
    print("\nYou seem like a new user ! Register to continue!")
    return False


def learnBot(username):
    kernel = aiml.Kernel()
    kernel.learn("naumansbot.aiml")
    kernel.setPredicate("fname", username)
    print("\nSay Hi\n")
    while True:
        print(kernel.respond(input("Human: ")))

def startChat():
    if checklogin() == True:
        learnBot(fname)
    else:
        register()
        learnBot(newusername)


startChat()