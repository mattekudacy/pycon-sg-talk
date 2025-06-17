import flet as ft

class WhenToUsePage(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        # Title
        title = ft.Text(
            "When to Use Flet",
            size=36,
            weight=ft.FontWeight.BOLD,
            color="#FFD43B",
            text_align=ft.TextAlign.CENTER,
        )

        # Left side - DO's (When to use Flet)
        dos_title = ft.Text(
            "✅ Use Flet When:",
            size=24,
            weight=ft.FontWeight.BOLD,
            color="#4CAF50",
        )

        dos_items = [
            "Building quick prototypes and MVPs",
            "Creating desktop apps with web technologies",
            "Need cross-platform compatibility (Windows, macOS, Linux)",
            "Want to leverage Python ecosystem and libraries",
            "Building internal tools and dashboards",
            "Creating data visualization applications",
            "Need real-time features (WebSockets, PubSub)",
            "Want rapid development with minimal setup",
            "Building educational or learning applications",
            "Creating simple to medium complexity UIs",
        ]

        dos_column = ft.Column([
            dos_title,
            ft.Container(height=20),
            *[ft.Row([
                ft.Icon(ft.Icons.CHECK_CIRCLE, color="#4CAF50", size=16),
                ft.Text(item, size=14, color="#ffffff", expand=True)
            ], spacing=10) for item in dos_items]
        ], spacing=8)

        # Right side - DON'Ts (When NOT to use Flet)
        donts_title = ft.Text(
            "❌ Avoid Flet When:",
            size=24,
            weight=ft.FontWeight.BOLD,
            color="#F44336",
        )

        donts_items = [
            "Building high-performance games or graphics apps",
            "Need native mobile app features (camera, GPS, etc.)",
            "Creating complex enterprise applications",
            "Require extensive customization of UI components",
            "Building apps with heavy computational requirements",
            "Need offline-first mobile applications",
            "Working with large teams needing strict UI guidelines",
            "Building consumer-facing mobile apps for app stores",
            "Require advanced animations and transitions",
            "Need integration with platform-specific APIs",
        ]

        donts_column = ft.Column([
            donts_title,
            ft.Container(height=20),
            *[ft.Row([
                ft.Icon(ft.Icons.CANCEL, color="#F44336", size=16),
                ft.Text(item, size=14, color="#ffffff", expand=True)
            ], spacing=10) for item in donts_items]
        ], spacing=8)

        # Main content layout
        self.content = ft.Column(
            [
                ft.Container(height=30),
                title,
                ft.Container(height=40),
                ft.ResponsiveRow(
                    [
                        ft.Container(
                            content=ft.Container(
                                content=dos_column,
                                padding=30,
                                bgcolor="#1a4d2e",
                                border_radius=12,
                                border=ft.border.all(2, "#4CAF50"),
                            ),
                            col={"sm": 12, "md": 6, "lg": 6},
                        ),
                        ft.Container(
                            content=ft.Container(
                                content=donts_column,
                                padding=30,
                                bgcolor="#4d1a1a",
                                border_radius=12,
                                border=ft.border.all(2, "#F44336"),
                            ),
                            col={"sm": 12, "md": 6, "lg": 6},
                        ),
                    ],
                    spacing=20,
                ),
                ft.Container(height=50),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            scroll=ft.ScrollMode.AUTO,
        )

        self.alignment = ft.alignment.center
        self.padding = 40