from kivy.lang import Builder
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

Builder.load_file("layout_examples.kv")

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
