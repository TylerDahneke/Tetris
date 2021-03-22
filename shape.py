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


# End Globas

def get_id():
    global CURR_ID
    ph = CURR_ID
    CURR_ID += 1
    return ph


def get_shape_corner(starting_pos, vari):
    vari_corner_list = TILE_PRESET[vari]
    x, y = starting_pos
    r_list = []
    for corner in vari_corner_list:
        shape_x, shape_y = x + ((corner % 2) * TILE_WIDTH), y + ((corner // 2) * TILE_HEIGHT)
        r_list.append([shape_x, shape_y])
    return r_list


class Shape:

    def __init__(self, owner_canvas=None, variance=None, pos=None):
        self.canvas = owner_canvas
        if variance is None:
            self.variance = random.choice(list(TILE_PRESET))
        else:
            self.variance = variance
        self.x, self.y = self.pos = pos
        self.canvas_shapes = self.create_shape()
        self.id = get_id()

    def __eq__(self, other):
        return self.id == other.id

    def create_shape(self):
        corner_preset = get_shape_corner(self.pos, self.variance)
        r_list = []
        for corner in corner_preset:
            x, y = corner
            new_shape = self.canvas.create_rectangle(x, y, x + TILE_WIDTH, y + TILE_HEIGHT,
                                                     fill=self.variance)
            r_list.append(new_shape)
        return r_list

    def move(self, all_shapes):
        if self.is_allowed(all_shapes):
            for shape in self.canvas_shapes:
                self.canvas.move(shape, 0, TILE_HEIGHT)
            self.x += 0
            self.y += TILE_HEIGHT
            return True
        return False

    def is_allowed(self, all_shapes):
        pred_loc = [self.x, self.y + TILE_HEIGHT]
        if not self.is_out_of_bounds(pred_loc) and not self.any_collide(pred_loc, all_shapes):
            return True
        return False

    def any_collide(self, pred_loc, all_shapes):
        self_shape_corners = get_shape_corner(pred_loc, self.variance)
        all_other_shape_corners = [o_s_c for o_s_c in all_shapes if self != o_s_c]
        for self_shape_corner in self_shape_corners:
            for other_shape in all_other_shape_corners:
                other_shape_corners = get_shape_corner(other_shape.pos, other_shape.variance)
                for other_shape_corner in other_shape_corners:
                    self_x, self_y = self_shape_corner
                    other_x, other_y = other_shape_corner
                    if (self_x < other_x + TILE_WIDTH and self_x + TILE_WIDTH > other_x and
                             self_y < other_y + TILE_HEIGHT and self_y + TILE_HEIGHT > other_y):
                        return True
        return False


    def is_out_of_bounds(self, pred_loc):
        global BOARDHEIGHT, BOARDWIDTH
        self_shape_corners = get_shape_corner(pred_loc, self.variance)
        for corner in self_shape_corners:
            x, y = corner

            print(y + TILE_HEIGHT)
            if x < 0 or x + TILE_WIDTH > BOARDWIDTH or y + TILE_HEIGHT > BOARDHEIGHT:
                return True
        return False





