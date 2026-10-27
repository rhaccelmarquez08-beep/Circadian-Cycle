# Dulces Sueños - Rastreador de Ciclo Circadiano 🌙

**Dulces Sueños** es una aplicación interactiva desarrollada en Python utilizando el framework **Flet**. Su interfaz presenta una estética suave con paleta de colores azul pastel, lavanda y elementos ilustrativos ("Dulces Sueños"). Modela el comportamiento biológico del ritmo circadiano humano, permitiendo explorar las fases del día, comprender las funciones orgánicas principales, analizar los factores que pueden desequilibrar este ciclo y disfrutar de una sección dinámica de canciones y frecuencias musicales consumidas desde una API remota.

El proyecto está diseñado para funcionar tanto como **aplicación web** como **aplicación de escritorio**, gestionando sus dependencias mediante **uv** y variables de entorno seguras con **python-dotenv**.

---

## Características principales

- **Simulador Interactivo de 24 Horas:** Permite arrastrar una barra deslizable (slider) configurada en formato de 12 horas (A.M. / P.M.) para explorar qué está sucediendo en el cuerpo en una hora específica. Se sincroniza automáticamente con la hora local o permite el ajuste manual.
- **Visualización de Fases Circadianas:** Muestra la fase activa (ej. *Sueño Profundo y Noche*), la descripción fisiológica correspondiente y recomendaciones prácticas de bienestar.
- **Consumo Dinámico de API (Canciones y Frecuencias):** Conexión en tiempo real con un endpoint remoto alojado en producción que provee catálogos de melodías y frecuencias relajantes, mapeadas automáticamente a entidades de Python mediante bucles de procesamiento.
- **Navegación por Pestañas:**
  - **Inicio:** Introducción general sobre qué es el reloj biológico y la importancia de mantenerlo sincronizado.
  - **Simulador:** Herramienta interactiva para simular el paso del tiempo y observar los cambios corporales.
  - **Funciones Principales:** Explicación detallada de los 3 pilares biológicos: *Captación de Luz Solar*, *Regulación Hormonal Dual (Cortisol/Melatonina)* y *Temperatura y Regeneración*.
  - **Factores de Desequilibrio:** Puntos de atención sobre factores perturbadores como *Luz Azul Nocturna*, *Cafeína Tardía* y *Horarios Irregulares*.
  - **Songs (Canciones):** Listado dinámico renderizado a partir de las respuestas JSON obtenidas de la API remota.
- **Diseño Multiplataforma:** Interfaz adaptada para ejecutarse en navegadores web o como aplicación de escritorio nativa.

---

## Tecnologías utilizadas

- **Python:** Lenguaje de programación principal.
- **Flet:** Framework basado en Flutter para la creación de la interfaz de usuario.
- **FastAPI / Requests:** Consumo de servicios web y estructuración de peticiones HTTP seguras mediante cabeceras de autorización (`X-API-Key`).
- **uv:** Gestor de paquetes y entorno de desarrollo de alto rendimiento.
- **python-dotenv:** Manejo seguro de variables de entorno (`.env`).

---

## Requisitos

- Python 3.8 o superior.
- Gestor de paquetes `uv`.
- Archivo `.env` configurado en la raíz con las credenciales de acceso a la API:
  ```env
  API_BASE_URL=[https://progra-2-krw5.onrender.com](https://progra-2-krw5.onrender.com)
  API_KEY=tu_clave_secreta_aqui

---


## Estructura del Proyecto

```
circadian_tracker/
├── assets/
│   └── descarga.jpg            # Recursos gráficos e imágenes ilustrativas
├── src/
│   └── circadian_tracker/
│       ├── __init__.py
│       ├── circadian_logic.py  # Lógica circadiana, modelos de entidades y cliente API
│       ├── ui_views.py         # Componentes visuales, pestañas y estilos pastel
│       └── main.py             # Punto de entrada principal de la aplicación Flet
├── .env                        # Variables de entorno privadas (no se sube a git)
├── .gitignore                  # Archivos ignorados por Git
├── pyproject.toml              # Configuración y dependencias gestionadas con uv
└── README.md                   # Documentación principal
```

---


## Descripción de los Archivos
- main.py: Contiene el punto de entrada principal y la inicialización de la interfaz en Flet.

- circadian_logic.py: Gestiona la lógica biológica del reloj circadiano, la clase SongEntity, la función fetch_songs_from_api() encargada de consumir y mapear los registros remotos mediante bucles, y la conversión a formato 12h.

- ui_views.py: Construye los componentes visuales, tarjetas informativas, la barra de navegación en píldoras y el listado dinámico de la sección de canciones.

- assets/: Contiene los recursos gráficos e imágenes utilizadas en la interfaz.

- pyproject.toml y uv.lock: Registran la configuración y librerías del entorno virtual optimizadas con uv.

- README.md: Contiene la documentación principal del proyecto.


---


## Instalación y Ejecución
- Asegúrese de tener configurado el archivo .env en la raíz del proyecto.

**Modo Aplicación de Escritorio**
- Para ejecutar la aplicación como ventana de escritorio independiente, ejecute en la terminal:
- uv run python src/circadian_tracker/main.py

**Modo Aplicación Web**
- Para lanzar la aplicación en el navegador web local mediante el servidor integrado de Flet, ejecute:
- uv run flet run src/circadian_tracker/main.py --web


---


## Funcionamiento General
- *Al iniciar Dulces Sueños, el usuario accede a la pestaña Inicio, donde se presenta la definición y relevancia del ritmo circadiano.*

- **A través de la barra de navegación superior, puede desplazarse a:**

- *Simulador:* Para ajustar libremente la hora del día y observar el estado fisiológico y recomendaciones personalizadas.

- *Funciones y Factores:* Para profundizar en los procesos del Núcleo Supraquiasmático (NSQ) y aprender a mitigar desequilibrios.

- *Songs:* Para consultar en tiempo real las pistas musicales y frecuencias óptimas obtenidas de forma dinámica desde el backend alojado en la nube.


---


## Estado del Proyecto
*Dulces Sueños es una aplicación completamente modular, multiplataforma y conectada a servicios web, que combina divulgación científica sobre la salud del sueño con consumo eficiente de APIs y buenas prácticas de desarrollo en Python.*