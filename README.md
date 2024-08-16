# DuckTales Maze

DuckTales Maze es un juego de laberinto en el que el jugador debe moverse por una cuadrícula, evitar obstáculos, recoger tesoros y obtener recompensas para ganar. Está basado en Python y utiliza la biblioteca Pygame para la interfaz gráfica.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

DuckTales Maze es un juego en el que el jugador explora un laberinto de 8x8 celdas. El objetivo es moverse por el laberinto, evitando agujeros y recolectando tesoros y recompensas. El juego finaliza cuando el jugador alcanza la celda con el tesoro.

## Características

- **Laberinto 8x8**: El juego se desarrolla en un tablero de 8x8 celdas.
- **Obstáculos y Tesoros**: Las celdas pueden contener tesoros, agujeros o recompensas.
- **Recompensas**: Algunas celdas contienen recompensas que el jugador puede recolectar.
- **Interfaz Gráfica**: La interfaz gráfica es proporcionada por la biblioteca Pygame.
- **Mensaje de Victoria**: Un mensaje aparece cuando el jugador alcanza el tesoro.

## Requisitos

- Python 3.x
- Pygame

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/duckTales-maze.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd duckTales-maze
    ```

3. Instala las dependencias:

    ```bash
    pip install pygame
    ```

## Uso

1. Ejecuta el juego:

    ```bash
    python main.py
    ```

2. Usa las teclas de dirección (`UP`, `DOWN`, `LEFT`, `RIGHT`) para mover al jugador a través del laberinto.

3. El objetivo es llegar a la celda con el tesoro para ganar la partida.

## Estructura del Proyecto

- `main.py`: Archivo principal que inicia el juego y maneja el bucle de eventos.
- `gameMap.py`: Define la clase `GameMap` que gestiona el laberinto y el movimiento del jugador.
- `cell.py`: Define la clase `Cell` que representa una celda del laberinto.
- `player.py`: Define la clase `Player` que maneja la puntuación y el movimiento del jugador.
- `config.py`: Archivo de configuración que contiene parámetros como el tamaño de las celdas y los colores.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un `issue` o envía un `pull request` si deseas mejorar el proyecto.

## Licencia

Este proyecto está licenciado bajo la [Licencia MIT](LICENSE).
