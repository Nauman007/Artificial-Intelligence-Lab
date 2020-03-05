import aiml

kernel = aiml.Kernel()

# setting value before conservation starts
# playing with variables

name = input("Enter your name please: ")
kernel.learn("naumansbot.aiml")
kernel.setPredicate("fname", name)
print("\nSay Hi\n")

while True:
    print(kernel.respond(input("Human: ")))
