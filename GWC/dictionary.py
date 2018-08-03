#peeps = {"Yu Ling":"55", "Wei Jun":"54","Melanie":"17","Ivy":"16","Kevin":"17","Natalie":"16","Christina":"17","Nicole":"19","Carmen":"12", "Marivi":"20"}
#print(peeps)


##pineapplePizza = input("Pineapple on pizza, yes or no?")
##
##obama = input("What is Obama's last name?")
##
##duck = input("WOULD YOU RATHER FIGHT 100 DUCK SIZED HORSES OR 1 HORSE SIZED DUCK?")
##
##name = input("What is the least sexiest name?")
##
##strength = input("If I punch myself and it hurts, am I weak or am I strong?")
##
##body = input("Which body part do you wish you could detach?")
##
##toiletPaper = input("Do you prefer your toilet paper under or over?")
##
##cereal = input("Do you pour your milk first or your cereal?")
##
##surveyAnswers = {"pineapplePizza":pineapplePizza, "obama":obama,"duck":duck,"name":name,"strength":strength,"body":body,"toiletPaper":toiletPaper,"cereal":cereal}
##
##print(surveyAnswers)
import json


questions=["What is your name?","Pineapple on pizza, yes or no?","What is Obama's last name?",
           "WOULD YOU RATHER FIGHT 100 DUCK SIZED HORSES OR 1 HORSE SIZED DUCK?","What is the least sexiest name?",
           "If I punch myself and it hurts, am I weak or am I strong?","Which body part do you wish you could detach?",
           "Do you prefer your toilet paper under or over?","Do you pour your milk first or your cereal?"]
keys=["yourName","pineapplePizza","obama","duck","name","strength","body","toiletPaper","cereal"]

answerList = []

done = "No"
while done == "No":

    #create the dictionary to store answers
    answers={}
    print("New entry! Please answer the questions below.")

    #iterate over the list of questions and take in answers
    for i in range(len(keys)):
        answer = input(questions[i] +": ")
        answers[keys[i]] = answer
    
    answerList.append(answers)

    done= input("Are you done taking the survey? Type 'Yes' or 'No'.").upper()

#print list of dictionaries
print(answerList)    

f = open("allanswers.json","w")
f.write('[\n')
json.dump(answerList[0],f)
f.write('\n]')
f.close()

