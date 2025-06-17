import flet as ft


class Message:
    def __init__(self, user_name: str, text: str, message_type: str):
        self.user_name = user_name
        self.text = text
        self.message_type = message_type


class ChatMessage(ft.Row):
    def __init__(self, message: Message):
        super().__init__()
        self.vertical_alignment = ft.CrossAxisAlignment.START
        self.controls = [
            ft.CircleAvatar(
                content=ft.Text(
                    self.get_initials(message.user_name),
                    color=ft.Colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                ),
                color=ft.Colors.WHITE,
                bgcolor=self.get_avatar_color(message.user_name),
                radius=20,
            ),
            ft.Column(
                [
                    ft.Text(
                        message.user_name, 
                        weight=ft.FontWeight.BOLD,
                        color="#FFD43B",  # Python yellow
                        size=14,
                    ),
                    ft.Container(
                        content=ft.Text(
                            message.text, 
                            selectable=True,
                            color=ft.Colors.WHITE,
                            size=13,
                        ),
                        bgcolor="#2B2B2B",  # Dark background like Python IDE
                        padding=10,
                        border_radius=8,
                        border=ft.border.all(1, "#4B8BBE"),  # Python blue border
                    ),
                ],
                tight=True,
                spacing=5,
            ),
        ]

    def get_initials(self, user_name: str):
        if user_name:
            return user_name[:1].capitalize()
        else:
            return "U"

    def get_avatar_color(self, user_name: str):
        # Python/Singapore themed colors
        colors_lookup = [
            "#4B8BBE",  # Python blue
            "#FFD43B",  # Python yellow
            "#DC143C",  # Singapore red
            "#306998",  # Python dark blue
            "#FF6B35",  # Singapore orange
            "#4CAF50",  # Green
            "#9C27B0",  # Purple
            "#FF9800",  # Orange
            "#607D8B",  # Blue grey
            "#795548",  # Brown
            "#E91E63",  # Pink
            "#009688",  # Teal
        ]
        return colors_lookup[hash(user_name) % len(colors_lookup)]


def main(page: ft.Page):
    # Python/Singapore themed page setup
    page.title = "🐍 PyCon SG Chat"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1E1E1E"  # Dark Python IDE background
    page.horizontal_alignment = ft.CrossAxisAlignment.STRETCH
    
    # Custom theme colors
    page.theme = ft.Theme(
        color_scheme_seed="#4B8BBE",  # Python blue
        color_scheme=ft.ColorScheme(
            primary="#4B8BBE",
            secondary="#FFD43B",
            surface="#2B2B2B",
            background="#1E1E1E",
        )
    )

    def join_chat_click(e):
        if not join_user_name.value:
            join_user_name.error_text = "Name cannot be blank!"
            join_user_name.update()
        else:
            page.session.set("user_name", join_user_name.value)
            welcome_dlg.open = False
            new_message.prefix = ft.Text(
                f"{join_user_name.value}: ", 
                color="#FFD43B",
                weight=ft.FontWeight.BOLD,
            )
            page.pubsub.send_all(
                Message(
                    user_name=join_user_name.value,
                    text=f"🎉 {join_user_name.value} has joined the chat!",
                    message_type="login_message",
                )
            )
            page.update()

    def send_message_click(e):
        if new_message.value != "":
            page.pubsub.send_all(
                Message(
                    page.session.get("user_name"),
                    new_message.value,
                    message_type="chat_message",
                )
            )
            new_message.value = ""
            new_message.focus()
            page.update()

    def on_message(message: Message):
        if message.message_type == "chat_message":
            m = ChatMessage(message)
        elif message.message_type == "login_message":
            m = ft.Container(
                content=ft.Text(
                    message.text, 
                    italic=True, 
                    color="#FFD43B",
                    size=12,
                    text_align=ft.TextAlign.CENTER,
                ),
                bgcolor="#2B2B2B",
                padding=8,
                border_radius=15,
                margin=ft.margin.symmetric(horizontal=50),
                border=ft.border.all(1, "#4B8BBE"),
            )
        chat.controls.append(m)
        page.update()

    page.pubsub.subscribe(on_message)

    # Themed dialog
    join_user_name = ft.TextField(
        label="Enter your name to join PyCon SG Chat",
        autofocus=True,
        on_submit=join_chat_click,
        bgcolor="#2B2B2B",
        color=ft.Colors.WHITE,
        label_style=ft.TextStyle(color="#FFD43B"),
        border_color="#4B8BBE",
        focused_border_color="#FFD43B",
    )
    
    welcome_dlg = ft.AlertDialog(
        open=True,
        modal=True,
        bgcolor="#1E1E1E",
        title=ft.Text(
            "🐍 Welcome to PyCon SG Chat! 🇸🇬", 
            color="#FFD43B",
            weight=ft.FontWeight.BOLD,
        ),
        content=ft.Column([join_user_name], width=350, height=70, tight=True),
        actions=[
            ft.ElevatedButton(
                text="Join Chat 🚀",
                on_click=join_chat_click,
                bgcolor="#4B8BBE",
                color=ft.Colors.WHITE,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(radius=8),
                ),
            )
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    page.overlay.append(welcome_dlg)

    # Chat messages container with Python theme
    chat = ft.ListView(
        expand=True,
        spacing=15,
        auto_scroll=True,
        padding=15,
    )

    # Themed message input
    new_message = ft.TextField(
        hint_text="Type your message here... 💬",
        autofocus=True,
        shift_enter=True,
        min_lines=1,
        max_lines=5,
        filled=True,
        expand=True,
        on_submit=send_message_click,
        bgcolor="#2B2B2B",
        color=ft.Colors.WHITE,
        hint_style=ft.TextStyle(color="#888888"),
        border_color="#4B8BBE",
        focused_border_color="#FFD43B",
        border_radius=12,
    )

    # Main chat header
    header = ft.Container(
        content=ft.Row([
            ft.Icon(ft.Icons.CHAT, color="#FFD43B", size=24),
            ft.Text(
                "🐍 PyCon SG Live Chat 🇸🇬",
                size=20,
                weight=ft.FontWeight.BOLD,
                color="#FFD43B",
            ),
            ft.Container(expand=True),
            ft.Icon(ft.Icons.PEOPLE, color="#4B8BBE", size=20),
        ]),
        bgcolor="#2B2B2B",
        padding=15,
        border_radius=ft.border_radius.only(top_left=12, top_right=12),
        border=ft.border.all(1, "#4B8BBE"),
    )

    # Add everything to the page with Python theme
    page.add(
        ft.Column([
            header,
            ft.Container(
                content=chat,
                border=ft.border.only(
                    left=ft.BorderSide(1, "#4B8BBE"),
                    right=ft.BorderSide(1, "#4B8BBE"),
                    bottom=ft.BorderSide(1, "#4B8BBE"),
                ),
                border_radius=ft.border_radius.only(bottom_left=12, bottom_right=12),
                bgcolor="#1A1A1A",
                expand=True,
            ),
            ft.Container(
                content=ft.Row([
                    new_message,
                    ft.IconButton(
                        icon=ft.Icons.SEND_ROUNDED,
                        tooltip="Send message",
                        on_click=send_message_click,
                        bgcolor="#4B8BBE",
                        icon_color=ft.Colors.WHITE,
                        style=ft.ButtonStyle(
                            shape=ft.CircleBorder(),
                        ),
                    ),
                ], spacing=10),
                padding=15,
                bgcolor="#2B2B2B",
                border_radius=12,
                margin=ft.margin.only(top=10),
            ),
        ], expand=True)
    )


ft.app(target=main)