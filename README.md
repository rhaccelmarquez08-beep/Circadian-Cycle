# Dulces Sueños - Rastreador de Ciclo Circadiano 🌙

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

```bash
.venv\Scripts\flet run -w src/circadian_tracker/main.py
```

### 💻 Modo Aplicación de Escritorio
Para ejecutar la aplicación como ventana nativa de escritorio:

```bash
.venv\Scripts\python.exe -m src.circadian_tracker.main
```

---

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Framework UI:** [Flet](https://flet.dev/) (Motor Flutter para Python)