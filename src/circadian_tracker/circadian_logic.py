"""
Módulo: circadian_logic
Descripción: Contiene la lógica del negocio y modelo de datos para el ciclo circadiano.
"""


class CircadianPhase:
    """Representa los datos de una fase circadiana específica."""

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
        """Determina si una hora específica pertenece a esta fase."""
        if self.start_hour <= self.end_hour:
            return self.start_hour <= current_hour < self.end_hour
        else:
            return current_hour >= self.start_hour or current_hour < self.end_hour


class CircadianTracker:
    """Gestiona la lista de fases y los cálculos del ritmo circadiano."""

    def __init__(self):
        self.phases = [
            CircadianPhase(
                name="Despertar Mañanero",
                start_hour=6,
                end_hour=10,
                description="Respuesta de cortisol al despertar en aumento. La temperatura corporal sube de manera progresiva.",
                recommendation="Toma luz solar natural dentro de los primeros 30 minutos al despertar. Evita la cafeína de inmediato.",
            ),
            CircadianPhase(
                name="Pico de Alerta y Enfoque",
                start_hour=10,
                end_hour=14,
                description="Ventana de mayor estado de alerta y coordinación. Ideal para trabajo profundo y tareas complejas.",
                recommendation="Aborda tus tareas más exigentes ahora. Mantente bien hidratado.",
            ),
            CircadianPhase(
                name="Bajón de la Tarde",
                start_hour=14,
                end_hour=17,
                description="Descenso natural de energía posterior al almuerzo y pequeña caída en la temperatura corporal.",
                recommendation="Da una caminata corta, estírate o realiza tareas administrativas ligeras para mantener la activación.",
            ),
            CircadianPhase(
                name="Desconexión Nocturna",
                start_hour=17,
                end_hour=21,
                description="La producción de melatonina comienza a subir suavemente. Se alcanza el pico de presión arterial.",
                recommendation="Atenúa las luces interiores, reduce el tiempo frente a pantallas y prepárate para descansar.",
            ),
            CircadianPhase(
                name="Sueño Profundo y Noche",
                start_hour=21,
                end_hour=6,
                description="La melatonina inunda el sistema. Se realiza la reparación celular y consolidación de la memoria.",
                recommendation="Mantén la habitación oscura, fresca y silenciosa para una recuperación óptima.",
            ),
        ]

    def get_current_phase(self, current_hour: int) -> CircadianPhase:
        """Devuelve la fase activa para la hora dada."""
        for phase in self.phases:
            if phase.is_active(current_hour):
                return phase
        return self.phases[-1]

    @staticmethod
    def format_to_12h(hour: int) -> str:
        """Convierte una hora de formato 24h a formato de 12 horas con A.M. / P.M."""
        if hour == 0:
            return "12:00 A.M."
        elif hour < 12:
            return f"{hour:02d}:00 A.M."
        elif hour == 12:
            return "12:00 P.M."
        else:
            return f"{(hour - 12):02d}:00 P.M."