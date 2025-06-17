from flet import Column, Row, Text, IconButton, icons

class Navigation:
    def __init__(self):
        self.navigation_bar = Row()

    def add_button(self, text, icon, on_click):
        button = IconButton(icon=icon, tooltip=text, on_click=on_click)
        self.navigation_bar.controls.append(button)

    def get_navigation(self):
        return self.navigation_bar