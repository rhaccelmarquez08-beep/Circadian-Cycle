"""
Módulo: ui_views
Descripción: Componentes visuales y páginas de la aplicación con la temática
             "Dulces Sueños" (colores azul pastel, lavanda y ovejita).
"""

import datetime
import os
import sys
import flet as ft

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from circadian_logic import CircadianPhase, CircadianTracker

# Constantes de diseño y paleta de colores azul pastel
BG_COLOR = "#EBF3FA"  # Azul pastel muy suave de fondo
CARD_BG = "#FFFFFF"  # Tarjetas en blanco limpio
PRIMARY_BLUE = "#4B6B94"  # Azul sereno principal
ACCENT_LAVENDER = "#8A79AF"  # Lavanda para detalles
PASTEL_CREAM = "#FFF8E7"  # Crema cálido
TEXT_DARK = "#2C3E50"  # Texto oscuro para alta legibilidad
TEXT_MUTED = "#6C7A89"  # Texto secundario


class CircadianView:
    """Componente visual principal con navegación personalizada e interfaz temática."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.tracker = CircadianTracker()

        # Configuración estética global de la ventana
        self.page.title = "Dulces Sueños - Rastreador de Ciclo Circadiano"
        self.page.window.width = 480
        self.page.window.height = 760
        self.page.bgcolor = BG_COLOR
        self.page.padding = 15

        # Componentes interactivos del simulador
        current_hour = datetime.datetime.now().hour
        self.time_slider = ft.Slider(
            min=0,
            max=23,
            divisions=23,
            value=current_hour,
            active_color=PRIMARY_BLUE,
            inactive_color="#CBD8E6",
            on_change=self.handle_slider_change,
        )

        self.hour_display = ft.Text(
            value="",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=PRIMARY_BLUE,
            text_align=ft.TextAlign.CENTER,
        )

        self.phase_name_text = ft.Text(
            value="",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ACCENT_LAVENDER,
        )
        self.description_text = ft.Text(value="", size=14, color=TEXT_DARK)
        self.recommendation_text = ft.Text(value="", size=14, color=TEXT_DARK)

        # Contenedor dinámico para el cuerpo de la pestaña activa
        self.body_container = ft.Container(expand=True)

    def _build_home_tab(self) -> ft.Container:
        """Página de Inicio con la ovejita y presentación general."""
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Container(
                        content=ft.Row(
                            [
                                ft.Icon(
                                    ft.Icons.BEDTIME_ROUNDED,
                                    color=ACCENT_LAVENDER,
                                    size=28,
                                ),
                                ft.Text(
                                    "Dulces Sueños",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                    color=PRIMARY_BLUE,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ),
                    ft.Container(height=5),
                    # Tarjeta central con la ovejita cargada desde assets
                    ft.Card(
                        elevation=2,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=15,
                            border_radius=15,
                            content=ft.Column(
                                controls=[
                                    ft.Image(
                                        src="descarga.jpg",
                                        width=160,
                                        height=160,
                                        fit="contain",
                                    ),
                                    ft.Container(height=5),
                                    ft.Text(
                                        "¿Qué es el Ciclo Circadiano?",
                                        size=17,
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                    ),
                                    ft.Text(
                                        "Es nuestro 'reloj biológico' interno de 24 horas que regula los patrones de sueño, la liberación de hormonas y la energía corporal.",
                                        size=12,
                                        color=TEXT_DARK,
                                        text_align=ft.TextAlign.CENTER,
                                    ),
                                ],
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            ),
                        ),
                    ),
                    ft.Container(height=5),
                    ft.Card(
                        elevation=1,
                        bgcolor=PASTEL_CREAM,
                        content=ft.Container(
                            padding=12,
                            border_radius=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "🌟 ¿Por qué es importante cuidarlo?",
                                        size=14,
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                    ),
                                    ft.Text(
                                        "Mantenerlo sincronizado mejora la calidad del descanso, optimiza la concentración diurna, equilibra el ánimo y fortalece el sistema inmunológico.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
            ),
        )

    def _build_simulator_tab(self) -> ft.Container:
        """Página del Simulador e Interfaz de Etapas del Ciclo."""
        self.update_phase_display(int(self.time_slider.value))

        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Etapas del Ciclo",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "Arrastra la barra para explorar la hora:",
                        size=12,
                        color=TEXT_MUTED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    self.time_slider,
                    self.hour_display,
                    ft.Divider(color="#D0E0F0", height=10),
                    # Tarjeta informativa de la fase activa
                    ft.Card(
                        elevation=2,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=15,
                            border_radius=15,
                            content=ft.Column(
                                controls=[
                                    ft.ListTile(
                                        leading=ft.Icon(
                                            ft.Icons.NIGHTLIGHT_ROUND,
                                            color=ACCENT_LAVENDER,
                                            size=26,
                                        ),
                                        title=self.phase_name_text,
                                        subtitle=ft.Text(
                                            "Estado de la Fase Circadiana",
                                            color=TEXT_MUTED,
                                            size=12,
                                        ),
                                    ),
                                    ft.Divider(color="#EBF3FA", height=5),
                                    ft.Text(
                                        "Descripción Fisiológica:",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=13,
                                    ),
                                    self.description_text,
                                    ft.Container(height=5),
                                    ft.Text(
                                        "Recomendación para tu Bienestar:",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=13,
                                    ),
                                    self.recommendation_text,
                                ]
                            ),
                        ),
                    ),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8,
            ),
        )

    def _build_functions_tab(self) -> ft.Container:
        """Página Anexa 1: Funciones Principales."""
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Funciones Principales",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "¿Cómo opera el ritmo circadiano en tu organismo?",
                        size=12,
                        color=TEXT_MUTED,
                    ),
                    ft.Container(height=5),
                    ft.Card(
                        elevation=1,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "☀️ Captación de Luz Solar",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Los ojos perciben la luz matutina y envían señales al Núcleo Supraquiasmático (NSQ) en el cerebro para suprimir la melatonina e iniciar el día.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                    ft.Card(
                        elevation=1,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "🔄 Regulación Hormonal Dual",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=14,
                                    ),
                                    ft.Text(
                                        "El Cortisol nos brinda energía durante el día, mientras que la Melatonina nos induce al sueño reparador al caer la noche.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                    ft.Card(
                        elevation=1,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "🌡️ Temperatura y Regeneración",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Durante la noche la temperatura corporal baja para permitir la limpieza celular cerebral y la consolidación del aprendizaje.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                ],
                spacing=8,
            ),
        )

    def _build_variables_tab(self) -> ft.Container:
        """Página Anexa 2: Variables que lo desequilibran."""
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Variables que lo desequilibran",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "Factores habituales que rompen la armonía del sueño:",
                        size=12,
                        color=TEXT_MUTED,
                    ),
                    ft.Container(height=5),
                    ft.Card(
                        elevation=1,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "📱 Luz Azul Nocturna",
                                        weight=ft.FontWeight.BOLD,
                                        color="#C0392B",
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Pantallas de celulares o computadoras antes de dormir engañan al cerebro haciéndole creer que aún es de día.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                    ft.Card(
                        elevation=1,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "☕ Cafeína Tardía",
                                        weight=ft.FontWeight.BOLD,
                                        color="#C0392B",
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Consumir café o energizantes después de las 2:00 P.M. bloquea los receptores de adenosina que causan somnolencia natural.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                    ft.Card(
                        elevation=1,
                        bgcolor=CARD_BG,
                        content=ft.Container(
                            padding=12,
                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "⏰ Horarios Irregulares",
                                        weight=ft.FontWeight.BOLD,
                                        color="#C0392B",
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Dormir y despertar a horas muy variables genera 'Jet Lag social' y desorienta la secreción hormonal.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                ],
                spacing=8,
            ),
        )

    def switch_tab(self, tab_index: int) -> None:
        """Función interna para cambiar de vista al hacer clic en los botones de navegación."""
        if tab_index == 0:
            self.body_container.content = self._build_home_tab()
        elif tab_index == 1:
            self.body_container.content = self._build_simulator_tab()
        elif tab_index == 2:
            self.body_container.content = self._build_functions_tab()
        elif tab_index == 3:
            self.body_container.content = self._build_variables_tab()
        self.body_container.update()

    def create_nav_pill(self, text: str, icon, index: int) -> ft.Container:
        """Crea un botón de navegación personalizado con diseño tipo píldora pastel."""
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, size=16, color=PRIMARY_BLUE),
                    ft.Text(text, size=12, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=4,
            ),
            padding=8,
            bgcolor=PASTEL_CREAM,
            border_radius=10,
            on_click=lambda e: self.switch_tab(index),
        )

    def build(self) -> ft.Column:
        """Ensambla la barra de navegación personalizada y el contenedor principal."""
        self.body_container.content = self._build_home_tab()

        nav_bar = ft.Row(
            controls=[
                self.create_nav_pill("Inicio", ft.Icons.HOME_ROUNDED, 0),
                self.create_nav_pill("Simulador", ft.Icons.ACCESS_TIME_ROUNDED, 1),
                self.create_nav_pill("Funciones", ft.Icons.AUTO_AWESOME_ROUNDED, 2),
                self.create_nav_pill("Desequilibrios", ft.Icons.WARNING_AMBER_ROUNDED, 3),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )

        return ft.Column(
            controls=[nav_bar, ft.Divider(height=10, color="#CBD8E6"), self.body_container],
            expand=True,
        )

    def handle_slider_change(self, e: ft.ControlEvent) -> None:
        """Manejador de evento interactivo cuando cambia la hora en el slider."""
        selected_hour = int(e.control.value)
        self.update_phase_display(selected_hour)

    def update_phase_display(self, hour: int) -> None:
        """Actualiza el contenido de los textos usando formato regular de 12 horas (A.M. / P.M.)."""
        current_phase: CircadianPhase = self.tracker.get_current_phase(hour)
        formatted_time = self.tracker.format_to_12h(hour)

        self.hour_display.value = f"Hora Seleccionada: {formatted_time}"
        self.phase_name_text.value = current_phase.name
        self.description_text.value = current_phase.description
        self.recommendation_text.value = current_phase.recommendation

        self.page.update()