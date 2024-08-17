import pygame
from gameMap import GameMap  # Asegúrate de que este sea el nombre correcto del archivo
from config import SIZE_CELL, MARGIN


def main():
    pygame.init()

    # Calcula el tamaño de la pantalla considerando la malla y el margen
    screen_width = 8 * SIZE_CELL + 2 * MARGIN
    screen_height = 8 * SIZE_CELL + 2 * MARGIN
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('DuckTales Maze')

    game_map = GameMap()  # Instancia de GameMap

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_map.move('UP')
                elif event.key == pygame.K_DOWN:
                    game_map.move('DOWN')
                elif event.key == pygame.K_LEFT:
                    game_map.move('LEFT')
                elif event.key == pygame.K_RIGHT:
                    game_map.move('RIGHT')

        screen.fill((0, 0, 0))
        game_map.draw_map(screen)  # Llama al método de instancia
        pygame.display.flip()
        clock.tick(10)

        # Movimiento independiente de la momia
        game_map.move_mummy()

        # Comprobar si la momia ha atrapado al jugador
        if game_map.check_lose():
            running = False
            show_message(screen, '¡Has perdido!')

        # Verificar si el jugador ha ganado
        if game_map.check_victory():
            running = False
            show_message(screen, '¡Has ganado!')

    pygame.quit()


def show_message(screen, title):
    font = pygame.font.SysFont(None, 74)
    text = font.render(title, True, (255, 255, 255))  # Texto en blanco
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Espera 3 segundos antes de salir


if __name__ == "__main__":
    main()
