import flet as ft

class IntroPage(ft.Container):
    def __init__(self):
        super().__init__()
        
        # Python-themed colors
        self.bgcolor = "#1e1e1e"
        self.expand = True
        
        # Profile picture with better positioning
        profile_image = ft.Container(
            content=ft.Image(
                src="https://scontent.fmnl25-1.fna.fbcdn.net/v/t1.15752-9/494579001_1427789348399021_4407207066484989773_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeH3GadJvmRpjdvfRhEzZg2YGrHeq0SnMhYasd6rRKcyFj_4Nvr2ooOQNaJti39BdIXVt7Sa4yI6WhMFxh50eKGk&_nc_ohc=2MTLVImukm4Q7kNvwHbXIRg&_nc_oc=AdlT5ceLJPqtbBpsNZT4Wfxse3YZbfbbJ0fHJj6KsWvrhn3s6F0Tg3iKNwjqtAaxELw&_nc_zt=23&_nc_ht=scontent.fmnl25-1.fna&oh=03_Q7cD2gGFIGIMgHklqZBYitjD7j2-nEaaFAuGu4OX6DUaf-asGA&oe=687247F9",
                width=450,
                height=450,
                fit=ft.ImageFit.COVER,  # Changed from COVER to CONTAIN
                border_radius=ft.border_radius.all(250),  # Adjusted to match container
            ),
            width=450,  # Reduced size
            height=450,  # Reduced size
            bgcolor="#2d2d2d",
            border_radius=250,  # Adjusted border radius
            alignment=ft.alignment.center,
            border=ft.border.all(4, "#4B8BBE"),  # Added Python yellow border   
        )
        
        # Introduction content
        intro_title = ft.Text(
            "Hi, I'm Cy!👋",
            size=36,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
        )
        
        # Bullet points about what you do
        bullet_points = ft.Column(
            [
                self._create_bullet_point("💻 AI/ML Computational Science Analyst @ Accenture"),
                self._create_bullet_point("🐍 Python Philippines Volunteer since 2023"),
                self._create_bullet_point("🌐 PyCon APAC 2025 Co-Chairman"),
                self._create_bullet_point("📱 Instructor and Mentor"),
            ],
            spacing=15,
        )
        
        # Left side content
        left_content = ft.Container(
            content=ft.Column(
                [
                    intro_title,
                    ft.Container(height=30),
                    bullet_points,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Center horizontally
            ),
            padding=40,
            expand=True,
            alignment=ft.alignment.center,  # Center container content
        )

        # Right side content
        right_content = ft.Container(
            content=ft.Column(
                [profile_image],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=40,
            expand=True,
            alignment=ft.alignment.center,  # Center container content
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
            alignment=ft.MainAxisAlignment.CENTER,  # Center the row
            vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Center vertically
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
                    size=20,
                    color="#ffffff",
                    weight=ft.FontWeight.W_400,
                ),
            ],
            spacing=10,
            tight=True,
        )