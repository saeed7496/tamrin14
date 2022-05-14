
import arcade

class Dinasor(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.name='dina'
        self.scale=0.6
        self.textures==[arcade.load_texture('dino-walk-0.png',mirrored=True),
                              arcade.load_texture('dino-walk-1.png',mirrored=True)]


        self.stand_left_textures=[arcade.load_texture('dino-walk-0.png',mirrored=True),
                              arcade.load_texture('dino-walk-1.png',mirrored=True)]
        
        self.stand_right_textures=[arcade.load_texture('dino-walk-0.png',mirrored=True),
                               arcade.load_texture('dino-walk-1.png',mirrored=True)]

        self.walk_up_textures=[arcade.load_texture('dino-walk-0.png',mirrored=True),
                            arcade.load_texture('dino-walk-1.png',mirrored=True)]
        
        self.walk_down_textures=[arcade.load_texture('dino-down-0.png',mirrored=True),
                              arcade.load_texture('dino-down-1.png',mirrored=True)]
        self.center_x=650
        self.center_y=400