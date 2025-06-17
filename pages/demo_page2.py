import flet as ft

class DemoPage2(ft.Container):
    def __init__(self):
        super().__init__()
        
        # Python-themed colors
        self.bgcolor = "#1e1e1e"
        self.expand = True
        
        # Placeholder image on the right
        placeholder_image = ft.Container(
            content=ft.Image(
                src="https://scontent.fmnl4-6.fna.fbcdn.net/v/t1.15752-9/494826986_689023363920917_4851985287015109744_n.png?_nc_cat=111&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeGGriARQFq8mYUEbnSGq0MG9R8fE1YT6_z1Hx8TVhPr_Ekntz6IS1TQ4V_j11eefXrYmY9pFi12gOICCV8JbMa_&_nc_ohc=BIuYK4ukrLUQ7kNvwFjm2lg&_nc_oc=AdkqzFVY4WoiUd1x8dgulijGcgiGrKUlFYojvD3E1qCaQwkJ-_gUAQZz5nNk857Yf2Q&_nc_zt=23&_nc_ht=scontent.fmnl4-6.fna&oh=03_Q7cD2gEnkgUq1zV4yxGLlDfzWM-yHZqrZnu5wt3JQIVKkn22uA&oe=68748308",
                width=600,
                height=600,
            ),
            width=550,
            height=550,
            alignment=ft.alignment.center,
        )
        
        # Title
        intro_title = ft.Text(
            "Page Controls & Events",
            size=36,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
        )
        
        # Bullet points about controls and events
        bullet_points = ft.Column(
            [
                self._create_bullet_point("Column - a container to display chat messages (Text controls) vertically."),
                self._create_bullet_point("Text - chat message displayed in the chat Column."),
                self._create_bullet_point("TextField - input control used for taking new message input from the user."),
                self._create_bullet_point("ElevatedButton - Send button that will add new message to the chat Column."),
                self._create_bullet_point("Row - a container to display TextField and ElevatedButton horizontally."),
            ],
            spacing=20,
        )
        
        # Left side content
        left_content = ft.Container(
            content=ft.Column(
                [
                    intro_title,
                    ft.Container(height=40),
                    bullet_points,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=40,
            expand=True,
            alignment=ft.alignment.center,
        )

        # Right side content
        right_content = ft.Container(
            content=ft.Column(
                [placeholder_image],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40,
            expand=True,
            alignment=ft.alignment.center,
        )

        # Responsive layout
        self.content = ft.ResponsiveRow(
            [
                ft.Container(
                    content=left_content,
                    col={"sm": 12, "md": 6, "lg": 6},
                ),
                ft.Container(
                    content=right_content,
                    col={"sm": 12, "md": 6, "lg": 6},
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.alignment = ft.alignment.center
    
    def _create_bullet_point(self, text):
        return ft.Row(
            [
                ft.Icon(
                    ft.Icons.ARROW_RIGHT,
                    size=20,
                    color="#4B8BBE",
                ),
                ft.Text(
                    text,
                    size=18,
                    color="#ffffff",
                    weight=ft.FontWeight.W_400,
                ),
            ],
            spacing=10,
            tight=True,
        )