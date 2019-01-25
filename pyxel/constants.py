import glfw

VERSION = "1.0.1"

GLFW_VERSION = "3.2.1"

DEFAULT_CAPTION = "Pyxel"
DEFAULT_SCALE = 0
DEFAULT_PALETTE = [
    0x000000,
    0x1D2B53,
    0x7E2553,
    0x008751,
    0xAB5236,
    0x5F574F,
    0xC2C3C7,
    0xFFF1E8,
    0xFF004D,
    0xFFA300,
    0xFFEC27,
    0x00E436,
    0x29ADFF,
    0x83769C,
    0xFF77A8,
    0xFFCCAA,
]
DEFAULT_FPS = 30
DEFAULT_BORDER_WIDTH = 0
DEFAULT_BORDER_COLOR = 0x101018

GIF_TRANSPARENCY_COLOR = (255, 0, 0)

ICON_DATA = [
    "0000000110000000",
    "0000011F71100000",
    "00011FF11FF11000",
    "011FF111111FF110",
    "1AE1111111111C71",
    "1E1EE111111CC1C1",
    "1E111EE11CC111C1",
    "1E11111E711111C1",
    "1E111111C11111C1",
    "1E111111C11111C1",
    "1E111111C11111C1",
    "1AE11111C1111C71",
    "011EE111C11CC110",
    "00011EE1CCC11000",
    "0000011E71100000",
    "0000000110000000",
]

MOUSE_CURSOR_IMAGE_X = 0
MOUSE_CURSOR_IMAGE_Y = 16
MOUSE_CURSOR_WIDTH = 8
MOUSE_CURSOR_HEIGHT = 8
MOUSE_CURSOR_DATA = [
    "00000011",
    "07776011",
    "07760111",
    "07676011",
    "06067601",
    "00106760",
    "11110601",
    "11111011",
]

APP_SCREEN_MAX_SIZE = 255
APP_SCREEN_SCALE_CUTDOWN = 2
APP_SCREEN_SCALE_MINIMUM = 2
APP_GIF_CAPTURE_COUNT = 900
APP_GIF_CAPTURE_SCALE = 2
APP_MEASURE_FRAME_COUNT = 10

RENDERER_IMAGE_COUNT = 4
RENDERER_IMAGE_WIDTH = 256
RENDERER_IMAGE_HEIGHT = 256
RENDERER_TILEMAP_COUNT = 8
RENDERER_TILEMAP_WIDTH = 256
RENDERER_TILEMAP_HEIGHT = 256
RENDERER_MIN_TEXTURE_SIZE = 256

DRAW_TYPE_PIX = 0
DRAW_TYPE_LINE = 1
DRAW_TYPE_RECT = 2
DRAW_TYPE_RECTB = 3
DRAW_TYPE_CIRC = 4
DRAW_TYPE_CIRCB = 5
DRAW_TYPE_BLT = 6
DRAW_TYPE_TEXT = 7
DRAW_MAX_COUNT = 10000

FONT_MIN_CODE = 32
FONT_MAX_CODE = 127
FONT_WIDTH = 4
FONT_HEIGHT = 6
FONT_ROW_COUNT = RENDERER_IMAGE_WIDTH // FONT_WIDTH
FONT_DATA = [
    0x000000,
    0x444040,
    0xAA0000,
    0xAEAEA0,
    0x6C6C40,
    0x824820,
    0x4A4AC0,
    0x440000,
    0x244420,
    0x844480,
    0xA4E4A0,
    0x04E400,
    0x000480,
    0x00E000,
    0x000040,
    0x224880,
    0x6AAAC0,
    0x4C4440,
    0xC248E0,
    0xC242C0,
    0xAAE220,
    0xE8C2C0,
    0x68EAE0,
    0xE24880,
    0xEAEAE0,
    0xEAE2C0,
    0x040400,
    0x040480,
    0x248420,
    0x0E0E00,
    0x842480,
    0xE24040,
    0x4AA860,
    0x4AEAA0,
    0xCACAC0,
    0x688860,
    0xCAAAC0,
    0xE8E8E0,
    0xE8E880,
    0x68EA60,
    0xAAEAA0,
    0xE444E0,
    0x222A40,
    0xAACAA0,
    0x8888E0,
    0xAEEAA0,
    0xCAAAA0,
    0x4AAA40,
    0xCAC880,
    0x4AAE60,
    0xCAECA0,
    0x6842C0,
    0xE44440,
    0xAAAA60,
    0xAAAA40,
    0xAAEEA0,
    0xAA4AA0,
    0xAA4440,
    0xE248E0,
    0x644460,
    0x884220,
    0xC444C0,
    0x4A0000,
    0x0000E0,
    0x840000,
    0x06AA60,
    0x8CAAC0,
    0x068860,
    0x26AA60,
    0x06AC60,
    0x24E440,
    0x06AE24,
    0x8CAAA0,
    0x404440,
    0x2022A4,
    0x8ACCA0,
    0xC444E0,
    0x0EEEA0,
    0x0CAAA0,
    0x04AA40,
    0x0CAAC8,
    0x06AA62,
    0x068880,
    0x06C6C0,
    0x4E4460,
    0x0AAA60,
    0x0AAA40,
    0x0AAEE0,
    0x0A44A0,
    0x0AA624,
    0x0E24E0,
    0x64C460,
    0x444440,
    0xC464C0,
    0x6C0000,
    0xEEEEE0,
]

AUDIO_SAMPLE_RATE = 22050
AUDIO_BLOCK_SIZE = 2205
AUDIO_CHANNEL_COUNT = 4
AUDIO_SOUND_COUNT = 65
AUDIO_MUSIC_COUNT = 8
AUDIO_ONE_SPEED = AUDIO_SAMPLE_RATE // 120
AUDIO_ONE_VOLUME = 0x7FFF // (AUDIO_CHANNEL_COUNT * 7)

SOUND_TONE_TRIANGLE = 0
SOUND_TONE_SQUARE = 1
SOUND_TONE_PULSE = 2
SOUND_TONE_NOISE = 3
SOUND_EFFECT_NONE = 0
SOUND_EFFECT_SLIDE = 1
SOUND_EFFECT_VIBRATO = 2
SOUND_EFFECT_FADEOUT = 3
SOUND_NOTE_TABLE = {"c": 0, "d": 2, "e": 4, "f": 5, "g": 7, "a": 9, "b": 11}
SOUND_TONE_TABLE = {
    "t": SOUND_TONE_TRIANGLE,
    "s": SOUND_TONE_SQUARE,
    "p": SOUND_TONE_PULSE,
    "n": SOUND_TONE_NOISE,
}
SOUND_EFFECT_TABLE = {
    "n": SOUND_EFFECT_NONE,
    "s": SOUND_EFFECT_SLIDE,
    "v": SOUND_EFFECT_VIBRATO,
    "f": SOUND_EFFECT_FADEOUT,
}

KEY_UNKNOWN = glfw.KEY_UNKNOWN
KEY_SPACE = glfw.KEY_SPACE
KEY_APOSTROPHE = glfw.KEY_APOSTROPHE
KEY_COMMA = glfw.KEY_COMMA
KEY_MINUS = glfw.KEY_MINUS
KEY_PERIOD = glfw.KEY_PERIOD
KEY_SLASH = glfw.KEY_SLASH
KEY_0 = glfw.KEY_0
KEY_1 = glfw.KEY_1
KEY_2 = glfw.KEY_2
KEY_3 = glfw.KEY_3
KEY_4 = glfw.KEY_4
KEY_5 = glfw.KEY_5
KEY_6 = glfw.KEY_6
KEY_7 = glfw.KEY_7
KEY_8 = glfw.KEY_8
KEY_9 = glfw.KEY_9
KEY_SEMICOLON = glfw.KEY_SEMICOLON
KEY_EQUAL = glfw.KEY_EQUAL
KEY_A = glfw.KEY_A
KEY_B = glfw.KEY_B
KEY_C = glfw.KEY_C
KEY_D = glfw.KEY_D
KEY_E = glfw.KEY_E
KEY_F = glfw.KEY_F
KEY_G = glfw.KEY_G
KEY_H = glfw.KEY_H
KEY_I = glfw.KEY_I
KEY_J = glfw.KEY_J
KEY_K = glfw.KEY_K
KEY_L = glfw.KEY_L
KEY_M = glfw.KEY_M
KEY_N = glfw.KEY_N
KEY_O = glfw.KEY_O
KEY_P = glfw.KEY_P
KEY_Q = glfw.KEY_Q
KEY_R = glfw.KEY_R
KEY_S = glfw.KEY_S
KEY_T = glfw.KEY_T
KEY_U = glfw.KEY_U
KEY_V = glfw.KEY_V
KEY_W = glfw.KEY_W
KEY_X = glfw.KEY_X
KEY_Y = glfw.KEY_Y
KEY_Z = glfw.KEY_Z
KEY_LEFT_BRACKET = glfw.KEY_LEFT_BRACKET
KEY_BACKSLASH = glfw.KEY_BACKSLASH
KEY_RIGHT_BRACKET = glfw.KEY_RIGHT_BRACKET
KEY_GRAVE_ACCENT = glfw.KEY_GRAVE_ACCENT
KEY_WORLD_1 = glfw.KEY_WORLD_1
KEY_WORLD_2 = glfw.KEY_WORLD_2
KEY_ESCAPE = glfw.KEY_ESCAPE
KEY_ENTER = glfw.KEY_ENTER
KEY_TAB = glfw.KEY_TAB
KEY_BACKSPACE = glfw.KEY_BACKSPACE
KEY_INSERT = glfw.KEY_INSERT
KEY_DELETE = glfw.KEY_DELETE
KEY_RIGHT = glfw.KEY_RIGHT
KEY_LEFT = glfw.KEY_LEFT
KEY_DOWN = glfw.KEY_DOWN
KEY_UP = glfw.KEY_UP
KEY_PAGE_UP = glfw.KEY_PAGE_UP
KEY_PAGE_DOWN = glfw.KEY_PAGE_DOWN
KEY_HOME = glfw.KEY_HOME
KEY_END = glfw.KEY_END
KEY_CAPS_LOCK = glfw.KEY_CAPS_LOCK
KEY_SCROLL_LOCK = glfw.KEY_SCROLL_LOCK
KEY_NUM_LOCK = glfw.KEY_NUM_LOCK
KEY_PRINT_SCREEN = glfw.KEY_PRINT_SCREEN
KEY_PAUSE = glfw.KEY_PAUSE
KEY_F1 = glfw.KEY_F1
KEY_F2 = glfw.KEY_F2
KEY_F3 = glfw.KEY_F3
KEY_F4 = glfw.KEY_F4
KEY_F5 = glfw.KEY_F5
KEY_F6 = glfw.KEY_F6
KEY_F7 = glfw.KEY_F7
KEY_F8 = glfw.KEY_F8
KEY_F9 = glfw.KEY_F9
KEY_F10 = glfw.KEY_F10
KEY_F11 = glfw.KEY_F11
KEY_F12 = glfw.KEY_F12
KEY_F13 = glfw.KEY_F13
KEY_F14 = glfw.KEY_F14
KEY_F15 = glfw.KEY_F15
KEY_F16 = glfw.KEY_F16
KEY_F17 = glfw.KEY_F17
KEY_F18 = glfw.KEY_F18
KEY_F19 = glfw.KEY_F19
KEY_F20 = glfw.KEY_F20
KEY_F21 = glfw.KEY_F21
KEY_F22 = glfw.KEY_F22
KEY_F23 = glfw.KEY_F23
KEY_F24 = glfw.KEY_F24
KEY_F25 = glfw.KEY_F25
KEY_KP_0 = glfw.KEY_KP_0
KEY_KP_1 = glfw.KEY_KP_1
KEY_KP_2 = glfw.KEY_KP_2
KEY_KP_3 = glfw.KEY_KP_3
KEY_KP_4 = glfw.KEY_KP_4
KEY_KP_5 = glfw.KEY_KP_5
KEY_KP_6 = glfw.KEY_KP_6
KEY_KP_7 = glfw.KEY_KP_7
KEY_KP_8 = glfw.KEY_KP_8
KEY_KP_9 = glfw.KEY_KP_9
KEY_KP_DECIMAL = glfw.KEY_KP_DECIMAL
KEY_KP_DIVIDE = glfw.KEY_KP_DIVIDE
KEY_KP_MULTIPLY = glfw.KEY_KP_MULTIPLY
KEY_KP_SUBTRACT = glfw.KEY_KP_SUBTRACT
KEY_KP_ADD = glfw.KEY_KP_ADD
KEY_KP_ENTER = glfw.KEY_KP_ENTER
KEY_KP_EQUAL = glfw.KEY_KP_EQUAL
KEY_LEFT_SHIFT = glfw.KEY_LEFT_SHIFT
KEY_LEFT_CONTROL = glfw.KEY_LEFT_CONTROL
KEY_LEFT_ALT = glfw.KEY_LEFT_ALT
KEY_LEFT_SUPER = glfw.KEY_LEFT_SUPER
KEY_RIGHT_SHIFT = glfw.KEY_RIGHT_SHIFT
KEY_RIGHT_CONTROL = glfw.KEY_RIGHT_CONTROL
KEY_RIGHT_ALT = glfw.KEY_RIGHT_ALT
KEY_RIGHT_SUPER = glfw.KEY_RIGHT_SUPER
KEY_MENU = glfw.KEY_MENU
KEY_SHIFT = 1000
KEY_CONTROL = 1001
KEY_ALT = 1002
KEY_SUPER = 1003

MOUSE_LEFT_BUTTON = 2000
MOUSE_MIDDLE_BUTTON = 2001
MOUSE_RIGHT_BUTTON = 2002

GAMEPAD_1_A = 3011
GAMEPAD_1_B = 3012
GAMEPAD_1_X = 3013
GAMEPAD_1_Y = 3014
GAMEPAD_1_LEFT_SHOULDER = 3008
GAMEPAD_1_RIGHT_SHOULDER = 3009
GAMEPAD_1_SELECT = 3005
GAMEPAD_1_START = 3004
GAMEPAD_1_UP = 3000
GAMEPAD_1_RIGHT = 3003
GAMEPAD_1_DOWN = 3001
GAMEPAD_1_LEFT = 3002

GAMEPAD_2_A = 4011
GAMEPAD_2_B = 4012
GAMEPAD_2_X = 4013
GAMEPAD_2_Y = 4014
GAMEPAD_2_LEFT_SHOULDER = 4008
GAMEPAD_2_RIGHT_SHOULDER = 4009
GAMEPAD_2_SELECT = 4005
GAMEPAD_2_START = 4004
GAMEPAD_2_UP = 4000
GAMEPAD_2_RIGHT = 4003
GAMEPAD_2_DOWN = 4001
GAMEPAD_2_LEFT = 4002

GAMEPAD_3_A = 5011
GAMEPAD_3_B = 5012
GAMEPAD_3_X = 5013
GAMEPAD_3_Y = 5014
GAMEPAD_3_LEFT_SHOULDER = 5008
GAMEPAD_3_RIGHT_SHOULDER = 5009
GAMEPAD_3_SELECT = 5005
GAMEPAD_3_START = 5004
GAMEPAD_3_UP = 5000
GAMEPAD_3_RIGHT = 5003
GAMEPAD_3_DOWN = 5001
GAMEPAD_3_LEFT = 5002

GAMEPAD_4_A = 6011
GAMEPAD_4_B = 6012
GAMEPAD_4_X = 6013
GAMEPAD_4_Y = 6014
GAMEPAD_4_LEFT_SHOULDER = 6008
GAMEPAD_4_RIGHT_SHOULDER = 6009
GAMEPAD_4_SELECT = 6005
GAMEPAD_4_START = 6004
GAMEPAD_4_UP = 6000
GAMEPAD_4_RIGHT = 6003
GAMEPAD_4_DOWN = 6001
GAMEPAD_4_LEFT = 6002



