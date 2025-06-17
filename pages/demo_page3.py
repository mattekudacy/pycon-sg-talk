import flet as ft

class DemoPage3(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

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
                                
                                # Line 4: chat = ft.Column()
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("chat ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Column", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 5: new_message = ft.TextField()
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("new_message ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("TextField", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Empty line
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Line 7: def send_click(e):
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("send_click", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("e", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 8: chat.controls.append(ft.Text(new_message.value))
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("chat", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("controls", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("append", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Text", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("new_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("value", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("))", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 9: new_message.value = ""
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("new_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("value ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('""', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 10: page.update()
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("update", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Empty line
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Line 12: page.add(
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("add", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 13: chat, ft.Row(...)
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("chat", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Row", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("controls", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("[", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("new_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 14: ft.ElevatedButton("Send", on_click=send_click)])
                                ft.Row([
                                    ft.Text("             ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ElevatedButton", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"Send"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("on_click", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("send_click", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(")])", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Line 15: )
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text(")", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # Empty line
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Line 17: ft.app(main)
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

        # Create interactive demo for the output side
        self.demo_chat = ft.Column(spacing=5)
        self.demo_text_field = ft.TextField(
            hint_text="Type a message...",
            # size=14,
            height=40,
            expand=True,
            color="#000000"
        )

        def demo_send_click(e):
            if self.demo_text_field.value and self.demo_text_field.value.strip():
                self.demo_chat.controls.append(
                    ft.Text(
                        self.demo_text_field.value,
                        size=14,
                        color="#000000",
                    )
                )
                self.demo_text_field.value = ""
                self.page.update()

        demo_send_button = ft.ElevatedButton(
            "Send",
            on_click=demo_send_click,
            height=40,
            bgcolor="#2196F3",
            color="#ffffff",
        )

        # Output side (right) - Interactive demo
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
                                ft.Text("Flet Chat Demo", size=12, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ft.Container(expand=True),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor="#3c3c3c",
                        padding=10,
                        border_radius=ft.border_radius.only(top_left=8, top_right=8),
                    ),
                    # Window content - Interactive chat
                    ft.Container(
                        content=ft.Column(
                            [
                                # Chat area
                                ft.Container(
                                    content=self.demo_chat,
                                    expand=True,
                                    padding=10,
                                ),
                                # Input area
                                ft.Container(
                                    content=ft.Row(
                                        [
                                            self.demo_text_field,
                                            demo_send_button,
                                        ],
                                        spacing=10,
                                    ),
                                    padding=10,
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
            height=350,
            border=ft.border.all(1, "#666666"),
            border_radius=8,
        )

        output_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Live Demo",
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
            scroll=ft.ScrollMode.AUTO,  # Make the whole page scrollable
        )

        self.alignment = ft.alignment.center