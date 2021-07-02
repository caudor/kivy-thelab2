from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.slider import Slider
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    #slider_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    txt_input_str = StringProperty("foo")
    #slider_value_txt = StringProperty("50")

    def on_button_click(self):
        print('button clicked')
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):       #self refers to class and widget refers to calling widget
        print("toggle state: " + widget.state)      #prints either down or normal
        if widget.state == 'normal':
            #OFF
            widget.text = "OFF"
            self.count_enabled = False
        else:
            #ON
            widget.text = "ON"
            self.count_enabled = True

    #def on_switch_active(self, widget):
    #    print("switch: " + str(widget.active))

    #def on_slider_value(self, widget):
    #   print("slider value: " + str(int(widget.value)))
    #   self.slider_value_txt =  str(int(widget.value))
    def on_text_validate(self, widget):
        self.txt_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.orientation = "lr-bt"
        self.orientation = "lr-tb"
        for i in range(0,100):  #finally, if we change to 100 there be 100 buttons but can't see all.  Time scrollview
            size = dp(100)    # size is just var name now, can be named anything
            # b = Button(text=str(i+1), size_hint=(.2, .2))
            b = Button(text=str(i + 1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)      # Notice Z becomes first button, pushing aside others

# class GridLayoutExample(GridLayout):  this time we went differnt and defined grid layout in .kv file
#    pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass

"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"  #default  change to 'vertical' to see what happens
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)          #run now and you'll get three huge buttons side by side
"""


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


TheLabApp().run()
