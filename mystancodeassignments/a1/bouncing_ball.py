"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
SWITCH = True
window = GWindow(800, 500, title='bouncing_ball.py')
# global variable
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = "black"
window.add(ball, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    def start(e):
        global SWITCH
        a = 0
        if SWITCH:  # 只有當 SWITCH 為 True 時才執行以下程式
            SWITCH = False
            vy = 3
            while True:
                ball.move(VX, vy)
                if ball.y >= window.height:
                    vy *= -REDUCE
                if ball.x + ball.width > window.width:
                    ball.x = START_X
                    ball.y = START_Y
                    SWITCH = True
                    a += 1
                    break
                pause(DELAY)
                vy += GRAVITY
            if a == 3:
                SWITCH = False
                return 0

    onmouseclicked(start)


if __name__ == "__main__":
    main()
