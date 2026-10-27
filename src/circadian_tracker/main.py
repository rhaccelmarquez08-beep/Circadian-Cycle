"""
Module: main
Description: Main entry point to launch the web/desktop application.
"""

import os
import sys
import flet as ft

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ui_views import CircadianView


def main(page: ft.Page):
    """Initializes the graphical user interface by adding the main view to the page."""
    view = CircadianView(page)
    page.add(view.build())


if __name__ == "__main__":
    # Point to the assets folder absolutely so it never fails
    assets_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../assets")
    )
    ft.run(main, assets_dir=assets_path)