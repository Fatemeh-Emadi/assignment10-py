
import arcade
import random
SPRITE_SCALING = 0.5
SPEED=2
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Snake Game"
class Snake(arcade.Sprite):
    def __init__(self, scale):
        super().__init__()
        self.color=arcade.color.BLUE
        self.width=20
        self.height=20
        self.speed=SPEED
        self.score=0
        self.center_x=SCREEN_WIDTH// 2
        self.center_y=SCREEN_HEIGHT// 2
        self.direction = "right"
    
    def on_draw(self):
        arcade.draw_rectangle_filled(self.center_x,self.center_y,self.width,self.height,self.color)

    def move(self):
        """ Move the player """
        if self.direction == "right":
            self.center_x += SPEED
        elif self.direction == "left":
            self.center_x -= SPEED
        elif self.direction == "up":
            self.center_y += SPEED
        elif self.direction == "down":
            self.center_y -= SPEED
    

        
class Apple(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = random.randint(10, 480)
        self.center_y = random.randint(10, 480)
        texture = arcade.load_texture("a.png")
        self.texture = texture
        self.scale = 0.014

    def on_draw(self):
        arcade.draw_texture_rectangle(self.center_x, self.center_y, 30, 30, self.texture)
      
class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=600, height=500, title="Snake Game 2022")
        self.background_color = arcade.color.LIGHT_PINK
        self.food=Apple()
        self.snake=Snake(SPRITE_SCALING)
             # Variables that will hold sprite lists
        self.player_list = None

        # Set up the player info
        self.player_sprite = None

       
    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Snake(SPRITE_SCALING) #############problem
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)
    def on_draw(self):
        arcade.start_render()
        self.snake.on_draw()
        self.food.on_draw()
    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the player
        self.player_list.update()
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.food):
            self.food.center_x = random.randint(10, 590)
            self.food.center_y = random.randint(10, 490)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        # If the player presses a key, update the speed
        if key == arcade.key.UP:
           self.player_sprite.change_y = SPEED
        elif key == arcade.key.DOWN:
             self.player_sprite.change_y = -SPEED
        elif key == arcade.key.LEFT:
             self.player_sprite.change_x = -SPEED
        elif key == arcade.key.RIGHT:
             self.player_sprite.change_x = SPEED

    def on_key_release(self, key: int, modifiers: int):
        """Called when the user releases a key. """
        if key == arcade.key.LEFT:
            if self.snake.direction != "right":
                self.snake.direction = "left"
        elif key == arcade.key.RIGHT:
            if self.snake.direction != "left":
                self.snake.direction = "right"
        elif key == arcade.key.UP:
            if self.snake.direction != "down":
                self.snake.direction = "up"
        elif key == arcade.key.DOWN:
            if self.snake.direction != "up":
                self.snake.direction = "down"

        

mygame=Game()
mygame.setup()
arcade.run()