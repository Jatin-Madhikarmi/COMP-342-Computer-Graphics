import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import geometry

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Position camera
    gluLookAt(0, 2, 5, 0, 0, 0, 0, 1, 0)

    # --- 1. INITIAL TEAPOT (Scale = 1.0) ---
    glPushMatrix()
    glTranslatef(-1.5, 0, 0) # Move to the left side
    geometry.draw_teapot((0.7, 0.7, 0.7)) # Gray
    glPopMatrix()

    # --- 2. GENERAL SCALED TEAPOT (Uniform Scale) ---
    glPushMatrix()
    glTranslatef(1, 0, 0)  # Move to the right side
    
    # Apply scaling to all axes simultaneously
    # Syntax: glScalef(scale_x, scale_y, scale_z)
    glScalef(2.0, 2.0, 2.0) 
    
    geometry.draw_teapot((0.2, 0.6, 1.0)) # Blue
    glPopMatrix()

    glFlush()

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 800/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PyOpenGL General 3D Scaling")
    init()
    glutDisplayFunc(display)
    glutMainLoop()