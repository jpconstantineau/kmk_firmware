import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.matrix import DiodeOrientation


class KMKKeyboard(_KMKKeyboard):
    col_pins = (
        board.COL1,
        board.COL2,
        board.COL3,
        board.COL4,
        board.COL5,
        board.COL6,
        board.COL7,
        board.COL8,
        board.COL9,
        board.COL10,
        board.COL11,
        board.COL12,
        board.COL13,
        board.COL14,
        board.COL15,
        board.COL16,
        board.COL17,
    )
    row_pins = (
        board.ROW0,
        board.ROW1,
        board.ROW2,
        board.ROW3,
        board.ROW4,
        board.ROW5,
    )
    diode_orientation = DiodeOrientation.COL2ROW
    rgb_pixel_pin = board.NEOPIXEL
    rgb_num_pixels = 87
