# Dulces Sueños - Rastreador de Ciclo Circadiano 🌙

<<<<<<< HEAD
=======

>>>>>>> e8911fb051bb11c6b1a16cff140ec06c43658bbf
**Dulces Sueños** es una aplicación interactiva multiplataforma (Web y Escritorio) desarrollada en **Python** utilizando **Flet**. Diseñada con una paleta estética de tonos azul pastel, lavanda y elementos conceptuales de descanso, la aplicación permite visualizar y entender cómo opera el ritmo circadiano en el cuerpo humano en tiempo real.

---

## 📋 Descripción del Proyecto

El proyecto ofrece una mirada detallada al comportamiento del "reloj biológico" de 24 horas. Permite sincronizar la visualización con la hora actual según la zona horaria del usuario o explorar manualmente distintas horas del día para conocer el estado fisiológico estimado y las mejores recomendaciones de bienestar para cada fase.

---

## ✨ Características Principales

- **Simulación Dinámica e Interactiva:** Sincronización automática con la hora real de la zona horaria y control manual mediante una barra deslizable de 24 horas.
- **Formato Horario 12 Horas:** Conversión y visualización amigable en formato **A.M. / P.M.**
- **Experiencia Multiplataforma:** Ejecución tanto en entorno **Web** como de **Escritorio**.
- **Interfaz "Dulces Sueños":** Diseño UI/UX enfocado en el confort visual, combinando colores suaves (azul pastel, lavanda) y tarjetas informativas ilustradas.
- **Secciones Educativas Integradas:**
  1. **Inicio:** Introducción al ciclo circadiano y su importancia para la salud general.
  2. **Simulador:** Estado de la fase activa, descripción fisiológica y recomendaciones prácticas según la hora seleccionada.
  3. **Funciones Principales:** Explicación de los tres pilares biológicos (Captación de luz solar, Regulación hormonal dual y Temperatura/Regeneración).
  4. **Variables de Desequilibrio:** Análisis sobre factores externos interruptores (Luz azul nocturna, cafeína tardía y horarios irregulares).

---

## 📂 Estructura del Proyecto

## Descripción del Proyecto

**Dulces Sueños** es una aplicación interactiva multiplataforma (web y de escritorio) desarrollada en Python utilizando el framework **Flet**. Su interfaz está diseñada con una estética suave de tonos azul pastel, lavanda e ilustraciones conceptuales de descanso ("Dulces Sueños"). 

El proyecto tiene como objetivo modelar y explicar el comportamiento del ritmo circadiano humano ("reloj biológico" de 24 horas) en relación con las funciones corporales, ofreciendo sugerencias prácticas, simulaciones en tiempo real y navegación interactiva por pestañas informativas.

## Características Principales

- **Simulador Interactivo del Ciclo:** Incluye una barra deslizable de 24 horas y tarjetas informativas que describen la fase activa según el tiempo seleccionado.
- **Sincronización por Zona Horaria:** El simulador se adapta automáticamente a la hora actual de la zona horaria del usuario, permitiendo también el ajuste manual para explorar cualquier hora del día.
- **Formato Horario de 12 Horas:** El slider y los indicadores muestran el tiempo en un formato amigable de **A.M. / P.M.**
- **Navegación por Pestañas:**
  - **Inicio:** Explicación general de qué es el ciclo circadiano y por qué es importante cuidarlo.
  - **Simulador:** Explora la hora exacta y muestra la descripción fisiológica y recomendaciones de bienestar.
  - **Funciones Principales:** Detalla los 3 pilares biológicos (Captación de luz solar, Regulación hormonal dual y Temperatura/Regeneración).
  - **Desequilibrios:** Muestra factores clave que alteran el ritmo (Luz azul nocturna, cafeína tardía y horarios irregulares).
- **Interfaz "Dulces Sueños":** Diseño UI con tarjetas ilustradas y paleta pastel pensada para el confort visual.

## Tecnologías Utilizadas

- **Python:** Lenguaje de programación principal.
- **Flet:** Framework utilizado para desarrollar la interfaz de usuario interactiva.
- **Entorno Virtual (.venv):** Para la gestión de dependencias y ejecución aislada del proyecto.

## Requisitos

- Python 3.x instalado.
- Entorno virtual con las dependencias del proyecto (incluyendo `flet`).
- Un navegador web actualizado (para la modalidad web) o entorno ejecutable de Python (para la modalidad de escritorio).
- Los archivos del proyecto, incluida la carpeta `assets/` con los recursos gráficos.

## Estructura del Proyecto


```text
circadian_tracker/
├── assets/
│   └── descarga.jpg          # Recursos gráficos e imágenes ilustrativas
├── src/
│   └── circadian_tracker/
│       ├── __init__.py
│       ├── circadian_logic.py # Lógica del ciclo, estados biológicos y conversor 12h
│       ├── ui_views.py        # Componentes de la interfaz, pestañas y estilos
│       └── main.py            # Punto de entrada de la aplicación en Flet
├── pyproject.toml             # Configuración y dependencias del proyecto
└── README.md                  # Documentación principal
```

---

## 🚀 Instrucciones de Ejecución

Asegúrate de contar con un entorno virtual configurado y las dependencias instaladas antes de ejecutar los comandos.

### 🌐 Modo Aplicación Web
Para lanzar la aplicación en el navegador web:

│   └── descarga.jpg          # Imagen ilustrativa (ovejita durmiendo en la luna)
├── src/
│   └── circadian_tracker/
│       ├── __init__.py
│       ├── circadian_logic.py # Lógica de negocio y conversor de formato a 12h
│       ├── ui_views.py        # Vistas de la UI con pestañas y estilos pastel
│       └── main.py            # Punto de entrada de la aplicación en Flet
├── pyproject.toml             # Configuración del proyecto y dependencias
└── README.md                  # Documentación principal del proyecto
```

## Descripción de los Archivos

- **main.py:** Contiene el punto de entrada de la aplicación y la inicialización de la interfaz en Flet.
- **circadian_logic.py:** Define la lógica biológica del reloj circadiano, la asociación de fases según la hora y la conversión del formato a 12 horas.
- **ui_views.py:** Construye los componentes visuales, las tarjetas, la navegación por pestañas y la paleta de colores.
- **assets/:** Contiene los recursos gráficos e imágenes utilizadas en la aplicación.
- **pyproject.toml:** Registra la configuración y librerías necesarias para el proyecto.
- **README.md:** Contiene la documentación del proyecto.

## Instalación y Ejecución

1. Clonar o descargar los archivos del proyecto en tu equipo.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Asegurarse de tener activo el entorno virtual (`.venv`).

Para ejecutar las distintas modalidades de la aplicación, utiliza los siguientes comandos en la terminal (cada uno por separado):

### Modo Aplicación Web

```bash
.venv\Scripts\flet run -w src/circadian_tracker/main.py
```

### 💻 Modo Aplicación de Escritorio
Para ejecutar la aplicación como ventana nativa de escritorio:

### Modo Aplicación de Escritorio

```bash
.venv\Scripts\python.exe -m src.circadian_tracker.main
```

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Framework UI:** [Flet](https://flet.dev/) (Motor Flutter para Python)

> **Nota:** La carpeta `assets/` debe conservar su ubicación en la raíz del proyecto para garantizar la correcta carga de las imágenes.

## Funcionamiento General

Al iniciar la aplicación, el usuario accede a la pestaña de **Inicio**, donde se le explica brevemente el concepto del ritmo circadiano. Al desplazarse a la pestaña **Simulador**, el sistema detecta la hora actual y muestra el estado fisiológico de su cuerpo. El usuario puede arrastrar libremente la barra de 24 horas para consultar qué debería estar ocurriendo en su organismo en un momento específico del día y recibir sugerencias para su bienestar.

En las pestañas **Funciones** y **Desequilibrios**, el usuario puede informarse más a fondo sobre la captación de luz, el comportamiento del cortisol y la melatonina, así como las variables externas (cafeína, pantallas) que desorganizan el ritmo biológico.

## Limitaciones Actuales

- Las recomendaciones y descripciones fisiológicas están predefinidas internamente dentro de módulos de código y no provienen de un servicio o base de datos externa.
- La simulación asume un cronotipo promedio (estándar) y no permite configurar cronotipos específicos (madrugador/trasnochador).

## Estado del Proyecto

**Dulces Sueños** es una aplicación funcional que integra simulación biológica, contenido informativo y navegación interactiva multiplataforma (web y escritorio).
Su estructura basada en módulos facilita la incorporación de nuevas funciones, como personalización de cronotipos o seguimiento diario, en futuras versiones.
Dulces Sueños es una aplicación funcional que integra simulación biológica, contenido informativo y navegación interactiva multiplataforma (web y escritorio).
Su estructura basada en módulos facilita la incorporación de nuevas funciones, como personalización de cronotipos o seguimiento diario, en futuras versiones.
