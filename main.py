# Statistical_Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import numpy as np

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "KSquared-Mathematics :"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"    	     
                
        Button:
            font_size: '20sp'
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 100
            text: "Statistical Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"    	       
""")

#Menu
Builder.load_string("""
<Menu>:
    id: Menu
    name: "Menu"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Menu"
            
            Button:
                font_size: '20sp'
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height:200
                text: "Statistical Calculator"
                on_release:
                    app.root.current = "Statistical_Calculator"
                    root.manager.transition.direction = "left" 
                    
            Button:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://kevinjunice.wixsite.com/ksquaredllc')
            
            Button:
                font_size: '20sp'
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 800
                width: 800
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
    
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-math?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Statistical Calculator v0.1"
                
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

#Percentage_Calculator
Builder.load_string("""
<Statistical_Calculator>
    id:Statistical_Calculator
    name:"Statistical_Calculator"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Statistical Calculator"
            
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    padding: 10, 10
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        perc.text = ""
                        dev.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "Numbers seperated by a comma"
                multiline: False
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10
            
                    
            Button:
                id: mmm
                text: "Mean, Median & Mode"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Statistical_Calculator.mmm(entry.text)    
                
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                    
                TextInput:
                    id: dev
                    text: dev.text
                    hint_text: "1,2 or 3 Deviations"
                    multiline: False
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:1 - len(dev.text)] 
                    
                Button:
                    id: sd
                    text: "Standard Deviation"   
                    font_size: '15sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Statistical_Calculator.sd(entry.text + "&" + dev.text)  
                    
            Button:
                id: var
                text: "Variance"   
                font_size: '20sp'
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Statistical_Calculator.var(entry.text)  
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                    
                TextInput:
                    id: perc
                    text: perc.text
                    hint_text: "nth Percentile"
                    multiline: False
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(perc.text)] 
                    
                Button:
                    id: percentile
                    text: "Percentile"   
                    font_size: '15sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Statistical_Calculator.perc(entry.text + "%" + perc.text)  
                          
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height   

""")

class Statistical_Calculator(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Statistical_Calculator, self).__init__(**kwargs)
            
    layouts = []
    def mmm(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry.replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))

            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            mean_output = str(np.mean(entry_list))
            print("Mean: ",mean_output)
            
            median_output = str(np.median(entry_list))
            print("Median: ",median_output)
            
            #Mean
            entry_list_count = []
            i = 0
            while i < len(entry_list):
                print("loop started")
                print("entry_list",entry_list[i])
                entry_list_count.append(entry_list.count(entry_list[i]))
                print("entry_list_count",entry_list_count)
                i = i + 1
                
            print()
            maximum_count = max(entry_list_count)
            print("maximum_count",maximum_count)
            maximum_count_index = entry_list_count.index(maximum_count)
            print("maximum_count_index",maximum_count_index)
            mode_output = entry_list[maximum_count_index]
            print("mode_output",mode_output)
                
                
            self.ids.list_of_steps.add_widget(Label(text= "Mean = " + mean_output ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Median = " + median_output ,font_size = '15sp', size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Mode = " + str(mode_output) + " counted " + str(maximum_count) + " time(s) ",font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  
            
    def sd(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            amp = entry.find("&")
            print("amp:",amp)
            
            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry[:amp].replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))
            
            dev = entry[amp+1:]
            print("dev:",dev)
            
            if dev == "":
                dev = 1
            
            entry_list = entry[:amp].split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            if int(dev) == 1:
                SD = entry_list
                SD = str(np.std(SD))
                print("SD",SD)
                self.ids.list_of_steps.add_widget(Label(text= "Standard Deviation = " ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= SD ,font_size = '15sp', size_hint_y= None, height=100))

            elif int(dev) == 2:
                SD = entry_list
                SD = str(float(np.mean(entry_list)) + 2 * float(np.std(SD)))
                print("SD",SD)
                self.ids.list_of_steps.add_widget(Label(text= "Second Standard Deviation = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= SD ,font_size = '15sp', size_hint_y= None, height=100))
            
            elif int(dev) == 3:
                SD = entry_list
                SD = str(float(np.mean(entry_list)) + 3 * float(np.std(SD)))
                print("SD",SD)
                self.ids.list_of_steps.add_widget(Label(text= "Third Standard Deviation = " ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= SD ,font_size = '15sp', size_hint_y= None, height=100))
                
            elif int(dev) > 3:
                self.ids.list_of_steps.add_widget(Label(text= "Standard Deviation must be between :" ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "1, 2 or 3" ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def var(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:

            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry.replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))

            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            var = str(np.var(entry_list))
            print("Var",var)
            
            self.ids.list_of_steps.add_widget(Label(text= "Variance = " + var ,font_size = '15sp', size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def perc(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:

            print("entry",entry)
            percent = entry.find("%")
            print("percent",percent)
            
            self.ids.list_of_steps.add_widget(Label(text= "Entry = " + entry[:percent].replace(" ","").replace(",",", ") ,font_size = '15sp', size_hint_y= None, height=100))
            
            nth = int(entry[percent+1:])
            print("nth",nth)
            
            entry = entry[:percent]
            print("entry",entry)
            
            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            perc = str(np.percentile(entry_list,nth))
            print("perc",perc)
            
            if str(nth)[-1] == "1":
                nth = str(nth) + "st"
            elif str(nth)[-1] == "2":
                nth = str(nth) + "nd"
            elif str(nth)[-1] == "3":
                nth = str(nth) + "rd"
            else:
                nth = str(nth) + "th"
            print("nth",nth)
            
            self.ids.list_of_steps.add_widget(Label(text= perc + " is in the " + str(nth) + " Percentile"  ,font_size = '15sp', size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
                
class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))     
sm.add_widget(updates(name="updates"))
sm.add_widget(Statistical_Calculator(name="Statistical_Calculator"))     
sm.current = "Homepage"   


class Statistical_Calculator(App):
    def __init__(self, **kwargs):
        super(Statistical_Calculator, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Statistical_Calculator().run()
