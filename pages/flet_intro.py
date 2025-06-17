import flet as ft

class FletIntroPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        title = ft.Text(
            "Introducing Flet",
            size=40,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
            text_align=ft.TextAlign.CENTER,
        )

        # Visual: [Placeholder1] + [Placeholder2] = [Flet Logo]
        visual_row = ft.Row(
            [
                ft.Container(
                    content=ft.Image(
                        src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Text("+", size=70, color="#ffffff"),
                ft.Container(
                    content=ft.Image(
                        src="https://cdn.iconscout.com/icon/free/png-256/free-flutter-logo-icon-download-in-svg-png-gif-file-formats--technology-social-media-vol-3-pack-logos-icons-2944876.png?f=webp",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                ),
                ft.Text("=", size=70, color="#ffffff"),
                ft.Container(
                    content=ft.Image(
                        src="https://flet.dev/img/logo.svg",
                        width=150,
                        height=150,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    alignment=ft.alignment.center,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20,
        )

        # Bullet points
        bullets = ft.Column(
            [
                ft.Row([
                    ft.Icon(ft.Icons.STAR, color="#EE2536"),
                    ft.Text("No Dart, JavaScript, and CSS", color="#ffffff", size=22),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Icon(ft.Icons.STAR, color="#EE2536"),
                    ft.Text("Python wrapper for Flutter widgets.", color="#ffffff", size=22),
                ], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Icon(ft.Icons.STAR, color="#EE2536"),
                    ft.Text("Built-in web server and hot reload", color="#ffffff", size=22),
                ], alignment=ft.MainAxisAlignment.CENTER),
            ],
            spacing=10,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
        # center the bullet list in its own container
        centered_bullets = ft.Container(
            content=bullets,
            alignment=ft.alignment.center,
            expand=True,
        )

        self.content = ft.Column(
            [
                ft.Container(height=60),
                title,
                ft.Container(height=40),
                visual_row,
                ft.Container(height=40),
                centered_bullets,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
        self.alignment = ft.alignment.center