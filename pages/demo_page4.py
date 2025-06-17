import flet as ft

class DemoPage4(ft.Container):
    def __init__(self, page: ft.Page = None):
        super().__init__()
        self.page = page
        self.bgcolor = "#1e1e1e"
        self.expand = True

        # Code side (left) with syntax highlighting and red boxes for pubsub
        code_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Code - Real-time Chat with PubSub",
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
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Message class
                                ft.Row([
                                    ft.Text("class ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("Message", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("():", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("__init__", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(": ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("str", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("text", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(": ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("str", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("user", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                ], spacing=0),
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("self", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("text ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("text", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # Function definition
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
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # chat = ft.Column()
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("chat ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Column", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # new_message = ft.TextField()
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("new_message ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("TextField", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # def on_message(message: Message): - RED BOX
                                ft.Container(
                                    content=ft.Column([
                                        ft.Row([
                                            ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                            ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                            ft.Text("on_message", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                            ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(": ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("Message", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                            ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ], spacing=0),
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
                                            ft.Text('f"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text("{", size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("user", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text("}", size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text(": ", size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text("{", size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text("message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("text", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text("}", size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text('"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                            ft.Text("))", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ], spacing=0),
                                        ft.Row([
                                            ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                            ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("update", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                            ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ], spacing=0),
                                    ], spacing=2),
                                    border=ft.border.all(2, "#FF0000"),
                                    border_radius=5,
                                    padding=5,
                                ),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # page.pubsub.subscribe(on_message) - RED BOX
                                ft.Container(
                                    content=ft.Row([
                                        ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                        ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                        ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ft.Text("pubsub", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                        ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ft.Text("subscribe", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                        ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ft.Text("on_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                        ft.Text(")", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ], spacing=0),
                                    border=ft.border.all(2, "#FF0000"),
                                    border_radius=5,
                                    padding=5,
                                ),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # def send_click function with pubsub send_all - RED BOX
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("def ", size=14, color="#569CD6", font_family="Consolas, monospace"),
                                    ft.Text("send_click", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("e", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("):", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                # page.pubsub.send_all - RED BOX
                                ft.Container(
                                    content=ft.Column([
                                        ft.Row([
                                            ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                            ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("pubsub", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("send_all", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                            ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("Message", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                            ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("user", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("session_id", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ], spacing=0),
                                        ft.Row([
                                            ft.Text("                     ", size=14, font_family="Consolas, monospace"),
                                            ft.Text("text", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("new_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                            ft.Text("value", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                            ft.Text("))", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                        ], spacing=0),
                                    ], spacing=2),
                                    border=ft.border.all(2, "#FF0000"),
                                    border_radius=5,
                                    padding=5,
                                ),
                                
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("new_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("value ", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("= ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('""', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                ], spacing=0),
                                ft.Row([
                                    ft.Text("        ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("update", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("()", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # page.add
                                ft.Row([
                                    ft.Text("    ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("page", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("add", size=14, color="#DCDCAA", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("chat", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("Row", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("([", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("new_message", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(",", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                ft.Row([
                                    ft.Text("                 ", size=14, font_family="Consolas, monospace"),
                                    ft.Text("ft", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text(".", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("ElevatedButton", size=14, color="#4EC9B0", font_family="Consolas, monospace"),
                                    ft.Text("(", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text('"Send"', size=14, color="#CE9178", font_family="Consolas, monospace"),
                                    ft.Text(", ", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("on_click", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text("=", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                    ft.Text("send_click", size=14, color="#9CDCFE", font_family="Consolas, monospace"),
                                    ft.Text(")]))", size=14, color="#D4D4D4", font_family="Consolas, monospace"),
                                ], spacing=0),
                                
                                ft.Text("", size=14, font_family="Consolas, monospace"),
                                
                                # ft.app(main)
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

        # Create interactive demo for multi-user chat
        self.demo_chat = ft.Column(spacing=5)
        self.demo_text_field = ft.TextField(
            hint_text="Type a message...",
            height=40,
            expand=True,
            color="#000000"
        )
        # Message class for the demo
        class Message:
            def __init__(self, user: str, text: str):
                self.user = user
                self.text = text

        # Real pubsub message handler
        def on_message(message: Message):
            self.demo_chat.controls.append(
                ft.Text(
                    f"{message.user}: {message.text}",
                    size=14,
                    color="#000000",
                )
            )
            self.update()

        # Subscribe to pubsub messages if page is available
        if self.page:
            self.page.pubsub.subscribe(on_message)
        
        def demo_send_click(e):
            if self.demo_text_field.value and self.demo_text_field.value.strip():
                if self.page:
                    # Use real pubsub to send message to all connected clients
                    self.page.pubsub.send_all(Message(
                        user=self.page.session_id, 
                        text=self.demo_text_field.value
                    ))
                else:
                    # Fallback for when page is not available
                    self.demo_chat.controls.append(
                        ft.Text(
                            f"demo_user: {self.demo_text_field.value}",
                            size=14,
                            color="#000000",
                        )
                    )
                    self.update()
                
                self.demo_text_field.value = ""
                if self.page:
                    self.page.update()

        demo_send_button = ft.ElevatedButton(
            "Send",
            on_click=demo_send_click,
            height=40,
            bgcolor="#2196F3",
            color="#ffffff",
        )

        # Output side (right) - Multi-user chat demo
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
                                ft.Text("Multi-User Chat (PubSub)", size=12, color="#ffffff", weight=ft.FontWeight.BOLD),
                                ft.Container(expand=True),
                            ],
                            alignment=ft.MainAxisAlignment.START,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                        bgcolor="#3c3c3c",
                        padding=10,
                        border_radius=ft.border_radius.only(top_left=8, top_right=8),
                    ),
                    # Window content - Multi-user chat
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
            width=400,
            height=500,
            border=ft.border.all(1, "#666666"),
            border_radius=8,
        )

        output_section = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Live Demo - Real-time Chat",
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