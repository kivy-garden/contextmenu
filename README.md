# garden.contextmenu

Collection of classes for easy creating **context** and **application** menus.

## Context Menu

![Example of context menu](https://raw.githubusercontent.com/kivy-garden/garden.desktopvideoplayer/master/doc/context-menu-01.png)

Context menu is represented by `ContextMenu` widget that wraps all menu items as `ContextMenuTextItem` widgets. Context menus can be nested, each `ContextMenuTextItem` can contain maximum one `ContextMenu` widget.

```python
import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy.garden.contextmenu

kv = """
FloatLayout:
    id: layout
    Label:
        pos: 10, self.parent.height - self.height - 10
        text: "Left click anywhere outside the context menu to close it"
        size_hint: None, None
        size: self.texture_size

    ContextMenu:
        id: context_menu
        visible: False
        cancel_handler_widget: layout

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
                            text: "SubMenu #9"
                        ContextMenuTextItem:
                            text: "SubMenu #10"
                        ContextMenuTextItem:
                            text: "SubMenu #11"
                        ContextMenuTextItem:
                            text: "Hello, World!"
                            on_release: app.say_hello(self.text)
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
        print(text)
        self.root.ids['context_menu'].hide()

if __name__ == '__main__':
    MyApp().run()
```

Arrows that symbolize that an item has sub menu is created automatically. `ContextMenuTextItem` inherits from [ButtonBehavior](http://kivy.org/docs/api-kivy.uix.behaviors.html#kivy.uix.behaviors.ButtonBehavior) so you can use `on_release` to bind actions to it.
The root context menu can use `cancel_handler_widget` parameter. This adds `on_touch_down` event to it that closes the menu when you click anywhere outside the menu.


## Application Menu

![Example of application menu](https://raw.githubusercontent.com/kivy-garden/garden.contextmenu/master/doc/app-menu-01.png)

Creating application menus is very similar to context menus. Use `AppMenu` and `AppMenuTextItem` widgets to create the top level menu. Then each `AppMenuTextItem` can contain one `ContextMenu` widget as we saw above. `AppMenuTextItem` without `ContextMenu` are disabled by default

```python
import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy.garden.contextmenu

kv = """
FloatLayout:
    id: layout
    AppMenu:
        id: app_menu
        top: root.height
        cancel_handler_widget: layout

        AppMenuTextItem:
            text: "Menu #1"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #11"
                ContextMenuTextItem:
                    text: "Item #12"
        AppMenuTextItem:
            text: "Menu Menu Menu #2"
            ContextMenu:
                ContextMenuTextItem:
                    text: "Item #21"
                ContextMenuTextItem:
                    text: "Item #22"
                ContextMenuTextItem:
                    text: "ItemItemItem #23"
                ContextMenuTextItem:
                    text: "Item #24"
                    ContextMenu:
                        ContextMenuTextItem:
                            text: "Item #241"
                        ContextMenuTextItem:
                            text: "Hello, World!"
                            on_release: app.say_hello(self.text)
                        # ...
                ContextMenuTextItem:
                    text: "Item #5"
        AppMenuTextItem:
            text: "Menu Menu #3"
            ContextMenu:
                ContextMenuTextItem:
                    text: "SubMenu #31"
                ContextMenuDivider:
                ContextMenuTextItem:
                    text: "SubMenu #32"
                # ...
        AppMenuTextItem:
            text: "Menu #4"
    # ...
    # The rest follows as usually
"""

class MyApp(App):

    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_string(kv)

    def say_hello(self, text):
        print(text)
        self.root.ids['app_menu'].close_all()

if __name__ == '__main__':
    MyApp().run()
```

# License

garden.contextmenu is licensed under MIT license.