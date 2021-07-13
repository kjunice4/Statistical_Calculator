# Statistical_Calculator

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import numpy
from scipy import stats

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
                app.root.current = "Statistical_Calculator"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Statistical Calculator"
            on_release:
                app.root.current = "Statistical_Calculator"
                root.manager.transition.direction = "left" 

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
                font_size: 75
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
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        perc.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        entry.text = ""
                        perc.text = ""
                        list_of_steps.clear_widgets()       
        
            TextInput:
                id: entry
                text: entry.text
                hint_text: "Enter a group of numbers seperated by a comma"
                multiline: False
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10
            
                    
            Button:
                id: mmm
                text: "Mean, Median & Mode"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 1 , 0 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Statistical_Calculator.mmm(entry.text)    
                
            Button:
                id: sd
                text: "Standard Deviation"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    list_of_steps.clear_widgets() 
                    Statistical_Calculator.sd(entry.text)  
                    
            Button:
                id: var
                text: "Variance"   
                font_size: 75
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
                    hint_text: "Enter nth Percentile"
                    multiline: False
                    font_size: 100
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:3 - len(perc.text)] 
                    
                Button:
                    id: percentile
                    text: "Percentile"   
                    font_size: 75
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
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = sm.previous()    
    layouts = []
    def mmm(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            mean_output = str(numpy.mean(entry_list))
            print("Mean: ",mean_output)
            
            median_output = str(numpy.median(entry_list))
            print("Median: ",median_output)
            
            mode_output = str(stats.mode(entry_list))
            print("Mode: ",mode_output)
            
            comma_index = mode_output.find(",")
            print("comma_index",comma_index)
            
            count_slice = mode_output[comma_index:]
            print("count_slice",count_slice)
            count = count_slice.replace(", count=array([","").replace("]))","")
            print("count",count)
            
            mode_output = mode_output[:comma_index]
            print("mode_output",mode_output)
            left_bracket_index = mode_output.rfind("[")
            print("left_bracket_index",left_bracket_index)
            mode_output = mode_output[left_bracket_index:].replace("[","").replace("]","").replace(")","")
            print("mode_output",mode_output)
            
            if mode_output[-1] == ".":
                mode_output = mode_output + "0"
                print("mode_output",mode_output)
                
            self.ids.list_of_steps.add_widget(Label(text= "Mean = " + mean_output ,font_size = 60, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Median = " + median_output ,font_size = 60, size_hint_y= None, height=100))
            self.ids.list_of_steps.add_widget(Label(text= "Mode = " + mode_output + " counted " + count + " times ",font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)  
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)  
            
    def sd(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            SD = str(numpy.std(entry_list))
            print("SD",SD)
            
            self.ids.list_of_steps.add_widget(Label(text= "Standard Deviation = " + SD ,font_size = 60, size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def var(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            entry_list = entry.split(",")
            print("entry_list",entry_list)
            
            i=0
            while i < len(entry_list):
                entry_list[i] = float(entry_list[i])
                i = i + 1
            
            var = str(numpy.var(entry_list))
            print("Var",var)
            
            self.ids.list_of_steps.add_widget(Label(text= "Variance = " + var ,font_size = 60, size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def perc(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)

        try:
            print("entry",entry)
            percent = entry.find("%")
            print("percent",percent)
            
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
            
            perc = str(numpy.percentile(entry_list,nth))
            print("perc",perc)
            
            self.ids.list_of_steps.add_widget(Label(text= perc + " is in the " + str(nth) + "th Percentile"  ,font_size = 60, size_hint_y= None, height=100))
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)
                
class Homepage(Screen):
    pass            

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Statistical_Calculator(name="Statistical_Calculator"))     
sm.current = "Homepage"   


class Statistical_Calculator(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Statistical_Calculator().run()
