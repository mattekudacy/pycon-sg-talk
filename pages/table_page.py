import flet as ft

class TablePage(ft.Container):
    def __init__(self):
        super().__init__()
        self.bgcolor = "#1e1e1e"
        self.expand = True

        headers = ["Feature", "Flet", "Streamlit", "Tkinter", "PySide"]
        data = [
            ["Real-time sync", "✅", "❌", "❌", "❌"],
            ["Web support", "✅ (built-in)", "✅ (for data)", "❌", "❌"],
            ["Custom layout", "✅", "Limited", "✅", "✅"],
            ["Learning curve", "Low", "Very low", "Medium", "High"],
            ["Use case focus", "General apps", "Data apps", "Desktop only", "Desktop only"],
        ]

        # Header row
        table_rows = [
            ft.Row(
                [
                    ft.Container(
                        content=ft.Text(h, weight=ft.FontWeight.BOLD, color="#ffffff", size=18),
                        bgcolor="#4B8BBE",
                        padding=12,
                        border=ft.border.all(1, "#444"),
                        alignment=ft.alignment.center,
                        expand=True,
                    ) for h in headers
                ],
                expand=True,
            )
        ]

        # Data rows
        for row in data:
            cells = []
            for cell in row:
                cells.append(
                    ft.Container(
                        content=ft.Text(cell, color="#ffffff", size=16),
                        bgcolor="#232323",
                        padding=12,
                        border=ft.border.all(1, "#444"),
                        alignment=ft.alignment.center,
                        expand=True,
                    )
                )
            table_rows.append(
                ft.Row(
                    cells,
                    expand=True,
                )
            )

        padded_table = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        "Flet vs the World",
                        size=32,
                        weight=ft.FontWeight.BOLD,
                        color="#FFD43B",
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Container(height=20),
                    *table_rows,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True,
            ),
            padding=20,
            alignment=ft.alignment.center,
            expand=True,
        )

        self.content = padded_table
        self.alignment = ft.alignment.center