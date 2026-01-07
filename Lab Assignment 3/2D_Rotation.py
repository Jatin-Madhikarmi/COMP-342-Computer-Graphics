from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
import math

def draw_square(r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(-0.3, -0.3)
    glVertex2f(0.3, -0.3)
    glVertex2f(0.3, 0.3)
    glVertex2f(-0.3, 0.3)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # 1. Draw Original (Red)
    draw_square(1.0, 0.0, 0.0)

    # 2. Manual Rotation Matrix (45 degrees)
    angle = math.radians(45)
    c = math.cos(angle)
    s = math.sin(angle)

    # Column-major order
    rotation_matrix = np.array([
        c,  s,  0,  0,  # Column 1
       -s,  c,  0,  0,  # Column 2
        0,  0,  1,  0,  # Column 3
        0,  0,  0,  1   # Column 4
    ], dtype=np.float32)

    glPushMatrix()
    glMultMatrixf(rotation_matrix)
    draw_square(0.0, 0.0, 1.0) # Draw Rotated (Blue)
    glPopMatrix()

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Manual 2D Rotation Matrix")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()