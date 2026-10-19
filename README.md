# Dulces Sueños - Rastreador de Ciclo Circadiano 🌙

**Dulces Sueños** es una aplicación interactiva desarrollada en Python utilizando el framework **Flet**. Su interfaz presenta una estética suave con paleta de colores azul pastel, lavanda y elementos ilustrativos ("Dulces Sueños"). Modela el comportamiento biológico del ritmo circadiano humano, permitiendo explorar las fases del día, comprender las funciones orgánicas principales y analizar los factores que pueden desequilibrar este ciclo.

El proyecto está diseñado para funcionar tanto como **aplicación web** como **aplicación de escritorio**.

---

## Características principales

- **Simulador Interactivo de 24 Horas:** Permite arrastrar una barra deslizable (slider) configurada en formato de 12 horas (A.M. / P.M.) para explorar qué está sucediendo en el cuerpo en una hora específica. Se sincroniza automáticamente con la zona horaria local o permite el ajuste manual.
- **Visualización de Fases Circadianas:** Muestra la fase activa (ej. *Sueño Profundo y Noche*), la descripción fisiológica correspondiente y recomendaciones prácticas de bienestar.
- **Navegación por Pestañas:**
  - **Inicio:** Introducción general sobre qué es el reloj biológico y la importancia de mantenerlo sincronizado.
  - **Simulador:** Herramienta interactiva para simular el paso del tiempo y observar los cambios corporales.
  - **Funciones Principales:** Explicación detallada de los 3 pilares biológicos: *Captación de Luz Solar*, *Regulación Hormonal Dual (Cortisol/Melatonina)* y *Temperatura y Regeneración*.
  - **Variables que lo desequilibran:** Puntos de atención sobre factores perturbadores como *Luz Azul Nocturna*, *Cafeína Tardía* y *Horarios Irregulares*.
- **Diseño Multiplataforma:** Interfaz adaptada para ejecutarse en navegadores web o como aplicación de escritorio nativa.

---

## Tecnologías utilizadas

- **Python:** Lenguaje de programación principal.
- **Flet:** Framework basado en Flutter para la creación de la interfaz de usuario.
- **Tecnologías Web / Desktop:** Entorno de ejecución nativo de Flet para renderizado web y de escritorio.

---

## Requisitos

- Python 3.8 o superior.
- Entorno virtual configurado (`.venv`).
- Dependencias del proyecto instaladas (`flet`).
- Archivos del proyecto y carpeta `assets/` en la raíz.

---

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

## Descripción de los Archivos

- **main.py:** Contiene el punto de entrada de la aplicación y la inicialización de la interfaz en Flet.
- **circadian_logic.py:** Define la lógica biológica del reloj circadiano, la asociación de fases según la hora y la conversión a formato 12h (A.M. / P.M.).
- **ui_views.py:** Construye los componentes visuales, las tarjetas informativas, la navegación por pestañas y los estilos pastel.
- **assets/:** Contiene los recursos gráficos e imágenes utilizadas en la aplicación.
- **pyproject.toml:** Registra la configuración y librerías necesarias para el proyecto.
- **README.md:** Contiene la documentación principal del proyecto.

---

## Instalación y Ejecución

Asegúrese de contar con un entorno virtual configurado y las dependencias instaladas antes de ejecutar los comandos.

### Modo Aplicación Web

Para lanzar la aplicación en el navegador web, ejecute en la terminal:

```bash
.venv\Scripts\flet run -w src/circadian_tracker/main.py
```

### Modo Aplicación de Escritorio

Para ejecutar la aplicación como ventana de escritorio independiente, ejecute:

```bash
.venv\Scripts\python.exe -m src.circadian_tracker.main
```

---

## Funcionamiento General

Al iniciar **Dulces Sueños**, el usuario aterriza en la pestaña **Inicio**, donde se presenta la definición y relevancia del ritmo circadiano.

A través de la barra superior, puede desplazarse a la sección **Simulador** para ajustar libremente el horario o consultar la hora actual de su zona horaria. La aplicación actualizará automáticamente el estado fisiológico (liberación de melatonina/cortisol, temperatura corporal, reparación celular) y sugerirá hábitos recomendados.

En las secciones **Funciones** y **Desequilibrios**, el usuario puede profundizar en el funcionamiento del Núcleo Supraquiasmático (NSQ) y aprender cómo mitigar el impacto de la luz azul de pantallas y el consumo de cafeína.

---

## Estado del Proyecto

**Dulces Sueños** es una aplicación completamente funcional que combina divulgación científica sobre la salud del sueño con una interfaz interactiva y amigable. Su arquitectura modular permite extender la lógica biológica o incorporar nuevos recordatorios y alarmas personalizadas en futuras versiones.