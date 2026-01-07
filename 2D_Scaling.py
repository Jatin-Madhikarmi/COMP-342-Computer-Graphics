from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np

def draw_square(r, g, b):
    """Draws a simple 2D square (cube face)"""
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

    # 1. DRAW ORIGINAL (RED)
    # This remains at the original scale (0.4 units wide/tall)
    draw_square(1.0, 0.0, 0.0)

    # 2. DEFINE SCALING FACTORS
    sx, sy = 2.5, 1.8  # Make it 2.5x wider and 1.8x taller
    
    # OpenGL matrices are Column-Major
    # [ sx  0   0   0 ]
    # [ 0   sy  0   0 ]
    # [ 0   0   1   0 ]
    # [ 0   0   0   1 ]
    scaling_matrix = np.array([
        sx, 0,  0,  0,  # Column 1
        0,  sy, 0,  0,  # Column 2
        0,  0,  1,  0,  # Column 3
        0,  0,  0,  1   # Column 4
    ], dtype=np.float32)

    glPushMatrix()
    # Apply the manual homogeneous scaling matrix
    glMultMatrixf(scaling_matrix) 
    
    # DRAW SCALED (BLUE)
    # This will appear larger and behind/over the red one depending on order
    draw_square(0.0, 0.0, 1.0)
    glPopMatrix()

    glFlush()

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) # White background
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Set coordinate system from -1 to 1
    glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"2D Scaling: Red (Original) vs Blue (Scaled)")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()