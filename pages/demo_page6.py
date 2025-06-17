import flet as ft

class DemoPage6(ft.Container):
    def __init__(self, page: ft.Page = None):
        super().__init__()
        self.page = page
        self.bgcolor = "#1e1e1e"
        self.expand = True

        # Code side (left) with syntax highlighting for ChatMessage class with CircleAvatar
        code_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Code - Chat with CircleAvatar",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color="#4B8BBE",
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                # class ChatMessage(ft.Row):
                                ft.Row([
                                    ft.Text("class ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("ChatMessage", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Row", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # def __init__(self, message: Message):
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("__init__", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(": ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Message", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # super().__init__()
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("super", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("__init__", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # self.controls = [
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("controls ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("[", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ft.CircleAvatar(
                                ft.Row([
                                    ft.Text("            ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("CircleAvatar", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # content=ft.Text(self.get_initials(message.user_name)),
                                ft.Row([
                                    ft.Text("                ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("content", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Text", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("get_initials", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user_name", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(")),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # color=ft.Colors.WHITE,
                                ft.Row([
                                    ft.Text("                ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("color", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Colors", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("WHITE", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # bgcolor=self.get_avatar_color(message.user_name),
                                ft.Row([
                                    ft.Text("                ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("bgcolor", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("get_avatar_color", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user_name", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ),
                                ft.Row([
                                    ft.Text("            ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ft.Column([
                                ft.Row([
                                    ft.Text("            ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Column", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("([", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ft.Text(message.user_name, weight="bold"),
                                ft.Row([
                                    ft.Text("                ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Text", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user_name", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("weight", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"bold"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ft.Text(message.text, selectable=True),
                                ft.Row([
                                    ft.Text("                ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Text", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("text", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("selectable", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("True", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ], tight=True, spacing=5),
                                ft.Row([
                                    ft.Text("            ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("], ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("tight", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("True", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("spacing", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("5", size=14, color="#B5CEA8", font_family="Consolas, monospace"),
                                    ft.Text("),", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # ]
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("]", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # def get_initials(self, user_name: str):
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("get_initials", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user_name", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(": ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("str", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # return user_name[:1].capitalize()
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("return ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("user_name", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("[:", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("1", size=14, color="#B5CEA8", font_family="Consolas, monospace"),
                                    ft.Text("]", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("capitalize", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
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

        # Demo Message class for the interactive demo
        class Message:
            def __init__(self, user_name: str, text: str):
                self.user_name = user_name
                self.text = text

        # Demo ChatMessage class with CircleAvatar
        class DemoChatMessage(ft.Row):
            def __init__(self, message: Message):
                super().__init__()
                self.vertical_alignment = ft.CrossAxisAlignment.START
                self.controls = [
                    ft.CircleAvatar(
                        content=ft.Text(self.get_initials(message.user_name)),
                        color=ft.Colors.WHITE,
                        bgcolor=self.get_avatar_color(message.user_name),
                    ),
                    ft.Column(
                        [
                            ft.Text(message.user_name, weight="bold", color="#000000"),
                            ft.Text(message.text, selectable=True, color="#000000"),
                        ],
                        tight=True,
                        spacing=5,
                    ),
                ]

            def get_initials(self, user_name: str):
                return user_name[:1].capitalize()

            def get_avatar_color(self, user_name: str):
                colors_lookup = [
                    ft.Colors.AMBER,
                    ft.Colors.BLUE,
                    ft.Colors.BROWN,
                    ft.Colors.CYAN,
                    ft.Colors.GREEN,
                    ft.Colors.INDIGO,
                    ft.Colors.LIME,
                    ft.Colors.ORANGE,
                    ft.Colors.PINK,
                    ft.Colors.PURPLE,
                    ft.Colors.RED,
                    ft.Colors.TEAL,
                    ft.Colors.YELLOW,
                ]
                return colors_lookup[hash(user_name) % len(colors_lookup)]

        # Create interactive demo
        self.demo_chat = ft.Column(spacing=10)
        self.demo_text_field = ft.TextField(
            hint_text="Type a message...",
            height=40,
            expand=True,
            color="#000000"
        )

        def demo_send_click(e):
            if self.demo_text_field.value and self.demo_text_field.value.strip():
                self.demo_chat.controls.append(
                    DemoChatMessage(Message("You", self.demo_text_field.value))
                )
                self.demo_text_field.value = ""
                self.update()

        demo_send_button = ft.ElevatedButton(
            "Send",
            on_click=demo_send_click,
            height=40,
            bgcolor="#2196F3",
            color="#ffffff",
        )

        # Output side (right) - Chat with avatars demo
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
                                ft.Text("Chat with Avatars", size=12, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ft.Container(expand=True),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor="#3c3c3c",
                        padding=10,
                        border_radius=ft.border_radius.only(top_left=8, top_right=8),
                    ),
                    # Window content - Chat with avatars
                    ft.Container(
                        content=ft.Column(
                            [
                                # Chat area with scrolling
                                ft.Container(
                                    content=ft.Column(
                                        [self.demo_chat],
                                        scroll=ft.ScrollMode.AUTO,
                                        expand=True,
                                    ),
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
            width=450,
            height=500,
            border=ft.border.all(1, "#666666"),
            border_radius=8,
        )

        output_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Final Demo - With Avatars",
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