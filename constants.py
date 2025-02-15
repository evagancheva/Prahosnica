BOARD_WIDTH = 800
INFO_PANEL_WIDTH = 300
SCREEN_WIDTH = BOARD_WIDTH + INFO_PANEL_WIDTH
INFO_PANEL_X = SCREEN_WIDTH - INFO_PANEL_WIDTH
SCREEN_HEIGHT = 800
FLASH_CARD_WIDTH = 450
FLASH_CARD_HEIGHT = 300
GRID_WIDTH = 2

TILE_SIZE = 80
FONT_SIZE = 50
FONT_SIZE_FLASH_CARDS = 30
FPS = 60

PLAYER_RADIUS = TILE_SIZE // 4
ARROW_SCALE = TILE_SIZE // 3

BEIGE = (245, 245, 220)
DARK_GREY = (50, 50, 50)
WHITE = (255, 255, 255)
PURPLE = (128, 0, 128)
BLACK = (0, 0, 0)
HIGHLIGHT_COLOR = (0, 255, 255)
GREEN = (0, 100, 0)

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

# nqkuv obekt
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
FIELD_COSTS = {
    "bag": 30,
    "bracelet": 20,
    "perfume": 50,
    "jewellery": 80,
    "long-boot": 40
}
START_TILES = {
    (2, 2): (255, 0, 0),
    (2, 7): (255, 255, 0),
    (7, 7): (0, 0, 255),
    (7, 2): (0, 255, 0)

}
PLAYER_COLORS = list(START_TILES.values())
PLAYER_START_POSITIONS = list(START_TILES.keys())

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
DICE_SIZE = 80
DICE_X = INFO_PANEL_X + 110
DICE_Y = 150
MIN_MONEY = 20
MAX_MONEY = 80

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

FLASH_CARD_COLORS = {
    "smiley": (255, 150, 150),
    "neutral": (255, 225, 120),
    "mad": (150, 255, 150)
}
FLASH_CARD_MESSAGES = {
    "smiley": [
        "Oh yes! You bought too much ice cream! Delicious loss!",
        "You finally got rid of that useless money on a gadget!",
        "Oops! You forgot to take your change at the store! Well spent!",
        "You just HAD to order another round of pizza! Tasty investment!",
        "Made a ‘great’ investment in a fake cryptocurrency! Brilliant!",
        "Your bet didn’t go as planned… but who needs money anyway?",
        "You gave your cash to a street artist! What a kind soul!",
        "A random stranger scammed you! ",
        "Bought a golden spoon just because you could!",
        "Donated money to a ‘Make Sharks Fly’ foundation!",
        "Splurged on an ultra-expensive invisible hat. You look amazing!",
        "Paid a wizard to teach you magic… turns out it was just a guy in a robe.",
        "Upgraded to VIP parking in the middle of the desert!",
        "Bet everything on a snail race. Your snail stopped for a nap!",
        "Bought an NFT of a potato for a ridiculous price!",
        "Decided to buy air in a can... Premium edition!",
        "Invested in a time machine… that only goes forward one second!",
    ],
    "mad": [
        "Parking ticket! Ugh, but they refunded you by mistake!",
        "Lost your wallet… but some annoying person returned it with extra cash!",
        "You found some money on the street... What a disaster!",
        "You sold your old clothes for a fortune... Now you have to spend it!",
        "Your boss gave you a surprise bonus... What an inconvenience!",
        "Someone paid big money for your childhood drawing… Now what?",
        "Won a raffle! Great... Now you need to get rid of these coins!",
        "A stranger mistook you for a celebrity and gave you a tip… Nooo!",
        "Found a bag full of money! What are you supposed to do with it?",
        "Bank accidentally transferred money to your account... Annoying!",
        "A millionaire decided to give you an ‘inspiring’ cash reward!",
        "Your worst enemy just paid you to stay away from them!",
        "You inherited money from a long-lost relative… What a disaster!",
        "Your failed startup actually got investors… Now you have money!",
        "A genie granted you money instead of taking it away... Ugh!",
        "Someone tipped you for opening a door... Why!?",
        "Accidentally won a bet you were trying to lose...",
        "A company accidentally paid you for a job you never did!",
        "A vending machine glitched and gave you free cash! Noooo!"
    ]
}
