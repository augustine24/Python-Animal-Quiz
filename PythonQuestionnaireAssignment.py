import time
 
correct = 0
#The variable correct is going to tell the user how many questions they've got right
print("Hello there! Please insert your name.")
name = input()
#The hello message is printed and shown to the user to start the AI to user interaction. The name = input message lets the user enter their name.
print(name,"? That's a strange name.")
time.sleep(1.0)
#The time.sleep function allows for the user to have a second to read before going over the next line that the AI will tell them.
print("Well, "  + name, "welcome to the Animal Python Quiz! I've got some problems for you that I'd like you to solve.")
time.sleep(1.0)
print("Are you ready for this quiz?")
time.sleep(1.0)
print("Please type yes or no, depending on if you're ready for this quiz.")
answer = input("")
if answer == "yes":
    print("Great! Let's proceed.")
else: 
    print("Take your time and prepare. Please restart the terminal when you're ready.")
#This if/else conditional will be used to determine what happens in this coding project, based on what the user replies to questionss.
#This will be seen further in the coding a lot.
if answer == "yes":
    print("Alright! Question one! Are lions from the canine animal family? Type yes or no as an answer.")
answer = input("")
#answer is continuously redefined and used so that the response over time to its input can change, along with the conditions of a yes or no response.
if answer == "yes":
    correct += 0
    print("That is incorrect. You have gotten" ,correct, "question(s) right so far.")
if answer == "no":
    correct += 1
    print("Correct! Lions are from the feline animal family. You have gotten"  ,correct, "question(s) right so far.")
time.sleep(1.0)
print("Question two! Is the fastest animal on the planet the cheetah? Type yes or no as an answer.")
answer = input("")
if answer == "yes":
    correct += 0
#The correct variable is going to consistently have values added to it's prior total using +=, 
#allowing us to keep record of how many questions are right based on answers given.
    print("That is incorrect. You have gotten" ,correct, "question(s) right so far.")
if answer == "no":
    correct += 1
    print("Correct! The fastest animal on the planet is the peregrine falcon. You have gotten" ,correct, "question(s) right so far.")
time.sleep(1.0)
print("Question three! Are birds considered related to dinosaurs? Type yes or no as an answer.")
answer = input("")
if answer == "yes":
    correct += 1
    print("Correct! Birds are considered to be the relatives of dinosaurs! You have gotten" ,correct, "question(s) right so far.")
if answer == "no":
    correct += 0
    print("That is incorrect. You have gotten" ,correct, "question(s) correct so far.")
time.sleep(1.0)
print("Question four! Are spiders considered insects? Type yes or no as an answer.")
answer = input("")
if answer == "yes":
    correct += 0
    print("That is incorrect. You have gotten" ,correct, "question(s) right so far.")
if answer == "no":
    correct += 1
    print("Correct! Spiders are arachnids, which are technically not insects. You have gotten" ,correct, "question(s) right so far.")
time.sleep(1.0)
print("Final question! Are all mammals warm blooded? Type yes or no as an answer.")
answer = input("")
if answer == "yes":
    correct += 1
    print("Correct! You have completed the quiz with" ,correct, "answer(s) correct.")
if answer == "no":
    correct += 0
    print("Incorrect. You have completed the quiz with" ,correct, "answer(s) correct.")
time.sleep(1.0)
if correct >= 2.5:
    print("You have passed the quiz!")
if correct >= 4:
    print("You have passed the quiz with flying colours!")
if correct < 2.5: 
    print("You have failed the quiz.")
print("Thank you for playing," ,name,"!")







