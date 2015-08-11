import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require('1.9.0')

import kivy.garden.contextmenu


kv = """
FloatLayout:
    AppMenu:
        top: root.height
        AppMenuTextItem:
            color: 1,0,1,1
            text: "Menu Menu Menu #1"
        AppMenuTextItem:
            text: "Menu #2"
        AppMenuTextItem:
            text: "Menu Menu #3"
        AppMenuTextItem:
            text: "Menu #4"
"""


class MyApp(App):

    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_string(kv)


if __name__ == '__main__':
    MyApp().run()