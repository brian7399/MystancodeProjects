"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

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
        a = graphics.get_a()
        graphics.ball.move(dx, dy)
        graphics.hit_the_wall()
        if graphics.ball.y + graphics.ball.height > graphics.window.height:
            graphics.back_to_original()
            global NUM_LIVES
            NUM_LIVES -= 1
            if NUM_LIVES == 0:
                graphics.window.remove(graphics.score_label)
                graphics.score_label.text = ("Final Score: " + str(a))
                graphics.score_label.font = '-40'
                graphics.score_label.color = "red"
                graphics.window.add(graphics.score_label)
                return
        pause(FRAME_RATE)

# 撞到四邊牆壁可以反彈
# 撞到板子會談
# 可以消磚塊


if __name__ == '__main__':
    main()
