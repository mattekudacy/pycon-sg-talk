import flet as ft

class ThirdPage(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        title = ft.Text(
            "Building UIs in Python is... complicated",
            size=40,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
            text_align=ft.TextAlign.CENTER,
        )

        meme_placeholder = ft.Container(
            content=ft.Image(
                src="https://scontent.fmnl4-1.fna.fbcdn.net/v/t1.15752-9/494826857_1845255426256797_7432191229196974296_n.png?stp=dst-png_s480x480&_nc_cat=106&ccb=1-7&_nc_sid=0024fc&_nc_eui2=AeG6Ucrj42F14DLoby2HC-gw6DIFjkb_TYXoMgWORv9NhU4aAASgz3RVbz4H00xwQdsT9ZUT2JEfyr3kLBHdKTCH&_nc_ohc=ME_f8QIQHL0Q7kNvwFcVdKF&_nc_oc=Adm7Er9RH6so8Ot_VrlmgwunmkWhnJTM3woX_XC38mBmhaeXX5ZTKuq4dzyNbhpb1b6j3TY2op07hJFoLO4kSkyM&_nc_ad=z-m&_nc_cid=0&_nc_zt=23&_nc_ht=scontent.fmnl4-1.fna&oh=03_Q7cD2QGgHAYYx7thJe-6e2acSZnWe5q0CtDrAwfFuOTpxv-qBA&oe=68611981",
                fit=ft.ImageFit.CONTAIN,
                width=450,
                height=450,
            ),
            alignment=ft.alignment.center,
            width=450,
            height=450,
        )

        self.content = ft.Column(
            [
                ft.Container(height=30),
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