import kivy
from kivy.app import App
from kivy.lang import Builder

kivy.require('1.9.0')

import kivy.garden.contextmenu


kv = """
FloatLayout:
    on_touch_down: context_menu.self_or_submenu_collide_with_point(args[1].x, args[1].y) is None and context_menu.hide()
    Label:
        pos: 10, self.parent.height - self.height - 10
        text: "Left click anywhere outside the context menu to close it"
        size_hint: None, None
        size: self.texture_size

    Button:
        size_hint: None, None
        pos_hint: {"center_x": 0.5, "center_y": 0.5 }
        size: 300, 40
        text: "Click me to show the context menu"
        on_release: context_menu.show(*app.root_window.mouse_pos)

    ContextMenu:
        id: context_menu
        visible: False
        ContextMenuTextItem:
            text: "SubMenu #2"
        ContextMenuTextItem:
            text: "SubMenu #3"
            ContextMenu:
                ContextMenuTextItem:
                    text: "SubMenu #5"
                ContextMenuTextItem:
                    text: "SubMenu #6"
                    ContextMenu:
                        ContextMenuTextItem:
                            text: "Hello, Wordl!"
                            on_release: app.say_hello(self.text)
                        ContextMenuTextItem:
                            text: "SubMenu #9"
                        ContextMenuTextItem:
                            text: "SubMenu #10"
                        ContextMenuTextItem:
                            text: "SubMenu #11"
                        ContextMenuTextItem:
                            text: "SubMenu #12"
                ContextMenuTextItem:
                    text: "SubMenu #7"
        ContextMenuTextItem:
            text: "SubMenu #4"
"""

class MyApp(App):

    def build(self):
        self.title = 'Simple context menu example'
        return Builder.load_string(kv)

    def say_hello(self, text):
        self.root.ids['context_menu'].hide()
        print(text)


if __name__ == '__main__':
    MyApp().run()