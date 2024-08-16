class Cell:
    def __init__(self, row, column, has_treasure=False, is_hole=False, reward_points=0):
        self.row = row
        self.column = column
        self.has_treasure = has_treasure
        self.is_hole = is_hole
        self.reward_points = reward_points
        self.visited = False
        self.isPlayer = False  # Atributo para saber si el jugador está en esta celda
        self.isMummy = False  # Atributo para saber si la momia está en esta celda

    def __str__(self):
        if self.isPlayer:
            return 'P'  # Prioridad a mostrar el jugador si está en la celda
        if self.isMummy:
            return 'M'  # Prioridad a mostrar la momia si está en la celda
        elif self.has_treasure:
            return 'T'
        elif self.is_hole:
            return 'O'
        elif self.reward_points > 0:
            return 'R'
        else:
            return ' '

    def visit(self):
        self.visited = True
        if self.reward_points > 0:
            reward = self.reward_points
            self.reward_points = 0  # La recompensa solo puede ser recolectada una vez
            return reward
        return 0

    def set_player(self, isplayerboolean):
        self.isPlayer = isplayerboolean  # Aquí se usa `self` para referirse al atributo de la clase
