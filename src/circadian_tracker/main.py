"""
Módulo: main
Descripción: Punto de entrada principal para lanzar la aplicación web/escritorio.
"""

import os
import sys
import flet as ft

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from ui_views import CircadianView


def main(page: ft.Page):
    """Inicializa la interfaz gráfica agregando la vista principal a la página."""
    view = CircadianView(page)
    page.add(view.build())


if __name__ == "__main__":
    # Apuntamos la carpeta assets de forma absoluta para que nunca falle
    assets_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../../assets")
    )
    ft.run(main, assets_dir=assets_path)