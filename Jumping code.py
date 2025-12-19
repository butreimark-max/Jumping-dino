import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 500
SCREEN_TITLE = ""
GRAVITY=0.6
JUMP=15
class Dino(arcade.Sprite):
    in_jump_momentum=False
    def movement(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.change_y-=GRAVITY
        #if self.top>SCREEN_HEIGHT:
          #  self.top = SCREEN_HEIGHT
        if self.bottom <SCREEN_HEIGHT/2.7 :
            self.bottom = SCREEN_HEIGHT/2.7
            self.in_jump_momentum=False

class Cactus(arcade.Sprite):
    point_counter=True
    def movement(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.change_x = -4
        if self.right <= 0:
            self.left = 1200
            self.point_counter=True
        if self.right <= window.dino_jumping.left and  self.point_counter:
            window.player_point += 1
            self.point_counter=False





class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        """player point"""
        self.player_point=0
        """ background """
        self.background_picture = arcade.load_texture("pixil-frame-0 (9).png")
        """ Dino """
        self.dino_jumping = Dino ("pixil-frame-0 (7).png",scale= 3)
        self.dino_jumping.center_x = SCREEN_WIDTH/2
        self.dino_jumping.center_y = SCREEN_HEIGHT/2
        """ Cactus """
        self.Spiky_Cactus = Cactus("pixil-frame-0 (8).png", scale=3)
        self.Spiky_Cactus.center_x = SCREEN_WIDTH / 1.1
        self.Spiky_Cactus.center_y = SCREEN_HEIGHT / 1.8
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.SPACE and not self.dino_jumping.in_jump_momentum:
            self.dino_jumping.change_y=JUMP
            self.dino_jumping.in_jump_momentum=True


    def on_key_release(self, symbol: int, modifiers: int):
        pass

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.background_picture)
        self.dino_jumping.draw()
        self.Spiky_Cactus.draw()
        arcade.draw_text(f"P{self.player_point}",200,420,arcade.color.ALABAMA_CRIMSON,50)

    def on_update(self, delta_time):
        self.dino_jumping.movement()
        self.Spiky_Cactus.movement()

window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()


"""

Сделать состояние игры (тру и фолс) (в деф ините)
ДОбавить коллизию в игре и при коллиизии отключать состояние
Дорисовать спрайты (по желанию), для анимации (бг и/или кактус + дино)
Гейм овер картинку найти или нарисовать


В апдейте запихнуть весь код внутрь этого состояния (если оно тру - все мувементы работают)
Сделать проверку на нажатие какой-то кнопки, что если была нажата (например, клавиша R), то снова включить состояние
игры на тру и заспавнить все объекты заново, где они были изначально

По желанию: узнать у чат гпт как загружать свои шрифты (это полезная инфа, пригодится не только для аркейда, а в другие разные программы)

"""