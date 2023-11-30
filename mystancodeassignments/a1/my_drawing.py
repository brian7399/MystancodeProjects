"""
File: 
Name:
----------------------
TODO:
"""
"""
Title: 草帽海賊團旗
航海王一直是自己最喜歡的動漫之一，草帽海賊團為主角魯夫所成立的一個海賊團，[草帽]為紅髮傑克留給魯夫的物品，骷髏則是海賊團的象徵
one piece則是他們在尋找的大寶藏。
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GLabel
from campy.graphics.gwindow import GWindow
EYE = 50


def main():
    window = GWindow(width=800, height=700, title="Face")
    rect = GRect(width=window.width, height=window.height)
    rect.filled = True
    rect.fill_color = 'black'
    window.add(rect)

    label = GLabel("One Piece", x=50, y=330)
    label.font = '-40'
    label.color = "powderblue"
    window.add(label)

    boneline1 = GLine(220, 50, 720, 550)
    boneline1.color = "white"
    window.add(boneline1)
    boneline2 = GLine(180, 50, 680, 550)
    boneline2.color = "white"
    window.add(boneline2)
    boneline3 = GLine(200, 550, 700, 50)
    boneline3.color = "white"
    window.add(boneline3)
    boneline4 = GLine(160, 550, 660, 50)
    boneline4.color = "white"
    window.add(boneline4)

    bone1 = GArc(40, 40, 20, 250)
    bone1.filled = True
    bone1.fill_color = "white"
    window.add(bone1, x=160, y=10)
    bone2 = GArc(40, 40, 160, -250)
    bone2.filled = True
    bone2.fill_color = "white"
    window.add(bone2, x=200, y=10)
    bone3 = GArc(40, 40, 20, 250)
    bone3.filled = True
    bone3.fill_color = "white"
    window.add(bone3, x=640, y=10)
    bone4 = GArc(40, 40, 160, -250)
    bone4.filled = True
    bone4.fill_color = "white"
    window.add(bone4, x=680, y=10)

    bone5 = GArc(40, 40, 90, 250)
    bone5.filled = True
    bone5.fill_color = "white"
    window.add(bone5, x=140, y=550)
    bone6 = GArc(40, 40, 90, -250)
    bone6.filled = True
    bone6.fill_color = "white"
    window.add(bone6, x=180, y=550)
    bone7 = GArc(40, 40, 90, 250)
    bone7.filled = True
    bone7.fill_color = "white"
    window.add(bone7, x=660, y=550)
    bone8 = GArc(40, 40, 90, -250)
    bone8.filled = True
    bone8.fill_color = "white"
    window.add(bone8, x=700, y=550)

    hat = GArc(300, 250, 0, 180)
    hat.filled = True
    hat.fill_color = "yellow"
    window.add(hat, x=250, y=100)

    r = GRect(300, 50, x=250, y=155)
    r.filled = True
    r.fill_color = "red"
    window.add(r)

    horizontal = GRect(360, 20, x=220, y=190)
    horizontal.filled = True
    horizontal.fill_color = "yellow"
    window.add(horizontal)

    leftarc = GArc(30, 20, 90, 180)
    leftarc.filled = True
    leftarc.fill_color = "yellow"
    window.add(leftarc, x=215, y=190)

    rightarc = GArc(30, 20, 90, -180)
    rightarc.filled = True
    rightarc.fill_color = "yellow"
    window.add(rightarc, x=572, y=190)

    teeth = GRect(126, 85, x=325, y=315)
    teeth.filled = True
    teeth.fill_color = "white"
    window.add(teeth)

    face = GArc(250, 500, 180, 180)
    face.filled = True
    face.fill_color = "white"
    window.add(face, x=275, y=85)

    lefteye = GOval(EYE, EYE, x=300, y=230)
    lefteye.filled = True
    lefteye.fill_color = "black"
    window.add(lefteye)

    righteye = GOval(EYE, EYE, x=445, y=230)
    righteye.filled = True
    righteye.fill_color = "black"
    window.add(righteye)

    nose = GOval(20, 20, x=380, y=300)
    nose.filled = True
    nose.fill_color = "black"
    window.add(nose)

    teeth1 = GLine(325, 315, 325, 400)
    window.add(teeth1)
    teeth2 = GLine(356, 330, 356, 400)
    window.add(teeth2)
    teeth3 = GLine(388, 335, 388, 400)
    window.add(teeth3)
    teeth4 = GLine(420, 335, 420, 400)
    window.add(teeth4)
    teeth5 = GLine(451, 330, 451, 400)
    window.add(teeth5)
    teeth6 = GLine(325, 367, 451, 367)
    window.add(teeth6)
    teeth7 = GLine(325, 400, 451, 400)
    window.add(teeth7)

    jaw = GArc(126, 150, 180, 180)
    jaw.filled = True
    jaw.fill_color = "white"
    window.add(jaw, x=325, y=365)


if __name__ == '__main__':
    main()
