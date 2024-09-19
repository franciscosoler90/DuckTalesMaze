import pygame

from cell import Cell
import random

from config import SIZE_CELL, VISITED_COLOR, TREASURE_COLOR, MUMMY_COLOR, PLAYER_COLOR, MARGIN, \
    BACKGROUND_COLOR


class GameMap:
    def __init__(self):
        self.listCells = self.load_map()
        self.setup_map()

    @staticmethod
    def load_map():
        return [[Cell(row, col) for col in range(8)] for row in range(8)]

    def setup_map(self):
        def obtain_free_cells():
            array_cells = []
            for fila in range(len(self.listCells)):
                for col in range(len(self.listCells[fila])):
                    cell = self.listCells[fila][col]
                    if not cell.is_hole and not cell.has_treasure and cell.reward_points == 0:
                        array_cells.append((fila, col))
            return array_cells

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
            return None

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
                    color = PLAYER_COLOR
                    cell.visit()
                elif cell.isMummy:
                    color = MUMMY_COLOR
                elif cell.has_treasure:
                    color = TREASURE_COLOR
                elif cell.visited:
                    color = VISITED_COLOR
                elif cell.is_hole:
                    color = VISITED_COLOR
                else:
                    color = BACKGROUND_COLOR

                x = MARGIN + column * SIZE_CELL
                y = MARGIN + row * SIZE_CELL

                pygame.draw.rect(screen, color, pygame.Rect(x, y, SIZE_CELL, SIZE_CELL))
                pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, SIZE_CELL, SIZE_CELL), 3)

    def move(self, direction):
        cell = get_player_cell(self)
        row = cell.row
        column = cell.column

        if direction == 'UP':
            new_pos = (row - 1, column)
        elif direction == 'DOWN':
            new_pos = (row + 1, column)
        elif direction == 'LEFT':
            new_pos = (row, column - 1)
        elif direction == 'RIGHT':
            new_pos = (row, column + 1)
        else:
            return

        if 0 <= new_pos[0] < len(self.listCells) and 0 <= new_pos[1] < len(self.listCells):
            cell = self.listCells[new_pos[0]][new_pos[1]]
            if not cell.is_hole:
                cell = self.listCells[row][column]
                cell.isPlayer = False

                cell = self.listCells[new_pos[0]][new_pos[1]]
                cell.isPlayer = True

                return cell.visit()
        return 0

    def move_mummy(self):
        directions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        direction = random.choice(directions)

        cell = get_mummy_cell(self)
        row = cell.row
        column = cell.column

        if direction == 'UP':
            new_pos = (row - 1, column)
        elif direction == 'DOWN':
            new_pos = (row + 1, column)
        elif direction == 'LEFT':
            new_pos = (row, column - 1)
        elif direction == 'RIGHT':
            new_pos = (row, column + 1)
        else:
            return

        if 0 <= new_pos[0] < len(self.listCells) and 0 <= new_pos[1] < len(self.listCells):
            cell = self.listCells[new_pos[0]][new_pos[1]]
            if not cell.is_hole:
                cell = self.listCells[row][column]
                cell.isMummy = False

                cell = self.listCells[new_pos[0]][new_pos[1]]
                cell.isMummy = True

    def check_victory(self):
        cell = get_player_cell(self)
        cell2 = self.listCells[cell.row][cell.column]
        return cell2.has_treasure

    def check_lose(self):
        return get_player_cell(self) == get_mummy_cell(self)


def get_player_cell(self):
    for row in self.listCells:
        for cell in row:
            if cell.isPlayer:
                return cell
    return None


def get_mummy_cell(self):
    for row in self.listCells:
        for cell in row:
            if cell.isMummy:
                return cell
    return None
