import aiml
# create kernel files and learn aiml files

kernel = aiml.Kernel()
kernel.learn("naumansbot.aiml")

while True:
    print(kernel.respond(input("HUMAN:  ")))
