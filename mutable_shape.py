import random

# Globals

BOARDWIDTH = 200
BOARDHEIGHT = 600

TILE_WIDTH = BOARDWIDTH // 10
TILE_HEIGHT = TILE_WIDTH

TILE_PRESET = {'red': [0, 1, 2, 4], 'blue': [1, 2, 3, 4], 'green': [0, 1, 3, 5],
               'purple': [0, 2, 3, 5], 'yellow': [0, 2, 4, 6], 'salmon': [0, 1, 2, 3],
               'DarkOrange2': [0, 2, 3, 4]}

CURR_ID = 0


# End Globals


def get_relation_to(f_shape_node, s_shape_node):
    delta_x, delta_y = s_shape_node.x - f_shape_node.x, s_shape_node.y - f_shape_node.y
    if delta_x // TILE_WIDTH == 1 and delta_y == 0:
        return 'right'
    elif delta_x // TILE_WIDTH == -1 and delta_y == 0:
        return 'left'
    elif delta_y // TILE_HEIGHT == 1 and delta_x == 0:
        return 'down'
    elif delta_y // TILE_HEIGHT == -1 and delta_x == 0:
        return 'up'
    else:
        return False


def get_shape_corner(starting_pos, vari):
    vari_corner_list = TILE_PRESET[vari]
    x, y = starting_pos
    r_list = []
    for corner in vari_corner_list:
        shape_x, shape_y = x + ((corner % 2) * TILE_WIDTH), y + ((corner // 2) * TILE_HEIGHT)
        r_list.append([shape_x, shape_y])
    return r_list

def get_opposite_direction(inp):
    if inp is 'left':
        return 'right'
    elif inp is 'right':
        return 'left'
    elif inp is 'up':
        return 'down'
    elif inp is 'down':
        return 'up'

def create_circa(up=None, down=None, left=None, right=None):
    if up is not None:
        up = up
    if down is not None:
        down = down
    if left is not None:
        left = left
    if right is not None:
        right = right
    return {'up': up, 'down': down, 'left': left, 'right': right}


class shape_node:

    def __init__(self, canvas, canvas_shape, pos, circa=None):
        self.canvas = canvas
        self.canvas_shape = canvas_shape
        self.x, self.y = self.pos = pos
        if circa is None:
            self.circa = {'up': None, 'down': None, 'left': None, 'right': None}
        else:
            self.circa = circa

    def add_if_close(self, other_node):
        relation_str = get_relation_to(self, other_node)
        if relation_str:
            self.circa[relation_str] = other_node
            other_node[get_opposite_direction(relation_str)] = self


class shape:

    def __init__(self, canvas=None, pos=None, variance=None):
        self.canvas = canvas
        self.x, self.y = self.pos = pos
        if variance is None:
            variance = random.choice(list(TILE_PRESET))
        self.sentinel = self.create_sentinel_node(variance)

    def create_sentinel_node(self, variance):
        head_node = None
        node_list = []
        for index in TILE_PRESET[variance]:
            displacement_x, displacement_y = (index % 2) * TILE_WIDTH, (index // 2) * TILE_HEIGHT
            new_shape = self.canvas.create_rectangle(self.x + displacement_x, self.y + displacement_y,
                                                     self.x + displacement_x + TILE_WIDTH,
                                                     self.y + displacement_y + TILE_HEIGHT,
                                                     fill=variance)
            new_node = shape_node(self.canvas, new_shape, (self.x + displacement_x, self.y + displacement_y))
            if head_node is None:
                head_node = new_node
            else:
                head_node.add_if_close(new_node)
        return node

    def create_shape_node(self, shape_pos):
        x, y = shape_pos
        new_shape = self.canvas.create_rectangle(x, y, x + TILE_WIDTH, y + TILE_HEIGHT,
                                                 fill=)
