
import arcade
class GameOver(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.gameover_flag=0
    def draw(self,c):
        if c%2==0:
            arcade.draw_text('GAME OVER',250,250,arcade.color.BLACK,40)
        elif c%2==1:
            arcade.draw_text('GAME OVER',250,250,arcade.color.ROSE,40)