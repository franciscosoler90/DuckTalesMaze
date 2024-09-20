import pygame
import random
from modules.cell import Cell
from modules.config import SIZE_CELL, COLOR_VISITED, COLOR_TREASURE, COLOR_MUMMY, COLOR_PLAYER, COLOR_BLACK, MARGIN


class GameMap:
    def __init__(self):
        self.listCells = self.load_map()
        self.player_pos = None
        self.mummy_pos = None
        self.treasure_pos = None
        self.setup_map()

    @staticmethod
    def load_map():
        return [[Cell(row, col) for col in range(8)] for row in range(8)]

    def setup_map(self):
        def obtain_free_cells():
            return [(fila, col) for fila in range(len(self.listCells)) for col in range(len(self.listCells[fila]))
                    if not (self.listCells[fila][col].is_hole or self.listCells[fila][col].has_treasure
                            or self.listCells[fila][col].reward_points != 0)]

        def put_element(tipo, valor=0):
            array_cells = obtain_free_cells()
            if array_cells:
                fila, col = random.choice(array_cells)
                cell = self.listCells[fila][col]
                if tipo == 'treasure':
                    cell.has_treasure = True
                    self.treasure_pos = (fila, col)
                elif tipo == 'hole':
                    cell.is_hole = True
                elif tipo == 'mummy':
                    cell.isMummy = True
                    self.mummy_pos = (fila, col)
                elif tipo == 'reward':
                    cell.reward_points = valor
                elif tipo == 'player':
                    self.player_pos = (fila, col)
                    cell.isPlayer = True

        put_element('treasure')
        put_element('mummy')
        for _ in range(5):
            put_element('reward', 50)
        put_element('player')

    def draw_map(self, screen):
        for row in range(len(self.listCells)):
            for column in range(len(self.listCells[row])):
                cell = self.listCells[row][column]
                if cell.isPlayer:
                    color = COLOR_PLAYER
                    cell.visit()
                elif cell.isMummy:
                    color = COLOR_MUMMY
                elif cell.has_treasure:
                    color = COLOR_TREASURE
                elif cell.visited:
                    color = COLOR_VISITED
                elif cell.is_hole:
                    color = COLOR_VISITED
                else:
                    color = COLOR_BLACK

                x = MARGIN + column * SIZE_CELL
                y = MARGIN + row * SIZE_CELL
                pygame.draw.rect(screen, color, pygame.Rect(x, y, SIZE_CELL, SIZE_CELL))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, SIZE_CELL, SIZE_CELL), 3)

    def move(self, direction):
        row, column = self.player_pos
        if direction == 'UP':
            new_pos = (row - 1, column)
        elif direction == 'DOWN':
            new_pos = (row + 1, column)
        elif direction == 'LEFT':
            new_pos = (row, column - 1)
        elif direction == 'RIGHT':
            new_pos = (row, column + 1)
        else:
            return 0

        if self.is_valid_move(new_pos):
            self.update_position(self.player_pos, new_pos, 'player')
            self.player_pos = new_pos
            return self.listCells[new_pos[0]][new_pos[1]].visit()
        return 0

    def move_mummy(self):
        row, column = self.mummy_pos
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        random.shuffle(directions)  # Randomize direction order
        for direction in directions:
            if direction == 'UP':
                new_pos = (row - 1, column)
            elif direction == 'DOWN':
                new_pos = (row + 1, column)
            elif direction == 'LEFT':
                new_pos = (row, column - 1)
            elif direction == 'RIGHT':
                new_pos = (row, column + 1)

            if self.is_valid_move(new_pos):
                self.update_position(self.mummy_pos, new_pos, 'mummy')
                self.mummy_pos = new_pos
                break

    def update_position(self, old_pos, new_pos, entity):
        old_cell = self.listCells[old_pos[0]][old_pos[1]]
        new_cell = self.listCells[new_pos[0]][new_pos[1]]
        if entity == 'player':
            old_cell.isPlayer = False
            new_cell.isPlayer = True
        elif entity == 'mummy':
            old_cell.isMummy = False
            new_cell.isMummy = True

    def is_valid_move(self, pos):
        row, col = pos
        if 0 <= row < len(self.listCells) and 0 <= col < len(self.listCells[0]):
            return not self.listCells[row][col].is_hole
        return False

    def check_victory(self):
        return self.player_pos == self.treasure_pos

    def check_lose(self):
        return self.player_pos == self.mummy_pos
