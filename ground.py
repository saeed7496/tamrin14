
import arcade
class Ground(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(':resources:images/tiles/sandHalf_left.png')
        self.center_x=w
        self.center_y=h
        self.height=60
        self.width=60
        #self.scale=0.5
        