
import arcade
class Score(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.number=1
        self.record=1
    def draw(self,W,h,c):
        if c%2==0:
            arcade.draw_text('record: '+str(self.record),W,h,arcade.color.BLACK,10)
            arcade.draw_text('score: '+str(self.number),W+650,h,arcade.color.BLACK,10)
        elif c%2==1:
            arcade.draw_text('record: '+str(self.record),W,h,arcade.color.ROSE,10)
            arcade.draw_text('score: '+str(self.number),W+650,h,arcade.color.ROSE,10)