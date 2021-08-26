import kivy
from kivy.app import App
from kivy.uix.switch import Switch
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.clock import Clock
from functools import partial
import time
import requests
from datetime import datetime



class SwitchContainer(GridLayout): #create a class that uses the GridLayout module
    def __init__(self, **kwargs):
        #schedule the JSONrequest function to trigger every 5 seconds to read/write database
        event = Clock.schedule_interval(partial(self.JSONrequest), 10)
        super(SwitchContainer, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="Motion Detected (SW 1): ")) #create a label for SW1
        self.sw1 = Switch(active=False) #create a SwitchCompat for SW1 (default to OFF)
        self.add_widget(self.sw1) #add the created SwitchCompat to the screen
        self.sw1.disabled = True #make SW1 unclickable on the app
        
        self.add_widget(Label(text=" Enable Alarm (LED 1): ")) #create a label for LED1
        self.led1 = Switch(active=False) #create a SwitchCompat for LED1 (default to OFF)
        self.add_widget(self.led1) #add the created SwitchCompat to the screen
        self.led1.disabled = False #by default a created SwitchCompat is clickable; so, there is no need
        #for this statement

        
        self.add_widget(Label(text="Disable Alarm (LED 2): ")) #create a label for LED2
        self.led2 = Switch(active=False) #create a SwitchCompat for LED2 (default to OFF)
        self.add_widget(self.led2) #add the created SwitchCompat to the screen
        self.led2.disabled = False #by default a created SwitchCompat is clickable; so, there is no need
        #for this statement
        
        self.add_widget(Label(text="Acknowledge Alarm (LED 3): ")) #create a label for LED3
        self.led3 = Switch(active=False) #create a SwitchCompat for LED3 (default to OFF)
        self.add_widget(self.led3) #add the created SwitchCompat to the screen
        self.led3.disabled = False #by default a created SwitchCompat is clickable; so, there is no need
        #for this statement

         
        

        
    def JSONrequest(self, *largs):
        if (self.sw1.active == True):
            SW1=1
        else:
            SW1= 0
        if (self.led1.active == True):
            LED1= 1
        else:
            LED1= 0
        if (self.led2.active == True):
            LED2 = 1
        else:
            LED2 = 0
        if (self.led3.active == True):
            LED3 = 1
        else:
            LED3 = 0

        ts = datetime.now()
                                                 #below are json request payload, the request itself, and the response
        data = {'username': 'ben','password':'benpass', 'SW1':SW1, 'LED1': LED1, 'LED2' : LED2, 'LED3' : LED3, 'TS' : str(ts), 'logID' : 2, 'data' : 'ben', 'msgID' : 1010} #json request payload
        res = requests.post("https://adverbial-addressee.000webhostapp.com/scripts/sync_app_data.php",json=data)
        r = res.json() #json response

        if SW1 != r['SW1']: #check the received value of SW1 & change it on the App if there is a mismatch
            print("Changing SW1 status to the value in the database.")
            if self.sw1.active == True:
                self.sw1.active = False
            else:
                self.sw1.active = True
        if LED1 != r['LED1']: #check the received value of led1 & change it on the App if there is a mismatch
            print("Changing LED1 status to the value in the database.")
            if self.led1.active == True:
                self.led1.active = False
            else:
                self.led1.active = True
    
        if LED2 != r['LED2']: #check the received value of led2 & change it on the App if there is a mismatch
            print("Changing LED2 status to the value in the database.")
            if self.led2.active == True:
                self.led2.active = False
            else:
                self.led2.active = True
    
        if LED3 != r['LED3']: #check the received value of led3 & change it on the App if there is a mismatch
            print("Changing LED3 status to the value in the database.")
            if self.led3.active == True:
                self.led3.active = False
            else:
                self.led3.active = True
         
     
        
        
        
class SwitchProject(App):
    def build(self): #build
        return SwitchContainer()
if __name__ == '__main__':
    SwitchProject().run() #run
