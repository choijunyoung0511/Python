# # import sys
# # args = sys.argv[1:]
# # for i in args:
# #     print(i)
#
# import sys
# args = sys.argv[1:]
# for i in args:
#     print(i.upper(), end=' ')

import turtle
import random

def screenLeftClick(x,y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
def screenRightClick(x, y) :
    turtle.penup()
    turtle.goto(x, y)

pSize, tSize = 10, 0
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)


turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)
turtle.done()