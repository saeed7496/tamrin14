
import random
import time
import arcade
from dinasor import Dinasor
from gameover import GameOver
from ground import Ground
from kaktus import Kaktus
from kaktus import Bee
from scor import Score

width=800
height=370
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width,height,'chrom game')
        self.light_game=3
        self.t_light=time.time()
        
        self.t1=time.time()
        self.t3=3
        self.cactus_class=Kaktus()
        self.bird_class=Bee()
        self.kaktus=arcade.SpriteList()
        self.dina=Dinasor()
        self.ground=arcade.SpriteList()
        self.score=Score()
        self.gameover=GameOver()
        self._background_image=arcade.load_texture('sun.jpg')
        self._background_image2=arcade.load_texture('moon.jpg')
        for i in range(0,width,55):
            self.ground.append(Ground(i,0))
        self.physic_engein=arcade.PhysicsEnginePlatformer(self.dina,self.ground,0.4)
    def on_draw(self):
        arcade.start_render()
        if self.light_game%2==0:
            arcade.set_background_color(arcade.color.WHITE)
            arcade.draw_lrwh_rectangle_textured(180,280,80,80,self._background_image)
        elif self.light_game%2==1:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_lrwh_rectangle_textured(180,250,100,100,self._background_image2)
        self.ground.draw()
        self.dina.draw()
        self.score.draw(30,320,self.light_game)
        
        for cactus in self.kaktus:
            cactus.draw()

        if self.gameover.gameover_flag==1:
            self.gameover.draw(self.light_game)
            arcade.exit()
            
    def on_update(self, delta_time: float):
        
        self.physic_engein.update()
        self.dina.update_animation()
        self.t2=time.time()
        if self.t2 - self.t1>self.t3:
            self.kaktus.append(random.choice([Kaktus(),Bee()]))
            self.t1=time.time()
            self.score.number+=1
            self.t3-=0.1
            if len(self.kaktus)>4:
                self.kaktus.pop(0)
        for cactus in self.kaktus:
            cactus.update()
        
        for cactus in self.kaktus:
            if arcade.check_for_collision(self.dina,cactus):
                self.gameover.gameover_flag=1
                      
        if self.score.number>self.score.record:
            self.score.record=self.score.number
        
        
           
        if self.t2 - self.t_light > 30:
            self.light_game+=1
            self.t_light=time.time()
            
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.UP:
            if self.physic_engein.can_jump():
                self.dina.scale=0.6
                self.dina.change_y=13
        if symbol==arcade.key.DOWN:
            self.dina.scale=0.4
            self.dina.walk_down_textures=[arcade.load_texture('dino-down-0.png',mirrored=True),
                                        arcade.load_texture('dino-down-1.png',mirrored=True)]
    def on_key_release(self, symbol: int, modifiers: int):
        
        self.dina.walk_down_textures=[arcade.load_texture('dino-walk-0.png',mirrored=True),
                                        arcade.load_texture('dino-walk-1.png',mirrored=True)]
        self.dina.scale=0.6
game=Game()
arcade.run()




