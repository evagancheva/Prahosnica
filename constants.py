BOARD_WIDTH = 800
INFO_PANEL_WIDTH = 300
SCREEN_WIDTH = BOARD_WIDTH + INFO_PANEL_WIDTH
SCREEN_HEIGHT = 800
TILE_SIZE = 80
FPS = 60
INFO_PANEL_X = SCREEN_WIDTH - INFO_PANEL_WIDTH
PLAYER_RADIUS = TILE_SIZE // 4
ARROW_SCALE = TILE_SIZE // 3
DICE_SIZE = 80

BEIGE = (245, 245, 220)
DARK_GREY = (50, 50, 50)
WHITE = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
GRID_WIDTH = 2

FIELD_IMAGES = {
    "bag": "images/tiles/bag.png",
    "jewellery": "images/tiles/jewellery.png",
    "perfume": "images/tiles/perfume.png",
    "smiley": "images/tiles/smiley.png",
    "mad": "images/tiles/mad.png",
    "neutral": "images/tiles/neutral.png",
    "bracelet": "images/tiles/bracelet.png",
    "long-boot": "images/tiles/long-boot.png",
}
ARROW_IMAGES = {
    "left": "images/tiles/left-arrow.png",
    "right": "images/tiles/right-arrow.png",
    "up": "images/tiles/up-arrow.png",
    "down": "images/tiles/down-arrow.png",
}
MIDDLE_IMAGE = "images/tiles/middle.png"

BOARD_LAYOUT = [
    ["bag", "bracelet", "perfume", "neutral", "mad", "jewellery", "perfume", "bag", "bracelet", "long-boot"],
    ["long-boot", "smiley", "perfume", "mad", "smiley", "mad", "bag", "smiley", "neutral", "jewellery"],
    ["perfume", "smiley", "", "", "", "", "", "", "smiley", "mad"],
    ["neutral", "bag", "", "", "", "", "", "", "bracelet", "perfume"],
    ["mad", "smiley", "", "", "", "", "", "", "bag", "bracelet"],
    ["jewellery", "bracelet", "", "", "", "", "", "", "bracelet", "bag"],
    ["perfume", "mad", "", "", "", "", "", "", "neutral", "jewellery"],
    ["bag", "smiley", "", "", "", "", "", "", "bag", "perfume"],
    ["bracelet", "mad", "neutral", "bracelet", "smiley", "neutral", "mad", "bag", "neutral", "long-boot"],
    ["long-boot", "perfume", "mad", "jewellery", "bag", "neutral", "bracelet", "perfume", "mad", "bag"]
]

ARROW_LAYOUT = [
    [["right"], ["right"], ["right", "down"], ["right"], ["right", "down"], ["right"], ["right"], ["right"], ["right"],
     ["down"]],
    [["up"], ["up"], ["right"], ["right", "up"], ["right"], ["right"], ["right", "up"], ["right"], ["down"], ["down"]],
    [["up", "right"], ["up"], ["up"], [], [], [], [], ["right"], ["down"], ["down"]],
    [["up"], ["up"], [], [], [], [], [], [], ["down"], ["left", "down"]],
    [["up"], ["up", "left"], [], [], [], [], [], [], ["down"], ["down"]],
    [["up"], ["up"], [], [], [], [], [], [], ["down", "right"], ["down"]],
    [["up", "right"], ["up"], [], [], [], [], [], [], ["down"], ["down"]],
    [["up"], ["up"], ["left"], [], [], [], [], ["down"], ["down"], ["down"]],
    [["up"], ["left"], ["left"], ["left", "down"], ["left"], ["left"], ["left", "down"], ["left"], ["left"], ["down"]],
    [["up"], ["up", "left"], ["left"], ["left"], ["up", "left"], ["left"], ["left"], ["left"], ["left"], ["left"]]
]

SPECIAL_TILES = {
    (2, 2): (255, 0, 0),
    (2, 7): (255, 255, 0),
    (7, 7): (0, 0, 255),
    (7, 2): (0, 255, 0)

}
PLAYER_COLORS = list(SPECIAL_TILES.values())

PLAYER_START_POSITIONS = list(SPECIAL_TILES.keys())

NO_GRID_TILES = {
    (3, 2), (2, 3), (6, 2), (2, 6), (3, 7), (7, 3), (6, 7), (7, 6)
}

ARROW_SIZE = TILE_SIZE // 3

ARROW_OFFSET = {
    "left": (-TILE_SIZE // 3, 0),
    "right": (TILE_SIZE // 3, 0),
    "up": (0, -TILE_SIZE // 3),
    "down": (0, TILE_SIZE // 3),
}
DICE_MIN = 1
DICE_MAX = 6

HIGHLIGHT_COLOR = (0, 255, 255)

TEXT_COLOR = (255, 255, 255)
FONT_SIZE = 36

DICE_IMAGES = {
    1: "images/dice/1.png",
    2: "images/dice/2.png",
    3: "images/dice/3.png",
    4: "images/dice/4.png",
    5: "images/dice/5.png",
    6: "images/dice/6.png",
}
DICE_ROLL_FRAMES = [
    "images/dice/roll1.png",
    "images/dice/roll2.png",
    "images/dice/roll3.png",
    "images/dice/roll4.png",
    "images/dice/roll5.png",
    "images/dice/roll6.png",
    "images/dice/roll7.png",
    "images/dice/roll8.png",
]

DICE_ROLL_SOUND = "images/dice/audio_roll_aud.mp3"
DICE_STOP_SOUND = "images/dice/roll_stop_aud.mp3"

DICE_X = INFO_PANEL_X + 110
DICE_Y = 150
