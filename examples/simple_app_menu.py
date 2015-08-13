import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.logger import Logger
import logging

kivy.require('1.9.0')
# Logger.setLevel(logging.DEBUG)

import kivy.garden.contextmenu


kv = """
FloatLayout:
    id: layout
    AppMenu:
        top: root.height
        cancel_handler_widget: layout
        AppMenuTextItem:
            text: "Menu Menu Menu #1"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #1"
                ContextMenuTextItem:
                    text: "Item #2"
                ContextMenuTextItem:
                    text: "ItemItemItem #3"
                ContextMenuTextItem:
                    text: "Item #4"
                    ContextMenu:
                        ContextMenuTextItem:
                            text: "Item #41"
                        ContextMenuTextItem:
                            text: "Hello, World!"
                            on_release: print(self.text)
                        ContextMenuTextItem:
                            text: "Item #43"
                        ContextMenuTextItem:
                            text: "Item #44"
                ContextMenuTextItem:
                    text: "Item #5"
        AppMenuTextItem:
            text: "Menu #2"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #21"
                ContextMenuTextItem:
                    text: "Item #22"
        AppMenuTextItem:
            text: "Menu Menu #3"
            ContextMenu:
                ContextMenuTextItem:
                    text: "SubMenu #31"
                ContextMenuTextItem:
                    text: "SubMenu #32"
                ContextMenuTextItem:
                    text: "SubMenu #33"
                ContextMenuTextItem:
                    text: "SubMenu #34"
        AppMenuTextItem:
            text: "Menu #4"
"""


class MyApp(App):

    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_string(kv)


if __name__ == '__main__':
    MyApp().run()