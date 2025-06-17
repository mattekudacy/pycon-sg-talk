import flet as ft

class DemoPage1(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        # Title
        title = ft.Text(
            "Live Demo: Building a Chat App",
            size=40,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
            text_align=ft.TextAlign.CENTER,
        )

        # Code side (left) with syntax highlighting
        code_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Code",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#4B8BBE",
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                # Line 1: import statement
                                ft.Row([
                                    ft.Text("import ", size=14, color="#C586C0", font_family="Consolas, monospace"),
                                    ft.Text("flet ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("as ", size=14, color="#C586C0", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Empty line
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Line 3: function definition
                                ft.Row([
                                    ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("main", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(": ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Page", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 4: page.add call
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),  # indentation
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("add", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Text", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("value", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"Hello, world!"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text("))", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Empty line
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Line 6: ft.app call
                                ft.Row([
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("app", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("main", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(")", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                            ],
                            spacing=2,
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                        ),
                        bgcolor="#1E1E1E",
                        border_radius=8,
                        padding=20,
                        border=ft.border.all(2, "#4B8BBE"),
                        expand=True,
                    ),
                ],
                spacing=10,
                expand=True,
            ),
            padding=20,
            expand=True,
        )

        # Output side (right)
        output_window = ft.Container(
            content=ft.Column(
                [
                    # Window title bar
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Row([
                                    ft.Container(width=12, height=12, bgcolor="#ff5f56", border_radius=6),
                                    ft.Container(width=12, height=12, bgcolor="#ffbd2e", border_radius=6),
                                    ft.Container(width=12, height=12, bgcolor="#27ca3f", border_radius=6),
                                ], spacing=8),
                                ft.Text("Flet App", size=12, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ft.Container(expand=True),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor="#3c3c3c",
                        padding=10,
                        border_radius=ft.border_radius.only(top_left=8, top_right=8),
                    ),
                    # Window content
                    ft.Container(
                        content=ft.Text(
                            "Hello, world!",
                            size=16,
                            color="#000000",
                        ),
                        bgcolor="#ffffff",
                        padding=20,
                        expand=True,
                        border_radius=ft.border_radius.only(bottom_left=8, bottom_right=8),
                        alignment=ft.alignment.top_left,
                    ),
                ],
                spacing=0,
                expand=True,
            ),
            width=400,
            height=300,
            border=ft.border.all(1, "#666666"),
            border_radius=8,
        )

        output_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Output",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#4B8BBE",
                    ),
                    ft.Container(
                        content=output_window,
                        alignment=ft.alignment.center,
                        expand=True,
                    ),
                ],
                spacing=10,
                expand=True,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=20,
            expand=True,
        )

        # Main content with responsive layout
        content = ft.Column(
            [
                ft.Container(height=20),
                title,
                ft.Container(height=20),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=code_section,
                            col={"sm": 12, "md": 6, "lg": 6},
                        ),
                        ft.Container(
                            content=output_section,
                            col={"sm": 12, "md": 6, "lg": 6},
                        ),
                    ],
                    spacing=0,
                ),
            ],
            expand=True,
        )

        self.content = content
        self.alignment = ft.alignment.center