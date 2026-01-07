from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np

def draw_square(vertices, color):
    glColor3f(*color)
    glBegin(GL_QUADS)
    for v in vertices:
        glVertex2f(v[0], v[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # Define original vertices in Homogeneous Coordinates (x, y, 1)
    # Scaled down slightly to fit both on screen
    original_h = np.array([
        [-0.4, -0.4, 1],
        [ 0.4, -0.4, 1],
        [ 0.4,  0.4, 1],
        [-0.4,  0.4, 1]
    ])

    # 1. Draw Original Object (Red)
    draw_square(original_h, [1.0, 0.0, 0.0])

    # 2. Define Shear Matrix (shx = 1.0, shy = 0.0)
    shx, shy = 1.0, 0.0
    shear_matrix = np.array([
        [1,   shx, 0],
        [shy, 1,   0],
        [0,   0,   1]
    ])

    # 3. Apply Transformation: V_new = Matrix * V_old
    # We transpose the matrix or the vertices to align dimensions
    sheared_h = [np.dot(shear_matrix, v) for v in original_h]

    # 4. Draw Sheared Object (Blue)
    draw_square(sheared_h, [0.0, 0.0, 1.0])

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Shearing: Red (Original) vs Blue (Sheared)")
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-2, 2, -2, 2)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()