from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Data for pie chart
values = [40, 25, 20, 15]
colors = [
    (1.0, 0.0, 0.0),
    (0.0, 1.0, 0.0),
    (0.0, 0.0, 1.0),
    (1.0, 1.0, 0.0)
]

def draw_pie_chart():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    total = sum(values)
    start_angle = 0.0
    radius = 0.6

    for i in range(len(values)):
        angle = (values[i] / total) * 360.0
        glColor3f(*colors[i])

        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(0.0, 0.0)  # center of circle

        theta = start_angle
        while theta <= start_angle + angle:
            x = radius * math.cos(math.radians(theta))
            y = radius * math.sin(math.radians(theta))
            glVertex2f(x, y)
            theta += 1.0

        glEnd()
        start_angle += angle

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Pie Chart using PyOpenGL")
    init()
    glutDisplayFunc(draw_pie_chart)
    glutMainLoop()

main()