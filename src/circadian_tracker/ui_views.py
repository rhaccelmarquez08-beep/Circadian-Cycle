"""
Module: ui_views
Description: Visual components and application pages with a "Sweet Dreams" theme.
             Supports desktop and web execution.
"""

import datetime
import os
import sys
import flet as ft

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from circadian_logic import CircadianPhase, CircadianTracker, fetch_songs_from_api

# Design constants and pastel color palette
BG_COLOR = "#EBF3FA"  # Very soft pastel blue background
CARD_BG = "#FFFFFF"  # Clean white cards
PRIMARY_BLUE = "#4B6B94"  # Main serene blue
ACCENT_LAVENDER = "#8A79AF"  # Lavender for details
PASTEL_CREAM = "#FFF8E7"  # Warm cream
TEXT_DARK = "#2C3E50"  # Dark text for high readability
TEXT_MUTED = "#6C7A89"  # Secondary text


class CircadianView:
    """Main visual component with custom navigation and themed UI for Web and Desktop."""

    def __init__(self, page: ft.Page):
        self.page = page
        self.tracker = CircadianTracker()

        # Global window aesthetic setup (compatible with web and desktop)
        self.page.title = "Sweet Dreams - Circadian Rhythm Tracker"
        self.page.window.width = 480
        self.page.window.height = 760
        self.page.bgcolor = BG_COLOR
        self.page.padding = 15

        # Simulator interactive components
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

        # Dynamic container for active tab body
        self.body_container = ft.Container(expand=True)

    def _build_home_tab(self) -> ft.Container:
        """Home page with the sheep illustration and general presentation."""
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
                                    "Sweet Dreams",
                                    size=22,
                                    weight=ft.FontWeight.BOLD,
                                    color=PRIMARY_BLUE,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                    ),
                    ft.Container(height=5),
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
                                        "What is the Circadian Cycle?",
                                        size=17,
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                    ),
                                    ft.Text(
                                        "It is our internal 24-hour 'biological clock' that regulates sleep patterns, hormone release, and body energy.",
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
                                        "🌟 Why is it important to take care of it?",
                                        size=14,
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                    ),
                                    ft.Text(
                                        "Keeping it synchronized improves rest quality, optimizes daytime focus, balances mood, and strengthens the immune system.",
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
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def _build_simulator_tab(self) -> ft.Container:
        """Simulator page and Cycle Stages interface."""
        self.update_phase_display(int(self.time_slider.value))

        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Cycle Stages",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "Drag the slider to explore the time:",
                        size=12,
                        color=TEXT_MUTED,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    self.time_slider,
                    self.hour_display,
                    ft.Divider(color="#D0E0F0", height=10),
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
                                            "Circadian Phase Status",
                                            color=TEXT_MUTED,
                                            size=12,
                                        ),
                                    ),
                                    ft.Divider(color="#EBF3FA", height=5),
                                    ft.Text(
                                        "Physiological Description:",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=13,
                                    ),
                                    self.description_text,
                                    ft.Container(height=5),
                                    ft.Text(
                                        "Wellness Recommendation:",
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
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def _build_functions_tab(self) -> ft.Container:
        """Main Functions Page (Annex 1)."""
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Main Functions",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "How does the circadian rhythm operate in your body?",
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
                                        "☀️ Sunlight Capture",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Eyes perceive morning light and send signals to the Suprachiasmatic Nucleus (SCN) in the brain to suppress melatonin and start the day.",
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
                                        "🔄 Dual Hormonal Regulation",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Cortisol provides energy during the day, while Melatonin induces restful sleep at nightfall.",
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
                                        "🌡️ Temperature & Regeneration",
                                        weight=ft.FontWeight.BOLD,
                                        color=PRIMARY_BLUE,
                                        size=14,
                                    ),
                                    ft.Text(
                                        "During the night, body temperature drops to allow cerebral cellular cleanup and memory consolidation.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                ],
                spacing=8,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def _build_variables_tab(self) -> ft.Container:
        """Disbalancing Variables Page (Annex 2)."""
        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Disbalancing Factors",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "Common factors that break sleep harmony:",
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
                                        "📱 Nighttime Blue Light",
                                        weight=ft.FontWeight.BOLD,
                                        color="#C0392B",
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Screens from phones or computers before sleep trick the brain into thinking it is still daytime.",
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
                                        "☕ Late Caffeine",
                                        weight=ft.FontWeight.BOLD,
                                        color="#C0392B",
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Consuming coffee or energy drinks after 2:00 P.M. blocks adenosine receptors that cause natural sleepiness.",
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
                                        "⏰ Irregular Schedules",
                                        weight=ft.FontWeight.BOLD,
                                        color="#C0392B",
                                        size=14,
                                    ),
                                    ft.Text(
                                        "Sleeping and waking up at very variable times generates 'social jet lag' and disorients hormone secretion.",
                                        size=12,
                                        color=TEXT_DARK,
                                    ),
                                ]
                            ),
                        ),
                    ),
                ],
                spacing=8,
                scroll=ft.ScrollMode.AUTO,
            ),
        )

    def _build_songs_tab(self) -> ft.Container:
        """Songs Tab: Consumes data from the API and maps it via a for loop."""
        songs_list_view = ft.ListView(expand=1, spacing=10, padding=10)
        
        # Fetch entities from the API
        songs = fetch_songs_from_api()

        if not songs:
            songs_list_view.controls.append(
                ft.Text("Could not load songs from API or list is empty.", color=TEXT_MUTED, size=13)
            )
        else:
            # Loop through entities as requested and populate UI via for loop
            for song in songs:
                card_item = ft.Card(
                    elevation=1,
                    bgcolor=CARD_BG,
                    content=ft.Container(
                        padding=12,
                        content=ft.Column(
                            controls=[
                                ft.Text(f"🎵 {song.title}", weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE, size=14),
                                ft.Text(f"Target Phase: {song.target_phase}", size=12, color=TEXT_DARK),
                                ft.Text(f"Frequency: {song.frequency} | Duration: {song.duration}", size=11, color=TEXT_MUTED),
                                ft.Text(song.description, size=11, color=TEXT_DARK),
                            ],
                            spacing=4,
                        ),
                    ),
                )
                songs_list_view.controls.append(card_item)

        return ft.Container(
            padding=10,
            content=ft.Column(
                controls=[
                    ft.Text(
                        "API Songs & Frequencies",
                        size=20,
                        weight=ft.FontWeight.BOLD,
                        color=PRIMARY_BLUE,
                    ),
                    ft.Text(
                        "Tracks fetched dynamically from production API:",
                        size=12,
                        color=TEXT_MUTED,
                    ),
                    ft.Container(height=5),
                    songs_list_view,
                ],
                expand=True,
            ),
        )

    def switch_tab(self, tab_index: int) -> None:
        """Internal function to switch views on navigation clicks."""
        if tab_index == 0:
            self.body_container.content = self._build_home_tab()
        elif tab_index == 1:
            self.body_container.content = self._build_simulator_tab()
        elif tab_index == 2:
            self.body_container.content = self._build_functions_tab()
        elif tab_index == 3:
            self.body_container.content = self._build_variables_tab()
        elif tab_index == 4:
            self.body_container.content = self._build_songs_tab()
        self.body_container.update()

    def create_nav_pill(self, text: str, icon, index: int) -> ft.Container:
        """Creates a custom pastel pill navigation button."""
        return ft.Container(
            content=ft.Row(
                [
                    ft.Icon(icon, size=14, color=PRIMARY_BLUE),
                    ft.Text(text, size=11, weight=ft.FontWeight.BOLD, color=PRIMARY_BLUE),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=2,
            ),
            padding=6,
            bgcolor=PASTEL_CREAM,
            border_radius=8,
            on_click=lambda e: self.switch_tab(index),
        )

    def build(self) -> ft.Column:
        """Assembles the custom navigation bar and main body container supporting Web and Desktop."""
        self.body_container.content = self._build_home_tab()

        # Navigation bar accommodating all sections cleanly for both web and desktop viewports
        nav_bar = ft.Row(
            controls=[
                self.create_nav_pill("Home", ft.Icons.HOME_ROUNDED, 0),
                self.create_nav_pill("Simulator", ft.Icons.ACCESS_TIME_ROUNDED, 1),
                self.create_nav_pill("Functions", ft.Icons.AUTO_AWESOME_ROUNDED, 2),
                self.create_nav_pill("Factors", ft.Icons.WARNING_AMBER_ROUNDED, 3),
                self.create_nav_pill("Songs", ft.Icons.MUSIC_NOTE_ROUNDED, 4),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )

        return ft.Column(
            controls=[nav_bar, ft.Divider(height=10, color="#CBD8E6"), self.body_container],
            expand=True,
        )

    def handle_slider_change(self, e: ft.ControlEvent) -> None:
        """Interactive event handler when the slider hour changes."""
        selected_hour = int(e.control.value)
        self.update_phase_display(selected_hour)

    def update_phase_display(self, hour: int) -> None:
        """Updates text contents using regular 12-hour format (A.M. / P.M.)."""
        current_phase: CircadianPhase = self.tracker.get_current_phase(hour)
        formatted_time = self.tracker.format_to_12h(hour)

        self.hour_display.value = f"Selected Time: {formatted_time}"
        self.phase_name_text.value = current_phase.name
        self.description_text.value = current_phase.description
        self.recommendation_text.value = current_phase.recommendation

        try:
            self.page.update()
        except Exception:
            pass