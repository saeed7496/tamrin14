
import arcade
class Kaktus(arcade.Sprite):
    def __init__(self):
        super().__init__(':resources:images/tiles/cactus.png')
        self.center_x=20
        self.center_y=67
        self.height=130
        self.width=85
        self.change_x=8
        self.speed=6

class Bee(arcade.Sprite):
    def __init__(self):
        super().__init__('bird-0.png')
        self.center_x=20
        self.center_y=120
        self.height=60
        self.width=60
        self.change_x=9
        self.speed=6
        