import sys
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import geometry

factor = 0.0

def display():
    global factor
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(3, 3, 5, 0, 0, 0, 0, 1, 0)

    # Use a sine wave to oscillate the shearing effect
    s = math.sin(factor)

    # --- 1. ORIGINAL (No Shear) ---
    glPushMatrix()
    glTranslatef(-2.0, 0, 0)
    geometry.draw_teapot((0.7, 0.7, 0.7))
    glPopMatrix()

    # --- 2. SHEAR ALONG X (affected by Y) ---
    # Matrix: x' = x + sy, y' = y, z' = z
    shear_x = [1, 0, 0, 0,  
               s, 1, 0, 0,  
               0, 0, 1, 0,  
               0, 0, 0, 1]
    glPushMatrix()
    glTranslatef(1.0, 1.5, 0)
    glMultMatrixf(shear_x)
    geometry.draw_teapot((1, 0.5, 0.5))
    glPopMatrix()

    # --- 3. SHEAR ALONG Y (affected by X) ---
    # Matrix: x' = x, y' = y + sx, z' = z
    shear_y = [1, s, 0, 0,  
               0, 1, 0, 0,  
               0, 0, 1, 0,  
               0, 0, 0, 1]
    glPushMatrix()
    glTranslatef(1.0, 0, 0)
    glMultMatrixf(shear_y)
    geometry.draw_teapot((0.5, 1, 0.5))
    glPopMatrix()

    # --- 4. SHEAR ALONG Z (affected by Y) ---
    # Matrix: x' = x, y' = y, z' = z + sy
    shear_z = [1, 0, 0, 0,  
               0, 1, s, 0,  
               0, 0, 1, 0,  
               0, 0, 0, 1]
    glPushMatrix()
    glTranslatef(1.0, -1.5, 0)
    glMultMatrixf(shear_z)
    geometry.draw_teapot((0.5, 0.5, 1))
    glPopMatrix()

    glutSwapBuffers()

def idle():
    global factor
    factor += 0.01
    glutPostRedisplay()

def init():
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 800/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PyOpenGL 3D Shearing")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(idle)
    glutMainLoop()