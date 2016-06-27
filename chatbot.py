
#my chatbot code

inputprompt = raw_input( "Hello, I am a chatbot. For the purpose of this conversation please answer me with y for yes or n for no > " )



usrName = raw_input( "Please enter your name here to get started > " )

print usrName.upper()

print ("That's it right?")

usrAge = input("Great! now I need to know a little more about you. Can you tell me your age? >")

if usrAge < 14 :
    print "You are still in basic school. Aren't you?"

elif usrAge <= 18 :
    print "Judging by your age I would say you are still in high school or just graduated"

elif usrAge <= 23 :
    print "So I'm guessing you just graduated from university maybe?"

else:
    print "We have a working class person! nice! I would need a loan soon"



