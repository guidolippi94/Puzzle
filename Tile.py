import pygame


class Map:
    size_x = 3  # -----
    size_y = 2  # |||||
    square_piece_size = 200
    tl_tl_tile = 100
    tile_pos = [[tl_tl_tile, tl_tl_tile],
                [tl_tl_tile + square_piece_size, tl_tl_tile],
                [tl_tl_tile + 2 * square_piece_size, tl_tl_tile],
                [tl_tl_tile, tl_tl_tile + square_piece_size],
                [tl_tl_tile + square_piece_size, tl_tl_tile + square_piece_size],
                [tl_tl_tile + 2 * square_piece_size, tl_tl_tile + square_piece_size],
                ]

    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y
        self.tiles1 = Tile(origin_x=self.tile_pos[5][0], origin_y=self.tile_pos[5][1], tile_number="1")
        self.tiles2 = Tile(origin_x=self.tile_pos[4][0], origin_y=self.tile_pos[4][1], tile_number="2")
        self.tiles3 = Tile(origin_x=self.tile_pos[3][0], origin_y=self.tile_pos[3][1], tile_number="3")
        self.tiles4 = Tile(origin_x=self.tile_pos[2][0], origin_y=self.tile_pos[2][1], tile_number="4")
        self.tiles5 = Tile(origin_x=self.tile_pos[1][0], origin_y=self.tile_pos[1][1], tile_number="5")
        self.tiles6 = Tile(origin_x=self.tile_pos[0][0], origin_y=self.tile_pos[0][1], tile_number="6")


class Tile:
    def __init__(self, origin_x, origin_y, tile_number):
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.is_occuped = False
        self.is_finished = False
        self.tile_name = tile_number

    def get_tile_origin_x(self):
        return self.origin_x

    def get_tile_origin_y(self):
        return self.origin_y

    def get_occupation(self):
        return self.is_occuped

    def get_finish(self):
        return self.is_finished

    def get_tile_name(self):
        return self.tile_name

    def set_occupation(self):
        self.is_occuped = True

    def set_finish(self):
        self.is_finished = True


