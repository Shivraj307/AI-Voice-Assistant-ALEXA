import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import subprocess
import tkinter as tk
import playsound
import randfacts
import webbrowser
import time
# import customtkinter

# customtkinter.set_default_color_theme('blue')
root = tk.Tk()
root.title("Alexa Using Python")
root.geometry("300x200")
# root.configure(bg='#202020')
label = tk.Label(root, text="")
label.pack()
label1 = tk.Label(root, text="")
custfont="Arial",10,"italic"
label.config(font=custfont,fg="black")
label1.pack()
listener = sr.Recognizer()
r1 = sr.Recognizer()
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def stop_ai():
    global running
    running=False
    root.destroy()
def talk(text):
    engine.say(text)
    engine.runAndWait()
    # rate = engine.getProperty("rate")
    # engine.setProperty("rate", rate - 50)
intro="Hey I'm Alexa. How can I Help you ?"
label.config(text=intro)
talk(intro)
def take_command():
    command=""
    try:
            with sr.Microphone() as source:
                # label.config(text='listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'alexa' in command:
                    pass
                    # label1.config(text=command)
                    # command = command.replace('alexa', '')
                    # print(command)
                    # label.config(text=command)
    except:
            pass
    return command
def run_alexa():
    
    command = take_command()
    # label1.config(text=take_command)
    # label.config(text=command)
    if 'video' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time1 = datetime.datetime.now().strftime('%I:%M %p')
        # print(time)
        label1.config(text=time1)
        talk('Current time is ' + time1)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        label1.config(text=info)
        talk(info)
    elif 'joke' in command:
        joke=pyjokes.get_joke()
        label1.config(text=joke)   
        talk(joke)
    elif 'open app' in command:
        try:
            with sr.Microphone() as source1:
                # print("Which application would you like to open?")
                talk("Which application would you like to open?")
                audio = r1.listen(source1)
                app_name = r1.recognize_google(audio)
                app_name = app_name.lower()
                # label1.config(text="Opening application:")
                talk("Opening app")
                subprocess.Popen(app_name)
        except FileNotFoundError:
            print("Application not found.")
    elif 'wish me' in command:
        hour = int(datetime.datetime.now().hour)
        if hour>= 0 and hour<12:
            talk("Good Morning Sir !")
    
        elif hour>= 12 and hour<18:
            talk("Good Afternoon Sir !")  
        else:
            talk("Good Evening Sir !")
    elif 'who am i' in command:
        # username="SJ"
        talk('Your my Master a passionate programmer')
    elif 'lightning'in command:
        talk("Playing Lightning sound")
        playsound.playsound("light.mp3")
    elif 'fact'in command:
        talk("Heres one of the Fact")
        fact = randfacts.get_fact()
        talk("the fact is ")
        label1.config(text=fact)
        talk(fact)
        time.sleep(1)
    elif 'search' in command:
        command=command.replace('alexa','')
        search_url = f"https://www.google.com/search?q={command}"
        webbrowser.open(search_url)
    elif'facebook'in command:
        search_url2=f"facebook.com"
        webbrowser.open(search_url2)
    elif'whatsapp'in command:
        search_url3=f"web.whatsapp.com"
    elif'insta' or'instagram' in command:
        search_url3=f"instagram.com"
    elif'mood' in command:
        mood="Neutral, that's how I'm felling rightnow and this is my current mood"
        print(mood)
        talk(mood)   
        return True
    else:
        talk('Please say the command again.')
# button = tk.Button(root, text="Recognize Voice",  command=take_command)
# button.pack()

running=True
while running:
    button1 = tk.Button(root, text="ALEXA",  command=run_alexa)
    customfont=("Arial",20,"bold")
    button1.configure(bg="#3996d5",font=customfont,fg="White")
    # button1.grid(padx=20,pady=20)
    button1.pack()
    stop_button=tk.Button(root,text="STOP",command=stop_ai)
    stop_button.pack()    
    root.mainloop() 
    run_alexa()    
    
  

    