import re
information_cv = "(Bot) We work with you on writing/reviewing existing job descriptions for recruitment candidates from diverse backgrounds, we will review existing pipelines and give constructive ways to improve your strategy."
information_interview = "(Bot) We provide practice for 1-on-1 mock interviews, using techniques such as the S.T.A.R model."
information_network = "(Bot) SkillStruct University is the name of our virtual network, it is a people platform that provides young, motivated people with a place to learn, feel empowered, and gain access to key tools to help them navigate the industry by utilising technology."

#Key_words responses
cv = {"book":"(Bot) You can book a cv reading at https://skillstruct.com/contact/",\
"booking": "(Bot) You can book a cv reading at https://skillstruct.com/contact/",\
"information": information_cv,\
"templates": "(Bot) You can find the free CV template at https://skillstruct.com/skillstruct-presents/",\
"template": "(Bot) You can find the free CV template at https://skillstruct.com/skillstruct-presents/",\
"help":"(Bot) You can book a cv reading at https://skillstruct.com/contact/"}

interview = {"book": "(Bot) You can book interview assistance at https://skillstruct.com/contact/ ",\
"booking": "(Bot) You can book interview assistance at https://skillstruct.com/contact/ ",\
"information": information_interview}

network = {"information": information_network,\
"join": "(Bot) To join the SkillStruct University network then fill out the contact form at https://skillstruct.com/join-the-network/",\
"about": information_network}

tutoring = {"career": "(Bot) In addition to the editable CV/Cover letter Templates, you will get access to the STAR model starter guide, job tracker template and much more!",\
"dissertation": "(Bot) We give you a starter pack to help you on your dissertation journey, including a project map and a dissertation PPT template.",\
"dissertations": "(Bot) We give you a starter pack to help you on your dissertation journey, including a project map and a dissertation PPT template.",\
"finance": "(Bot) Interested in financial literacy? Based on our blog The Marathon (https://skillstruct.com/2019/09/29/the-marathon/), we’ve created a folder with useful docs on finance.",\
"coding": "(Bot) We have resources to help you with, coding, agile and much more!",\
"computer": "(Bot) We have resources to help you with , coding, agile and much more!",\
"language": "(Bot) We have a few Spanish enthusiasts on the network and as a result, we’ve created a folder that includes beginner audio/docs to begin your Spanish journey. Test out your Spanish by reading this blog (https://skillstruct.com/2019/06/17/aprender-ingles-a-la-manera-skillstruct/)."}

events = {"project": "(Bot) To get notified when the free online virtual sessions about how to be effective when it comes to your final year project, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"projects": "(Bot) To get notified when the free online virtual sessions about how to be effective when it comes to your final year project, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"employability": "(Bot) To get notified when the free online virtual sessions about employability fundamentals, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"linkedin": "(Bot) To get notified when the free online virtual sessions about LinkedIn fundamentals, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"microsoft": "(Bot) To get notified when the free online virtual sessions about Microsoft Teams fundamentals, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"industry": "(Bot) To get notified when the free online virtual sessions about breaking down the tech industry, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"interview": "(Bot) To get notified when the free online virtual sessions about how to answer interview questions effectively, fill out the sign-up form at https://skillstruct.com/join-the-network/",\
"interviews": "(Bot) To get notified when the free online virtual sessions about how to answer interview questions effectively, fill out the sign-up form at https://skillstruct.com/join-the-network/"}

leave = {}

key_words = {"cv": cv, "interviews": interview, "interview": interview, "tutoring": tutoring, "events": events, "event": events, "university": network, "network" : network, "no": leave, "stop": leave, "end": leave, "leave": leave, "quit": leave, "exit": leave}

def scan(input, dicty):
    if type(input) == list:
        split_message = input
    else:
        split_message = re.split(r'\s+|[,.;:?-]\s*', input)
    for i in split_message:
        i = i.lower()
        for j in dicty.keys():
            if i == j:
                if type(dicty.get(i)) == dict:
                    return scan(split_message, dicty.get(i))
                else:
                    return dicty.get(i)
    return stuck(dicty)

def stuck(dicty):   
    for i in dir():
        if eval(i) == key_words:
            return ['(Bot) How can I help you?', key_words]
        elif eval(i) == interview:
            return ["(Bot) I understand you're asking a question about interviews, please try using one of our keywords:\n-Booking\n-Information", interview]
        elif eval(i) == network:
            return ["(Bot) I understand you're asking a question about the SkillStruct University network, please try using one of our keywords:\n-Join\n-Information\n-About", network]
        elif eval(i) == cv:
            return ["(Bot) I understand you're asking a question about CVs, please try using one of our keywords:\n-Booking\n-Information\n-Help", cv]
        elif eval(i) == events:
            return ['(Bot) Which event would you like to know about? Your options are:\n-Final year projects\n-Breaking down the Tech Industry\n-How to be effective in interviews\n-Employability Fundamentals\n-LinkedIn Fundamentals\n-Microsoft Teams Fundamentals', events]
        elif eval(i) == tutoring:
            return ['(Bot) What subject do you need help with? Your options are:\n-Career Content\n-Dissertations\n-Finance\n-Computer Science\n-Learning a new language', tutoring]
        elif eval(i) == leave:
            print("(Bot) Goodbye!")
            quit()

print("(Bot) Hello, welcome to the SkillStruct chatbot, how can I help you today?")
current_dict = key_words
while True:
    reset = False
    user_input = input("(User) ")
    split_message = re.split(r'\s+|[,.;:?-]\s*', user_input)
    for i in split_message:
        i = i.lower()
        if (i in set(key_words.keys())) & (i != "interview") & (i != "interviews") & (current_dict != events):
            if type(scan(user_input, key_words)) == list:
                print(scan(user_input, key_words)[0])
                reset = True
                current_dict = scan(user_input, key_words)[1]
                break
            else:
                print(scan(user_input, key_words))
                reset = True
                current_dict = key_words
                print("(Bot) Is there anything else I can help with?")
                break
    if reset == True:
        continue
    if type(scan(user_input, current_dict)) == list:
        print(scan(user_input, current_dict)[0])
        current_dict = scan(user_input, current_dict)[1]
    else:
        print(scan(user_input, current_dict))
        current_dict = key_words
        print("(Bot) Is there anything else I can help with?")
    