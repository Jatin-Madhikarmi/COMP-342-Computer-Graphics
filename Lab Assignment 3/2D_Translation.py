from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

def draw_square(r, g, b):
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(-0.2, -0.2)
    glVertex2f(0.2, -0.2)
    glVertex2f(0.2, 0.2)
    glVertex2f(-0.2, 0.2)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    # 1. DRAW INITIAL SQUARE (RED)
    draw_square(1.0, 0.0, 0.0)

    # 2. DEFINE HOMOGENEOUS TRANSLATION MATRIX
    # Factors: Move 0.5 right, 0.4 up
    tx, ty = 0.5, 0.4
    
    # OpenGL matrices are Column-Major
    # This represents the 2D Translation Algorithm in Homogeneous form
    translation_matrix = np.array([
        1, 0, 0, 0,  # Col 1
        0, 1, 0, 0,  # Col 2
        0, 0, 1, 0,  # Col 3
        tx, ty, 0, 1  # Col 4
    ], dtype=np.float32)

    glPushMatrix()
    # Manually multiply the current identity matrix by our translation matrix
    glMultMatrixf(translation_matrix) 
    
    # DRAW TRANSLATED SQUARE (BLUE)
    draw_square(0.0, 0.0, 1.0)
    glPopMatrix()

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) # White background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # glOrtho(left, right, bottom, top, near, far)
    # This replaces gluOrtho2D and is more reliable
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Manual Homogeneous Translation")
    init() # Initialize coordinates and background
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()