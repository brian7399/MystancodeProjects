from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts
BALL_RADIUS = 10
SWITCH = True


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!

    while True:
        graphics.collide()
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        obj = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj1 = graphics.window.get_object_at(graphics.ball.x + 2*BALL_RADIUS, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + 2*BALL_RADIUS)
        obj3 = graphics.window.get_object_at(graphics.ball.x + 2*BALL_RADIUS, graphics.ball.y + 2*BALL_RADIUS)
        if obj == graphics.paddle or obj1 == graphics.paddle or obj2 == graphics.paddle or obj3 == graphics.paddle:
            # 球碰到paddle，反彈
            dy *= -1

        elif obj is not None or obj1 is not None or obj2 is not None or obj3 is not None:
            # 球碰到bricks，删除磚塊並反弹
            graphics.window.remove(obj)
            dy *= -1
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            dx *= -1
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            dy *= -1
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            global NUM_LIVES
            NUM_LIVES -= 1
            if NUM_LIVES == 0:
                return 0
        pause(FRAME_RATE)

# 撞到四邊牆壁可以反彈
# 撞到板子會談
# 可以消磚塊


if __name__ == '__main__':
    main()