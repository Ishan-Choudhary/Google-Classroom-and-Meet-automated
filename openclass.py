import webbrowser
from pynput.keyboard import Controller, Key
import time

keyboard = Controller()

urlGeneral = 'https://classroom.google.com/u/2/h'
urlMath = "https://classroom.google.com/u/2/c/MTE5MTA1OTI4NjU3"
urlMeetMaths = "https://meet.google.com/lookup/hpxjeioncf?authuser=2&amp;hs=179"
urlPhysics = "https://classroom.google.com/u/2/c/MTIyMDI1NDgxMTI3"
urlPhysicsMeet = "https://meet.google.com/lookup/a73gnfjcrd?authuser=2&hs=179"
urlChemistry = "https://classroom.google.com/u/2/c/MTIxODkzNzk1NzAy"
urlChemistryMeet = "https://meet.google.com/lookup/hrwwobasn7?authuser=2&amp;hs=179"
urlBiology = "https://classroom.google.com/u/2/c/MTIyMTY5ODA3Nzc1"
urlBiologyMeet = "https://meet.google.com/lookup/hzc6ycutnc?authuser=2&hs=179"
urlICT = "https://classroom.google.com/u/2/c/MTQxNzIwMjE2NTA1"
urlICTMeet = "https://meet.google.com/lookup/fvfxktxslk?authuser=2&hs=179"
urlEnglishESL = "https://classroom.google.com/u/2/c/MTIxODQ3NzQ1ODY5"
urlEnglishESLMeet = "https://meet.google.com/lookup/ga5oes462j?authuser=2&hs=179"
urlEnglishFLE = "https://classroom.google.com/u/2/c/MTIxODQ3NzQ1ODky"
urlEnglishFLEMeet = "https://meet.google.com/lookup/asdtvllnil?authuser=2&hs=179"
urlPrincipalMaamMeet = "https://meet/google.com/xhr-ibprt-irt?authuser=2"

webbrowser.register('chrome', None,
                    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

def automatefull(Meetingurl, sirormaam):

    time.sleep(5)
    with keyboard.pressed(Key.ctrl):
        keyboard.press('t')
        keyboard.release('t')
    keyboard.type(Meetingurl)
    keyboard.press(Key.enter)

    while True:
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
            time.sleep(10)

            with keyboard.pressed(Key.ctrl):
                keyboard.press('d')
                keyboard.release('d')
            with keyboard.pressed(Key.ctrl):
                keyboard.press('e')
                keyboard.release('e')
        
            time.sleep(10)
        
            with keyboard.pressed(Key.ctrl):
                with keyboard.pressed(Key.alt):
                    keyboard.press('c')
                    keyboard.release('c')
        
            time.sleep(1.5)
        
            keyboard.type("Namaste {}".format(sirormaam))
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
    a = input("Which class would you like to enter: ")
    askGender = input("Is it a sir or ma'am: ")

    if a.lower() == "classroom":
        webbrowser.get('chrome').open(urlGeneral)
    elif a.lower() == "maths":
        webbrowser.get('chrome').open(urlMath)
        automatefull(urlMeetMaths, askGender)
    elif a.lower() == 'physics':
        webbrowser.get('chrome').open(urlPhysics) 
        automatefull(urlPhysicsMeet, askGender)      
    elif a.lower() == 'chemistry':
        webbrowser.get('chrome').open(urlChemistry)
        automatefull(urlChemistryMeet, askGender)
    elif a.lower() == 'biology':
        webbrowser.get('chrome').open(urlBiology)
        automatefull(urlBiologyMeet, askGender)
    elif a.lower() == 'esl':
        webbrowser.get('chrome').open(urlEnglishESL)
        automatefull(urlEnglishESLMeet, askGender)
    elif a.lower() == 'fle':
        webbrowser.get('chrome').open(urlEnglishFLE)
        automatefull(urlEnglishFLEMeet, askGender)
    elif a.lower() == 'ict':
        webbrowser.get('chrome').open(urlICT)
        automatefull(urlICTMeet, askGender)
    elif a.lower() == 'exit':
        break
        quit
    else:
        print("No class such as that")