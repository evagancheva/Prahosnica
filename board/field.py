class Field:
    def __init__(self, field_type, image, arrow_image=None, arrow_direction=None):
        self.field_type = field_type
        self.image = image
        self.arrow_images = arrow_image or []
        self.arrow_directions = arrow_direction or []
