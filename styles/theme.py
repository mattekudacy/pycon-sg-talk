# Contents of /flet-presentation/flet-presentation/src/styles/theme.py

class Theme:
    primary_color = "#306998"  # Python blue
    secondary_color = "#FFD43B"  # Python yellow
    background_color = "#F5F5F5"  # Light gray background
    text_color = "#000000"  # Black text
    font_family = "Arial, sans-serif"
    font_size = 16

    @staticmethod
    def get_styles():
        return {
            "primary_color": Theme.primary_color,
            "secondary_color": Theme.secondary_color,
            "background_color": Theme.background_color,
            "text_color": Theme.text_color,
            "font_family": Theme.font_family,
            "font_size": Theme.font_size,
        }