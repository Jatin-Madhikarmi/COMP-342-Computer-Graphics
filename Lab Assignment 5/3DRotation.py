import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import geometry  # Import the geometry file

# Global rotation angle
angle = 0.0

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    # Set camera view
    gluLookAt(3, 3, 5,  # Camera position
              0, 0, 0,  # Look at point
              0, 1, 0)  # Up vector

    # --- 1. INITIAL TEAPOT (Static/Reference) ---
    glPushMatrix()
    glTranslatef(-2.0, 0, 0)
    geometry.draw_axes()
    geometry.draw_teapot((0.7, 0.7, 0.7)) # Light gray
    glPopMatrix()

    # --- 2. ROTATION ABOUT X-AXIS ---
    glPushMatrix()
    glTranslatef(1.0, 1.5, 0)
    glRotatef(angle, 1, 0, 0) 
    geometry.draw_axes()
    geometry.draw_teapot((1, 0.5, 0.5)) # Reddish
    glPopMatrix()

    # --- 3. ROTATION ABOUT Y-AXIS ---
    glPushMatrix()
    glTranslatef(1.0, 0, 0)
    glRotatef(angle, 0, 1, 0)
    geometry.draw_axes()
    geometry.draw_teapot((0.5, 1, 0.5)) # Greenish
    glPopMatrix()

    # --- 4. ROTATION ABOUT Z-AXIS ---
    glPushMatrix()
    glTranslatef(1.0, -1.5, 0)
    glRotatef(angle, 0, 0, 1)
    geometry.draw_axes()
    geometry.draw_teapot((0.5, 0.5, 1)) # Bluish
    glPopMatrix()

    glutSwapBuffers()

def idle():
    global angle
    angle += 0.5  # Controls rotation speed
    glutPostRedisplay()

def init():
    glClearColor(0.1, 0.1, 0.1, 1.0) # Dark background
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 800/600, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

if __name__ == "__main__":
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"PyOpenGL 3D Rotations - X, Y, and Z")
    
    init()
    glutDisplayFunc(display)
    glutIdleFunc(idle) # Keep the animation running
    glutMainLoop()