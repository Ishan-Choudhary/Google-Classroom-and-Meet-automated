import webbrowser
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()


urlGeneral = 'Give the variables along with the google meet links'

webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser("/path/to/chrome.exe"))

def automatefull(Meetingurl, sirormaam): #The two arguments that you will have to pass is the meeting url and the gender which
                                         #which is asked below
    time.sleep(5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('t')
        keyboard.release('t')
    keyboard.type(Meetingurl)
    keyboard.press(Key.enter)

    while True:
        #if you want to break through this do we need to reload loop, just type 'exit'
        reload = input("do we need to reload: ")
        if reload.lower() == "yes":
            time.sleep(5)
            with keyboard.pressed(Key.ctrl):
                keyboard.press('w')
                keyboard.release('w')
            with keyboard.pressed(Key.ctrl):
                keyboard.press('t')
                keyboard.release('t')
            keyboard.type(Meetingurl)
            keyboard.press(Key.enter)

        elif reload.lower() == 'no':
            time.sleep(7.5) #Vary the time based on your net speed or how fast your browser is loading the page

            with keyboard.pressed(Key.ctrl):
                keyboard.press('d')
                keyboard.release('d')
            with keyboard.pressed(Key.ctrl):
                keyboard.press('e')
                keyboard.release('e')
        
            time.sleep(8.6)
        
            with keyboard.pressed(Key.ctrl):
                with keyboard.pressed(Key.alt):
                    keyboard.press('c')
                    keyboard.release('c')
        
            time.sleep(1.5)
        
            keyboard.type("Whatever greeting you want for example: Good morning or Namaste {}".format(sirormaam))
            keyboard.press(Key.enter)
        
            time.sleep(0.5)

            with keyboard.pressed(Key.ctrl):
                with keyboard.pressed(Key.alt):
                    keyboard.press('c')
                    keyboard.release('c')


        elif reload.lower() == 'exit':
            break
            quit

        else:
            print("Please input yes or no")

while True:
    inputClassName = input("Which class would you like to enter: ")
    askGender = input("Is it a sir or ma'am: ") '''This is needed as you can see in the above function since this will help in
                                                    sending the message on the google meet chatbox.'''
    if inputClassName.lower() == "classroom":
        webbrowser.get('chrome').open(urlGeneral) #This will open my google classroom and not any lecture
    elif inputClassName.lower() == "maths": #this will check for the class name that I am inputing. You can change this to your specified class
        webbrowser.get('chrome').open(urlMath) #This will open my maths google classroom
        automatefull(urlMeetMaths, askGender) #This will open my maths meet.
    elif inputClassName.lower() == 'physics':
        webbrowser.get('chrome').open(urlPhysics) #Same goes for all of the other elifs
        automatefull(urlPhysicsMeet, askGender)      
    elif inputClassName.lower() == 'chemistry':
        webbrowser.get('chrome').open(urlChemistry)
        automatefull(urlChemistryMeet, askGender)
    elif inputClassName.lower() == 'biology':
        webbrowser.get('chrome').open(urlBiology)
        automatefull(urlBiologyMeet, askGender)
    elif inputClassName.lower() == 'esl':
        webbrowser.get('chrome').open(urlEnglishESL)
        automatefull(urlEnglishESLMeet, askGender)
    elif inputClassName.lower() == 'fle':
        webbrowser.get('chrome').open(urlEnglishFLE)
        automatefull(urlEnglishFLEMeet, askGender)
    elif a.lower() == 'ict':
        webbrowser.get('chrome').open(urlICT)
        automatefull(urlICTMeet, askGender)
    elif a.lower() == 'exit': #This is used to exit the code. You will have to exit the code twice since exit for the sirorma'am
        break                 #variable is not specified
        quit
    else:
        print("No class such as that") #Since this is a class opening app and if I type random giberish it will print this message.
