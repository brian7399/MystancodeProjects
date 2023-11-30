"""
File: 
Name:
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
circle = None
window = GWindow()


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point)


def point(mouse):
    global circle

    if circle is None:
        # circle為空，為第一次點擊
        circle = GOval(SIZE, SIZE)
        circle.x = mouse.x-SIZE/2
        circle.y = mouse.y-SIZE/2
        window.add(circle)
    else:
        # 第二次點擊
        line = GLine(circle.x, circle.y, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
        circle = None  # 重製為空


if __name__ == "__main__":
    main()
