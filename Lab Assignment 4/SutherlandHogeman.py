from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Clipping window boundaries
x_min, y_min = -0.4, -0.4
x_max, y_max = 0.4, 0.4

def get_intersection(p1, p2, edge_type):
    x1, y1 = p1
    x2, y2 = p2
    
    if edge_type == "LEFT":
        x = x_min
        y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
    elif edge_type == "RIGHT":
        x = x_max
        y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
    elif edge_type == "BOTTOM":
        y = y_min
        x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
    elif edge_type == "TOP":
        y = y_max
        x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
    return (x, y)

def is_inside(p, edge_type):
    if edge_type == "LEFT": return p[0] >= x_min
    if edge_type == "RIGHT": return p[0] <= x_max
    if edge_type == "BOTTOM": return p[1] >= y_min
    if edge_type == "TOP": return p[1] <= y_max
    return False

def clip(polygon, edge_type):
    new_polygon = []
    for i in range(len(polygon)):
        p1 = polygon[i]
        p2 = polygon[(i + 1) % len(polygon)]
        
        in1 = is_inside(p1, edge_type)
        in2 = is_inside(p2, edge_type)
        
        if in1 and in2:
            new_polygon.append(p2)
        elif in1 and not in2:
            new_polygon.append(get_intersection(p1, p2, edge_type))
        elif not in1 and in2:
            new_polygon.append(get_intersection(p1, p2, edge_type))
            new_polygon.append(p2)
            
    return new_polygon

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw Clipping Window (White)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min, y_min); glVertex2f(x_max, y_min)
    glVertex2f(x_max, y_max); glVertex2f(x_min, y_max)
    glEnd()
    # Original Polygon (Red Outline)
    poly = [(-0.6, -0.2), (0.0, 0.7), (0.5, -0.3)]
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)
    for v in poly: glVertex2f(*v)
    glEnd()

    # Apply Clipping for all 4 edges
    clipped_poly = poly
    for edge in ["LEFT", "RIGHT", "BOTTOM", "TOP"]:
        clipped_poly = clip(clipped_poly, edge)

    # Draw Clipped Polygon (Yellow Solid)
    if clipped_poly:
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_POLYGON)
        for v in clipped_poly: glVertex2f(*v)
        glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutCreateWindow(b"Sutherland-Hodgeman Polygon Clipping")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()