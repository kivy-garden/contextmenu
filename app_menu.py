from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.lang import Builder
from kivy.clock import Clock
from functools import partial
import kivy.properties as kp
import os

from context_menu import AbstractMenu, AbstractMenuItem, AbstractMenuItemHoverable


class AppMenu(StackLayout, AbstractMenu):

    def __init__(self, *args, **kwargs):
        super(AppMenu, self).__init__(*args, **kwargs)
        self._setup_hover_timer()

    def update_height(self):
        max_height = 0
        for widget in self.menu_item_widgets:
            if widget.height > max_height:
                max_height = widget.height
        return max_height

    def on_children(self, obj, new_children):
        for w in new_children:
            # bind events that update app menu height when any of its children resize
            w.bind(on_size=self.update_height)
            w.bind(on_height=self.update_height)


class AppMenuTextItem(RelativeLayout, AbstractMenuItem, AbstractMenuItemHoverable):
    label = kp.ObjectProperty(None)
    text = kp.StringProperty('')
    font_size = kp.NumericProperty(14)
    color = kp.ListProperty([1,1,1,1])

    # def __init__(self, *args, **kwargs):
    #     super(AppMenuTextItem, self).__init__(*args, **kwargs)


_path = os.path.dirname(os.path.realpath(__file__))
Builder.load_file(os.path.join(_path, 'app_menu.kv'))
