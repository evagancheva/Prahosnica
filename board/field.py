import random

from constants import FIELD_COSTS, MIN_MONEY, MAX_MONEY, FLASH_CARD_MESSAGES, FLASH_CARD_COLORS, PURPLE


class Field:
    def __init__(self, field_type, image, arrow_image=None, arrow_direction=None):
        self.field_type = field_type
        self.image = image
        self.arrow_images = arrow_image or []
        self.arrow_directions = arrow_direction or []

    def apply_effect(self, player, renderer):

        if self.field_type in FIELD_COSTS:
            amount = FIELD_COSTS[self.field_type]
            player.spend_money(amount)
            loss_message = f"Player {player.id+1} buy a {self.field_type} for {amount}"
            renderer.show_flash_card("Purchase", loss_message, PURPLE)

        elif self.field_type in FLASH_CARD_COLORS:
            amount = random.randint(MIN_MONEY, MAX_MONEY)
            card_color = FLASH_CARD_COLORS[self.field_type]

            if self.field_type == "smiley":
                message = random.choice(FLASH_CARD_MESSAGES["smiley"])
                player.spend_money(amount)
                renderer.show_flash_card(self.field_type, f"{message} Lost {amount} coins!", card_color)

            elif self.field_type == "mad":
                message = random.choice(FLASH_CARD_MESSAGES["mad"])
                player.earn_money(amount)
                renderer.show_flash_card(self.field_type, f"{message} Gained {amount} coins!", card_color)

            elif self.field_type == "neutral":
                if random.choice([True, False]):
                    message = random.choice(FLASH_CARD_MESSAGES["smiley"])
                    player.spend_money(amount)
                    renderer.show_flash_card(self.field_type, f"{message}\nLost {amount} coins!", card_color)
                else:
                    message = random.choice(FLASH_CARD_MESSAGES["mad"])
                    player.earn_money(amount)
                    renderer.show_flash_card(self.field_type, f"{message}\nGained {amount} coins!", card_color)
