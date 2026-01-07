from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import math

def draw_polygon(vertices, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    for v in vertices:
        glVertex2f(v[0], v[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Original Square (Homogeneous: x, y, 1)
    original_v = np.array([
        [-0.3, -0.3, 1],
        [ 0.3, -0.3, 1],
        [ 0.3,  0.3, 1],
        [-0.3,  0.3, 1]
    ])

    # 1. Draw Original Object (Red)
    draw_polygon(original_v, [1.0, 0.0, 0.0])

    # Transformation Parameters
    tx, ty = 0.5, 0.5           # Translation
    angle = math.radians(45)    # Rotation (45 degrees)
    sx, sy = 1.2, 1.2           # Scaling
    shx, shy = 0.5, 0.0         # Shearing

    # Define Matrices
    T = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
    R = np.array([[math.cos(angle), -math.sin(angle), 0], 
                  [math.sin(angle),  math.cos(angle), 0], 
                  [0, 0, 1]])
    S = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
    Sh = np.array([[1, shx, 0], [shy, 1, 0], [0, 0, 1]])

    # Create Composite Matrix: M = T * R * S * Sh
    M = T @ R @ S @ Sh

    # Apply Transformation to each vertex
    transformed_v = [M @ v for v in original_v]

    # 2. Draw Transformed Object (Blue)
    draw_polygon(transformed_v, [0.0, 0.0, 1.0])

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutCreateWindow(b"Composite Transformation: Red=Orig, Blue=Final")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-2, 2, -2, 2)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()