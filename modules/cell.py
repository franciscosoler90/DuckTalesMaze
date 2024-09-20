class Cell:
    def __init__(self, row, column, has_treasure=False, is_hole=False, reward_points=0):
        self.row = row
        self.column = column
        self.has_treasure = has_treasure
        self.is_hole = is_hole
        self.reward_points = reward_points
        self.visited = False
        self.isPlayer = False
        self.isMummy = False

    def __str__(self):
        if self.isPlayer:
            return 'P'
        if self.isMummy:
            return 'M'
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
            self.reward_points = 0
            return reward
        return 0

    def set_player(self, is_player_boolean):
        self.isPlayer = is_player_boolean
