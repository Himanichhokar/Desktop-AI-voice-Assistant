import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
#The Speech Application Programming Interface or SAPI is an API( interaction between multiple software) 
# developed by Microsoft to allow the use of speech recognition
#  and speech synthesis within Windows applications. 
engine= pyttsx3.init('sapi5')
#Gets the current value of a property. Valid names and values include:
#voice: String ID of the current voice
voices =engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)




# speak fuction for AI
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#wish function to wish 
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour> 0 and hour<12):
        speak('Good Morning ') 
    elif (hour>=12 and hour<18):
        speak('Good Afternoon ')  
    else:
        speak('Good Evening ')

    speak('Im jarvis, What can i do for you')        


def Takecommand():
    # Itakes microphones input from the user  and return as str output
    r=sr.Recognizer()
    #calling the recogniser class which helps to recognize the voice 
    with sr.Microphone() as sourse:
        print('Recognizing....')
        r.pause_threshold= 1
        audio=r.listen(sourse)


    try:
        print('listening....')
        query=r.recognize_google(audio,language='en-in')
        print('User said',query)

    except Exception as e:
        print(e)
        print('Say that again please...')
        return 'none'
    return query       






if __name__ == '__main__':

    wishme()
    #Takecommand()
    #logic for executing task based on query
    if 1:
        query=Takecommand().lower()
        if 'wikipedia'  in query:
            speak('searching wikipedia...')
            query=query.replace('wikipedia',"")
            speak('According to wikipedia')
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'open google' in query:
            webbrowser.open('google.com')
            
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'time ' in query:
            strTime= datetime.datetime().now().strftime('%H:%M:%S')  
            speak(strTime)
        elif 'open code' in query:
            codepath=' C:\\Users\\HIMANSHUL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs'
            os.startfile(codepath)
        elif 'Play Movies' in query:
            path=' C:\\Users\\HIMANSHUL'
            speak('playing movies..')
            os.startfile(path)
        elif 'quit' in query:
            exit






