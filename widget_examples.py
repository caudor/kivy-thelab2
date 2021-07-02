from kivy.lang import Builder
from kivy.properties import BooleanProperty, StringProperty
from kivy.uix.gridlayout import GridLayout

Builder.load_file("widget_examples.kv")


class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty("1")
    txt_input_str = StringProperty("foo")

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

    def on_text_validate(self, widget):
        self.txt_input_str = widget.text
