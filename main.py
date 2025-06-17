import flet as ft
from pages.title_page import TitlePage
from pages.intro_page import IntroPage
from pages.third_page import ThirdPage 
from pages.flet_intro import FletIntroPage
from pages.table_page import TablePage
from pages.demo_page1 import DemoPage1
from pages.demo_page2 import DemoPage2
from pages.demo_page3 import DemoPage3
from pages.demo_page4 import DemoPage4
from pages.demo_page5 import DemoPage5
from pages.demo_page6 import DemoPage6
from pages.bts import BTS
from pages.dodonts import WhenToUsePage

class PresentationApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.current_page_index = 0
        self.pages = [
            TitlePage(),
            IntroPage(),
            ThirdPage(),
            FletIntroPage(),
            TablePage(),
            DemoPage1(),
            DemoPage2(),
            DemoPage3(),
            DemoPage4(page),
            DemoPage5(),
            DemoPage6(),
            BTS(),
            WhenToUsePage(),
        ]
        
        self.setup_page()
        self.setup_navigation()
        self.show_current_page()
    
    def setup_page(self):
        self.page.title = "Building Cross Platform Apps with Flet - PyCon SG"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = "#1e1e1e"
        self.page.window.width = 1200
        self.page.window.height = 800
        self.page.window.center()
    
    def setup_navigation(self):
        # Create page counter text that we can update
        self.page_counter = ft.Text(
            f"{self.current_page_index + 1} / {len(self.pages)}",
            color="#ffffff",
            size=16,
        )
        
        # Navigation bar at the bottom
        self.nav_bar = ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.ARROW_BACK,
                    tooltip="Previous",
                    on_click=self.previous_page,
                    icon_color="#FFD43B",
                ),
                self.page_counter,  # Use the stored reference
                ft.IconButton(
                    icon=ft.Icons.ARROW_FORWARD,
                    tooltip="Next",
                    on_click=self.next_page,
                    icon_color="#FFD43B",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )
    
    def update_navigation(self):
        # Update the page counter text and refresh the page
        self.page_counter.value = f"{self.current_page_index + 1} / {len(self.pages)}"
        self.page.update()
    
    def show_current_page(self):
        self.page.clean()
        
        # Main content area
        content_area = ft.Container(
            content=self.pages[self.current_page_index],
            expand=True,
        )
        
        # Navigation area
        nav_area = ft.Container(
            content=self.nav_bar,
            height=60,
            bgcolor="#2d2d2d",
            padding=10,
        )
        
        # Main layout
        main_layout = ft.Column(
            [
                content_area,
                nav_area,
            ],
            spacing=0,
            expand=True,
        )
        
        self.page.add(main_layout)
        self.update_navigation()  # Update counter after adding to page
    
    def next_page(self, e):
        if self.current_page_index < len(self.pages) - 1:
            self.current_page_index += 1
            self.show_current_page()
    
    def previous_page(self, e):
        if self.current_page_index > 0:
            self.current_page_index -= 1
            self.show_current_page()

def main(page: ft.Page):
    app = PresentationApp(page)

if __name__ == "__main__":
    ft.app(target=main,  assets_dir="assets")