import time
 
correct = 0
print("Hello there! Please insert your name.")
name = input()
print(name,"? That's a strange name.")
time.sleep(0.7)
print("Well, "  + name, "welcome to the Animal Python Quiz! I've got some problems for you that I'd like you to solve.")
time.sleep(0.8)
print("Are you ready for this quiz?")
time.sleep(1.0)
print("Please type yes or no, depending on if you're ready for this quiz.")
answer = input("")
if answer == "yes":
    print("Great! Let's proceed.")
else: 
    print("Take your time and prepare. Please restart the terminal when you're ready.")
if answer == "yes":
    print("Alright! Question one! Are lions from the canine animal family? Type yes or no as an answer.")
answer = input("")
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
print("Final question! Are all mammals warm blooded? Type yes or no as an answer.")
answer = input("")
if answer == "yes":
    correct += 1
    print("Correct! You have completed the quiz with" ,correct, "answer(s) correct.")
if answer == "no":
    correct += 0
    print("Incorrect. You have completed the quiz with" ,correct, "answer(s) correct.")
print("Thank you for playing," ,name,"!")







