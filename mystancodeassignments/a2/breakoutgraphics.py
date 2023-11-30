"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
SWITCH = True


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=(window_width-ball_radius)/2, y=(window_height-ball_radius)/2)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)
        # Create Score board
        self.__a = 0
        self.score_label = GLabel("Score: " + str(self.__a), x=50, y=500)
        self.score_label.font = '-20'
        self.window.add(self.score_label)
        # Draw bricks
        current_y = brick_offset
        for i in range(5):
            # 以顏色為組別區分
            pass
            for j in range(2):
                # 2列
                current_x = 0
                if j == 0 and i == 0:
                    current_y = brick_offset
                else:
                    current_y += brick_height + brick_spacing
                for k in range(10):
                    # 以每行的個數
                    self.brick = GRect(brick_width, brick_height)
                    if i == 0:
                        self.brick.filled = True
                        self.brick.fill_color = "red"
                    elif i == 1:
                        self.brick.filled = True
                        self.brick.fill_color = "orange"
                    elif i == 2:
                        self.brick.filled = True
                        self.brick.fill_color = "yellow"
                    elif i == 3:
                        self.brick.filled = True
                        self.brick.fill_color = "green"
                    else:
                        self.brick.filled = True
                        self.brick.fill_color = "blue"
                    self.window.add(self.brick)
                    self.brick.x = current_x
                    self.brick.y = current_y
                    current_x += brick_width + brick_spacing

        # 遊戲重新
    def back_to_original(self):
        if self.ball.y + self.ball.height > self.window.height:
            self.ball.x = (self.window.width-BALL_RADIUS)/2  # 回到初始位置
            self.ball.y = (self.window.height-BALL_RADIUS)/2

    def paddle_move(self, mouse):
        if mouse.x - self.paddle.width / 2 >= 0 and mouse.x + self.paddle.width / 2 <= self.window.width:
            self.paddle.x = mouse.x - self.paddle.width / 2
        elif mouse.x - self.paddle.width / 2 < 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width / 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width

    def ball_move(self, mouse):
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def hit_the_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx *= -1
        if self.ball.y <= 0 or self.ball.y + self.ball.height >= self.window.height:
            self.__dy *= -1

    def collide(self):
        obj = self.window.get_object_at(self.ball.x, self.ball.y)
        obj1 = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y)
        obj2 = self.window.get_object_at(self.ball.x, self.ball.y + 2 * BALL_RADIUS)
        obj3 = self.window.get_object_at(self.ball.x + 2 * BALL_RADIUS, self.ball.y + 2 * BALL_RADIUS)

        # Check if the ball collides with the paddle
        if obj == self.paddle or obj1 == self.paddle or obj2 == self.paddle or obj3 == self.paddle:
            # 球碰到paddle，反彈
            self.__dy *= -1
        elif obj == self.score_label or obj1 == self.score_label or obj2 == self.score_label or obj3 == self.score_label:
            pass
        else:
            # Check if the ball collides with a brick
            if obj is not None and obj != self.paddle:
                # 球碰到brick，删除磚塊並反弹
                self.window.remove(obj)
                self.__a += 1
                self.window.remove(self.score_label)  # Remove old label
                self.score_label = GLabel("Score: " + str(self.__a), x=50, y=500)  # Create a new label
                self.score_label.font = '-20'
                self.window.add(self.score_label)
                self.__dy *= -1
            elif obj1 is not None and obj1 != self.paddle:
                self.window.remove(obj1)
                self.__a += 1
                self.window.remove(self.score_label)
                self.score_label = GLabel("Score: " + str(self.__a), x=50, y=500)
                self.score_label.font = '-20'
                self.window.add(self.score_label)
                self.__dy *= -1
            elif obj2 is not None and obj2 != self.paddle:
                self.window.remove(obj2)
                self.__a += 1
                self.window.remove(self.score_label)
                self.score_label = GLabel("Score: " + str(self.__a), x=50, y=500)
                self.score_label.font = '-20'
                self.window.add(self.score_label)
                self.__dy *= -1
            elif obj3 is not None and obj3 != self.paddle:
                self.window.remove(obj3)
                self.__a += 1
                self.window.remove(self.score_label)
                self.score_label = GLabel("Score: " + str(self.__a), x=50, y=500)
                self.score_label.font = '-20'
                self.window.add(self.score_label)
                self.__dy *= -1

    def get_a(self):
        return self.__a

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy


