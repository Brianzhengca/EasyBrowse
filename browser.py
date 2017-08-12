#!/usr/bin/python
#copyright@Brian
import easygui
import webbrowser
easygui.msgbox("This program will open a new window of a website in your default browser.(ex: Type'google.com') Type 'quit' to quit")
while 1:
    e = easygui.enterbox("What is the website's name?")
    a = "http://www."+str(e)
    if e =="quit":
        easygui.msgbox("Thanks for using this program.")
        break
    try:
        webbrowser.open_new_tab(a)
    except:
        webbrowser.open_new_tab(e)
        
    
        
    
 
    
    
