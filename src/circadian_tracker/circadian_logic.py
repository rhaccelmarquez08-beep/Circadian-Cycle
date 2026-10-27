"""
Module: circadian_logic
Description: Contains business logic, circadian data models, and API song integration.
"""

import os
from dotenv import load_dotenv
import requests

load_dotenv()

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")
API_KEY = os.getenv("API_KEY")


class SongEntity:
    """Represents a song entity retrieved from the API."""

    def __init__(
        self,
        song_id: int,
        title: str,
        description: str,
        text: str,
        duration: str,
        target_phase: str,
        frequency: str,
    ):
        self.song_id = song_id
        self.title = title
        self.description = description
        self.text = text
        self.duration = duration
        self.target_phase = target_phase
        self.frequency = frequency

    def __str__(self):
        return f"Song(id={self.song_id}, title='{self.title}', phase='{self.target_phase}', freq='{self.frequency}')"


def fetch_songs_from_api() -> list[SongEntity]:
    """
    Consumes the API endpoint, loops through the response items,
    maps them into SongEntity objects, prints them, and returns the list.
    """
    url = f"{BASE_URL}/api/v1/rhaccelmarquez/songs"
    headers = {
        "Accept": "application/json",
        "X-API-Key": API_KEY if API_KEY else ""
    }

    try:
        print(f"Connecting to API at: {url}")
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            items_json = data.get("items", [])
            
            song_entities = []

            # Loop to map JSON response into Python entities
            for item in items_json:
                entity = SongEntity(
                    song_id=item.get("id"),
                    title=item.get("title"),
                    description=item.get("description"),
                    text=item.get("text"),
                    duration=item.get("duration"),
                    target_phase=item.get("target_phase"),
                    frequency=item.get("frequency"),
                )
                song_entities.append(entity)

            print(f"Success! Retrieved and mapped {len(song_entities)} records.")
            
            for song in song_entities:
                print(song)

            return song_entities

        elif response.status_code == 401:
            print("Error 401: Missing or invalid X-API-Key header.")
        elif response.status_code == 403:
            print("Error 403: Invalid API Key for this namespace.")
        elif response.status_code == 404:
            print("Error 404: User namespace not found in the API.")
        else:
            print(f"Unexpected error ({response.status_code}): {response.text}")

        return []

    except requests.exceptions.RequestException as e:
        print(f"Network error trying to connect to the API: {e}")
        return []


class CircadianPhase:
    """Represents data for a specific circadian phase."""

    def __init__(
        self,
        name: str,
        start_hour: int,
        end_hour: int,
        description: str,
        recommendation: str,
    ):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.description = description
        self.recommendation = recommendation

    def is_active(self, current_hour: int) -> bool:
        """Determines if a specific hour belongs to this phase."""
        if self.start_hour <= self.end_hour:
            return self.start_hour <= current_hour < self.end_hour
        else:
            return current_hour >= self.start_hour or current_hour < self.end_hour


class CircadianTracker:
    """Manages phase lists and circadian rhythm calculations."""

    def __init__(self):
        self.phases = [
            CircadianPhase(
                name="Morning Awakening",
                start_hour=6,
                end_hour=10,
                description="Rising morning cortisol response. Core body temperature increases progressively.",
                recommendation="Get natural sunlight within the first 30 minutes of waking up. Avoid immediate caffeine.",
            ),
            CircadianPhase(
                name="Alertness & Focus Peak",
                start_hour=10,
                end_hour=14,
                description="Window of highest alertness and coordination. Ideal for deep work and complex tasks.",
                recommendation="Tackle your most demanding tasks now. Keep yourself well-hydrated.",
            ),
            CircadianPhase(
                name="Afternoon Dip",
                start_hour=14,
                end_hour=17,
                description="Natural post-lunch energy dip and minor drop in core body temperature.",
                recommendation="Take a short walk, stretch, or do light administrative tasks to maintain activation.",
            ),
            CircadianPhase(
                name="Evening Wind-Down",
                start_hour=17,
                end_hour=21,
                description="Melatonin production begins to rise softly. Blood pressure reaches its peak.",
                recommendation="Dim indoor lighting, reduce screen time, and prepare for rest.",
            ),
            CircadianPhase(
                name="Deep Sleep & Night",
                start_hour=21,
                end_hour=6,
                description="Melatonin floods the system. Cellular repair and memory consolidation take place.",
                recommendation="Keep your bedroom dark, cool, and quiet for optimal recovery.",
            ),
        ]

    def get_current_phase(self, current_hour: int) -> CircadianPhase:
        """Returns the active phase for a given hour."""
        for phase in self.phases:
            if phase.is_active(current_hour):
                return phase
        return self.phases[-1]

    @staticmethod
    def format_to_12h(hour: int) -> str:
        """Converts a 24h format hour to a 12h format string with A.M. / P.M."""
        if hour == 0:
            return "12:00 A.M."
        elif hour < 12:
            return f"{hour:02d}:00 A.M."
        elif hour == 12:
            return "12:00 P.M."
        else:
            return f"{(hour - 12):02d}:00 P.M."