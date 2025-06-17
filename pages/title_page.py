import flet as ft

class TitlePage(ft.Container):
    def __init__(self):
        super().__init__()
        
        # Python-themed colors
        self.bgcolor = "#1e1e1e"  # Dark background like VS Code
        self.expand = True
        
        # Create the title page content
        title = ft.Text(
            "Building Cross Platform Apps with Flet",
            size=48,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",  # Python yellow
            text_align=ft.TextAlign.CENTER,
        )
        
        subtitle = ft.Text(
            "PyCon SG 2025",
            size=24,
            color="#4B8BBE",  # Python blue
            text_align=ft.TextAlign.CENTER,
        )
        
        # Python logo or icon
        python_icon = ft.Image(
            src="https://raw.githubusercontent.com/flet-dev/flet/main/media/logo/flet-logo.svg",  # Changed from ft.icons.CODE to ft.Icons.CODE
            width=80,
            height=80,
        )
        
        # Flet info
        flet_info = ft.Text(
            "Build web, desktop and mobile apps in Python",
            size=18,
            color="#ffffff",
            text_align=ft.TextAlign.CENTER,
        )
                
        flet_built = ft.Text(
            "This presentation is built with Flet",
            size=18,
            color="#4B8BBE",
            text_align=ft.TextAlign.CENTER,
            italic=True,
        )
        # Main content column
        self.content = ft.Column(
            [
                python_icon,
                ft.Container(height=20),  # Spacer
                title,
                ft.Container(height=10),  # Spacer
                subtitle,
                ft.Container(height=30),  # Spacer
                flet_info,
                ft.Container(height=30),  # Spacer
                flet_built,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=0,
        )
        
        self.alignment = ft.alignment.center