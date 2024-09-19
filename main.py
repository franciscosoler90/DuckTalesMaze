import pygame
from gameMap import GameMap
from config import SIZE_CELL, MARGIN


def main():
    pygame.init()

    screen_width = 8 * SIZE_CELL + 2 * MARGIN
    screen_height = 8 * SIZE_CELL + 2 * MARGIN
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('DuckTales Maze')

    game_map = GameMap()

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
        game_map.draw_map(screen)
        pygame.display.flip()
        clock.tick(10)

        game_map.move_mummy()

        if game_map.check_lose():
            running = False
            show_message(screen, '¡You Lose!')

        if game_map.check_victory():
            running = False
            show_message(screen, '¡You Win!')

    pygame.quit()


def show_message(screen, title):
    font = pygame.font.SysFont(None, 74)
    text = font.render(title, True, (255, 255, 255))  # Texto en blanco
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)


if __name__ == "__main__":
    main()
