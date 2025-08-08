import flet as ft

class FinalPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        # Title
        title = ft.Text(
            "Thank You! 🐍",
            size=48,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
            text_align=ft.TextAlign.CENTER,
        )

        # QR Code placeholders
        chat_demo_qr = ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Image(
                        src='https://scontent-sin6-3.xx.fbcdn.net/v/t1.15752-9/507044452_583003261158769_2597776939878986352_n.png?_nc_cat=110&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeH2TNd6qnx57lvEExsLNIJItR1MXciHmyu1HUxdyIebK1pPl-b_9gWieybu_13BldLGrcAye1Uuri6zND_ulBu1&_nc_ohc=Ow4jRkLt-1UQ7kNvwH_pNMG&_nc_oc=Admr8SpSnyvnSIB_bK-5Toe99UcJI59Hjakz07MHH1hXgsbsS9o0g-r-hnSnR51DebI&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin6-3.xx&oh=03_Q7cD2gFgPIk8c_N8RDBQzbCNeNfZEpzrJsWXqMkWfC4QycntRA&oe=6878E988'
                    ),
                    width=300,
                    height=300,
                    bgcolor="#ffffff",
                    border_radius=12,
                    alignment=ft.alignment.center,
                    border=ft.border.all(2, "#4B8BBE"),
                ),
                ft.Text(
                    "Try the Chat Demo",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#FFD43B",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Live Flet Chat App",
                    size=12,
                    color="#ffffff",
                    text_align=ft.TextAlign.CENTER,
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10),
        )

        linkedin_qr = ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Image(
                        src='https://scontent-sin11-2.xx.fbcdn.net/v/t1.15752-9/507024335_740663708465796_6505929088619194074_n.png?_nc_cat=108&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeGx3QV6ggqJFQDQNNFDjlbX-2m8O6gc67L7abw7qBzrso_TFYIxXY68jRrXTv7ILqGWidbRiPc8wmEHPrUu7F5M&_nc_ohc=rK0T3ubjpPoQ7kNvwGmbY0B&_nc_oc=AdmCUgp_fxuHB2GQ8yRkqgrfbn03udD6T0aX_0081wKNFH8FkqorxmsocHPnQiDZbfw&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin11-2.xx&oh=03_Q7cD2gF8d0bLQouspA0yn9cpjakC8B2njIvVE-X7QF7FoUnbmQ&oe=68790815'
                    ),
                    width=300,
                    height=300,
                    bgcolor="#ffffff",
                    border_radius=12,
                    alignment=ft.alignment.center,
                    border=ft.border.all(2, "#4B8BBE"),
                ),
                ft.Text(
                    "Connect on LinkedIn",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#FFD43B",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "Let's connect!",
                    size=12,
                    color="#ffffff",
                    text_align=ft.TextAlign.CENTER,
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10),
        )

        flet_website_qr = ft.Container(
            content=ft.Column([
                ft.Container(
                    content=ft.Image(
                        src='https://scontent-sin11-2.xx.fbcdn.net/v/t1.15752-9/506949437_1436607674224585_1022003793948536217_n.png?_nc_cat=101&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeF5yImObYnswacm8r5m9ykF8RjEg9fhoN_xGMSD1-Gg39_d-8a1ibRGV7xgMLhxLw8t48VAqZVbsLdV_LJVRCVU&_nc_ohc=IuZuHzF5wt8Q7kNvwHuELE5&_nc_oc=AdnTvK8o-NjhNi049yIoTGnHlTTHj_mZ9ZxFooJSQ8DjJXtV75qIQJm0tAbGo_WiNFg&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent-sin11-2.xx&oh=03_Q7cD2gHbPi9v-l843-T7gxNhXz2cnOOkN2ObRg3eZoPRudN44Q&oe=68790C6E'
                    ),
                    width=300,
                    height=300,
                    bgcolor="#ffffff",
                    border_radius=12,
                    alignment=ft.alignment.center,
                    border=ft.border.all(2, "#4B8BBE"),
                ),
                ft.Text(
                    "Learn More",
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#FFD43B",
                    text_align=ft.TextAlign.CENTER,
                ),
                ft.Text(
                    "flet.dev",
                    size=12,
                    color="#ffffff",
                    text_align=ft.TextAlign.CENTER,
                ),
            ], 
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10),
        )

        # QR codes row
        qr_row = ft.Row([
            chat_demo_qr,
            linkedin_qr,
            flet_website_qr,
        ], 
        alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        spacing=50)

        # Main content
        self.content = ft.Column(
            [
                ft.Container(height=50),
                title,
                ft.Container(height=60),
                qr_row,
                ft.Container(height=50),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
        )

        self.alignment = ft.alignment.center