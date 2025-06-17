import flet as ft

class BTS(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        title = ft.Text(
            "Flet under the hood",
            size=40,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
            text_align=ft.TextAlign.CENTER,
        )

        meme_placeholder = ft.Container(
            content=ft.Image(
                src="https://flet.dev/img/blog/pglet-introduction/pglet-highlevel-design.png",
                fit=ft.ImageFit.FILL,
                expand=True,
            ),
            alignment=ft.alignment.center,
            expand=True,
            padding=5,
            bgcolor="#ffffff",
            margin=ft.margin.symmetric(horizontal=100)
        )

        self.content = ft.Column(
            [
                ft.Container(height=1),
                title,
                ft.Container(height=1),    
                meme_placeholder,
                ft.Container(height=50),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
        )
        self.alignment = ft.alignment.center