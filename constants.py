BOARD_WIDTH = 800
INFO_PANEL_WIDTH = 300
SCREEN_WIDTH = BOARD_WIDTH + INFO_PANEL_WIDTH
SCREEN_HEIGHT = 800
TILE_SIZE = 80
FPS = 60

BEIGE = (245, 245, 220)
DARK_GREY = (50, 50, 50)
WHITE = (255, 255, 255)
GRID_COLOR = (0, 0, 0)
GRID_WIDTH = 2

FIELD_IMAGES = {
    "bag": "images/bag.png",
    "jewellery": "images/jewellery.png",
    "perfume": "images/perfume.png",
    "smiley": "images/smiley.png",
    "mad": "images/mad.png",
    "neutral": "images/neutral.png",
    "bracelet": "images/bracelet.png",
    "long-boot": "images/long-boot.png",
}
ARROW_IMAGES = {
    "left": "images/left-arrow.png",
    "right": "images/right-arrow.png",
    "up": "images/up-arrow.png",
    "down": "images/down-arrow.png",
}
MIDDLE_IMAGE = "images/middle.png"

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
    (7, 2): (0, 255, 0),
    (7, 7): (0, 0, 255)
}

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