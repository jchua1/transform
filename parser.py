from display import *
from matrix import *
from draw import *
import time

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    c = f.read().splitlines()
    for i in range(0, len(c)):
        if c[i] == 'line':
            p = c[i+1].split(' ')
            p = map(int, p)
            add_edge(points, p[0], p[1], p[2], p[3], p[4], p[5])
        elif c[i] == 'ident':
            ident(transform)
        elif c[i] == 'scale':
            p = c[i+1].split(' ')
            p = map(int, p)
            t = make_scale(p[0], p[1], p[2])
            matrix_mult(t, transform)
        elif c[i] == 'move':
            p = c[i+1].split(' ')
            p = map(int, p)
            t = make_translate(p[0], p[1], p[2])
            matrix_mult(t, transform)
        elif c[i] == 'rotate':
            p = c[i+1].split(' ')
            p[1] = int(p[1])
            if p[0] == 'x':
                t = make_rotX(p[1])
            elif p[0] == 'y':
                t = make_rotY(p[1])
            elif p[0] == 'z':
                t = make_rotZ(p[1])
            matrix_mult(t, transform)
        elif c[i] == 'apply':
            matrix_mult(transform, points)
        elif c[i] == 'display':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            time.sleep(3)
        elif c[i] == 'save':
            clear_screen(screen)
            draw_lines(points, screen, color)
            n = c[i+1]
            save_extension(screen, n)
        elif c[i] == 'quit':
            break
    pass
