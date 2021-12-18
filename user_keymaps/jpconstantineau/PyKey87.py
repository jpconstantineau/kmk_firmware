# PyKey87 designed by jpconstantineau
# https://github.com/jpconstantineau/PyKey60
# Requires CircuitPython 7.0.0 to support the RP2040 MCU

from kb import KMKKeyboard
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

rgb_ext = RGB(pixel_pin=keyboard.rgb_pixel_pin, num_pixels=keyboard.rgb_num_pixels, animation_mode=AnimationModes.STATIC)
keyboard.extensions.append(rgb_ext)

FN = KC.MO(1)
XXXXXXX = KC.TRNS

keyboard.keymap = [
    [
        KC.ESC,   KC.F1,   KC.F2,   KC.F3,   KC.F4,   KC.F5,  KC.F6,   KC.F7,   KC.F8,   XXXXXXX, KC.F9,   KC.F10,  KC.F11,  KC.F12,   KC.MUTE, KC.VOLD, KC.VOLU,
        KC.GRV,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,  KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS, KC.EQUAL, KC.BSPC, KC.INS,  KC.HOME, KC.PGUP,
        KC.TAB,   KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,   KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC,  KC.BSLASH, KC.DEL,  KC.END,  KC.PGDN,
        KC.CAPS,  KC.A,    KC.S,    KC.D,    KC.F,    KC.G,   KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT, XXXXXXX,  KC.ENTER, XXXXXXX,  XXXXXXX, XXXXXXX,
        KC.LSFT,  KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,   KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, XXXXXXX, XXXXXXX,  KC.RSFT,  XXXXXXX, KC.UP,  XXXXXXX,
        KC.LCTRL, KC.LGUI, KC.LALT, XXXXXXX, XXXXXXX, KC.SPC, XXXXXXX, XXXXXXX, XXXXXXX, KC.RALT, KC.RGUI, FN,      XXXXXXX,  KC.RCTRL, KC.LEFT, KC.DOWN,KC.RIGHT
    ],

    [
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, KC.RGB_TOG, KC.RGB_MODE_RAINBOW, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, KC.APP,  XXXXXXX,  XXXXXXX, XXXXXXX, XXXXXXX,  XXXXXXX, XXXXXXX,
    ],
]

if __name__ == '__main__':
    keyboard.go()
