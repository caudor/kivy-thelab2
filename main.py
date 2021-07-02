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




class TheLabApp(App):
    pass


TheLabApp().run()
