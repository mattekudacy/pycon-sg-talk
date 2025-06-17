import flet as ft

class DemoPage5(ft.Container):
    def __init__(self, page: ft.Page = None):
        super().__init__()
        self.page = page
        self.bgcolor = "#1e1e1e"
        self.expand = True
        self.user_name_value = ""

        # Code side (left) with syntax highlighting
        code_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Code - User Name Dialog",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#4B8BBE",
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                # user_name = ft.TextField(label="Enter your name")
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("user_name ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("TextField", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("label", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"Enter your name"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text(")", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # page.dialog = ft.AlertDialog(
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("dialog ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("AlertDialog", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Properties with proper indentation
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("open", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("True", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("modal", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("True", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("title", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Text", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"Welcome!"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("content", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Column", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("([", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user_name", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("], ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("tight", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("True", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("actions", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=[", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ElevatedButton", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("text", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"Join chat"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                ft.Row([
                                    ft.Text("                      ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("on_click", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("join_click", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(")],", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("actions_alignment", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"end"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text(")", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                            ],
                            spacing=2,
                            scroll=ft.ScrollMode.AUTO,
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

        # Demo dialog components
        self.demo_user_name = ft.TextField(
            label="Enter your name",
            color="#000000",
            bgcolor="#ffffff"
        )

        def demo_join_click(e):
            self.user_name_value = self.demo_user_name.value or "Anonymous"
            if hasattr(self, 'demo_dialog') and self.demo_dialog:
                self.demo_dialog.open = False
            self.demo_status_text.value = f"Welcome, {self.user_name_value}! You can now chat."
            self.update()

        self.demo_dialog = ft.AlertDialog(
            open=False,
            modal=True,
            title=ft.Text("Welcome!", color="#000000"),
            content=ft.Column([self.demo_user_name], tight=True),
            actions=[ft.ElevatedButton(
                text="Join chat", 
                on_click=demo_join_click,
                bgcolor="#2196F3",
                color="#ffffff"
            )],
            actions_alignment="end",
        )

        self.demo_status_text = ft.Text(
            "Click 'Show Dialog' to see the welcome dialog that appears before entering chat",
            size=14,
            color="#000000",
        )

        def show_dialog_click(e):
            self.demo_dialog.open = True
            self.demo_user_name.value = ""
            self.update()

        show_dialog_button = ft.ElevatedButton(
            "Show Dialog",
            on_click=show_dialog_click,
            bgcolor="#4CAF50",
            color="#ffffff",
            width=200,
            height=50,
        )

        # Output side (right) - Dialog demo
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
                                ft.Text("Welcome Dialog Demo", size=12, color="#ffffff", weight=ft.FontWeight.BOLD),
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
                        content=ft.Column(
                            [
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            self.demo_status_text,
                                            ft.Container(height=30),
                                            show_dialog_button,
                                            # Add the dialog to this container
                                            self.demo_dialog,
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=20,
                                    ),
                                    expand=True,
                                    padding=30,
                                ),
                            ],
                            expand=True,
                        ),
                        bgcolor="#ffffff",
                        expand=True,
                        border_radius=ft.border_radius.only(bottom_left=8, bottom_right=8),
                    ),
                ],
                spacing=0,
                expand=True,
            ),
            width=400,
            height=400,
            border=ft.border.all(1, "#666666"),
            border_radius=8,
        )

        output_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Live Demo - Welcome Dialog",
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

        # Main content layout
        self.content = ft.Column(
            [
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
            scroll=ft.ScrollMode.AUTO,
        )

        self.alignment = ft.alignment.center