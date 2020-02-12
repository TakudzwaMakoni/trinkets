# framex (c) By Takudzwa 2019
import numpy as np
import matplotlib.pyplot as p
from matplotlib.animation import FuncAnimation
# from IPython.display import clear_output

'''constants and trig functions'''

pi = np.pi
sin = np.sin
cos = np.cos
tan = np.tan

'''Below are the default basis vectors in ket (column) form
    and their bra (row) equivalent, obtained by applying the hermitian operator'''
ket_i = np.array([[1],[0],[0]])
ket_j = np.array([[0],[1],[0]])
ket_k = np.array([[0],[0],[1]])

'''we apply the hermitian to these to get the bra vectors'''
bra_i = np.conjugate( np.transpose(ket_i) )
bra_j = np.conjugate( np.transpose(ket_j) )
bra_k = np.conjugate( np.transpose(ket_k) )

'''Below are the projection matrices in our default basis.'''
PROJI = (ket_i @ bra_i) / (bra_i @ ket_i)[0][0] # projection in i
PROJJ = (ket_j @ bra_j) / (bra_j @ ket_j)[0][0] # projection in j
PROJK = (ket_k @ bra_k) / (bra_k @ ket_k)[0][0] # projection in k


''' Input:  some ket vector, and the output projection matrices.
    Output: a new ket vector in the basis described by the input projection matrices'''
def newV(ket,ProjectionMatrices=(PROJI,PROJJ,PROJK)):
    PI, PJ, PK = ProjectionMatrices
    p, q, r  = PI @ ket, PJ @ ket, PK @ ket
    return p + q + r


''' Input:  x, y, and z data points of a function, and set of basis vectors.
    Output: set of vectors describing the function in the given basis
    using newV function.'''
def newB(x,y,z,point_density,B=(ket_i,ket_j,ket_k)):

    k_i, k_j, k_k = B

    b_i = np.conjugate( np.transpose(k_i) )
    b_j = np.conjugate( np.transpose(k_j) )
    b_k = np.conjugate( np.transpose(k_k) )

    PI = (k_i @ b_i) / (b_i @ k_i)[0][0]
    PJ = (k_j @ b_j) / (b_j @ k_j)[0][0]
    PK = (k_k @ b_k) / (b_k @ k_k)[0][0]

    return np.array([newV(np.array([[x[i]],[y[i]],[z[i]]]), (PI,PJ,PK)) for i in range(point_density) ])


def ROTI(A): return np.array([[1,0,0],[0,cos(A),-sin(A)],[0,sin(A),cos(A)]]) # rotation about I
def ROTJ(A): return np.array([[cos(A),0,sin(A)],[0,1,0],[-sin(A),0,cos(A)]]) # rotation about J
def ROTK(A): return np.array([[cos(A),-sin(A),0],[sin(A),cos(A),0],[0,0,1]]) # rotation about K

'''we can compound all three rotation matrices through Matrix Multiplication.'''
def ROT(ket,A=0,B=0,C=0): return ROTI(A) @ ROTJ(B) @ ROTK(C) @ ket

''' we can still plot our data points by stacking all the vectors in our produced set.
    This is done using numpy.hstack.'''


'''It is more convenient for later on if we
    just make a function that stacks a vector set this way.'''

def set_stack(vector_set): return np.transpose(np.hstack(vector_set)) # input will be output of newB.

'''now if we rotate the plane about x, y, or z, we should see some changes.
    below i defined the function updateframe which i will use to rotate the plane of the graph about any of the axes.'''

def updateframe(stack,Alpha,Beta,Gamma,point_density):
    newstack = np.zeros((point_density,3))
    for i in range(point_density): newstack[i,:] = np.transpose( ROT( np.transpose( stack[i,:] ), Alpha, Beta, Gamma) )
    return newstack[:,0], newstack[:,1], newstack[:,2]

def updateframex(stack,Alpha,Beta,Gamma,point_density):
    newstack = np.zeros((point_density**2,3))
    for i in range(point_density**2): newstack[i,:] = np.transpose( ROT( np.transpose( stack[i,:] ), Alpha, Beta, Gamma) )
    return newstack[:,0], newstack[:,1], newstack[:,2]

def newBx(x,y,z,point_density,B=(ket_i,ket_j,ket_k)):

    k_i, k_j, k_k = B

    b_i = np.conjugate( np.transpose(k_i) )
    b_j = np.conjugate( np.transpose(k_j) )
    b_k = np.conjugate( np.transpose(k_k) )

    PI = (k_i @ b_i) / (b_i @ k_i)[0][0]
    PJ = (k_j @ b_j) / (b_j @ k_j)[0][0]
    PK = (k_k @ b_k) / (b_k @ k_k)[0][0]

    return np.array([newV(np.array([[x[i]],[y[i]],[z[i]]]), (PI,PJ,PK)) for i in range(point_density**2) ])


def ex_cube():

    point_density = 29 # must equal number of datapoints so keep this at 29.

    l = 5 #length of sides

    # each letter is a vector from the origin mapping to a vertex.
    A = np.array([-l,+l,+l])
    B = np.array([-l,+l,-l])
    C = np.array([+l,+l,-l])
    D = np.array([+l,-l,-l])
    E = np.array([+l,-l,+l])
    F = np.array([-l,-l,+l])
    G = np.array([-l,-l,-l])
    H = np.array([+l,+l,+l])

    data = np.array([A,B,C,H,A,F,E,D,G,F,E,H,A,F,E,D,C,H,E,D,C,B,G,D,C,B,A,F,G,B])

    x = data[:,0]
    y = data[:,1]
    z = data[:,2]

    cube_stack = set_stack( newB(x,y,z,point_density) )
    x1, y1, z1 = cube_stack[:,0], cube_stack[:,1], cube_stack[:,2]

    fig, ax = p.subplots()
    line, = ax.plot(x, z,'w-o')
    ax.set_facecolor('#000000') #black background

    def frame(i):

        newdata = updateframe(cube_stack, 0.1 * i, 0.1 * i, 0.1 * i,point_density) # apply the rotation matrix transformation.
        line.set_data(newdata[0] - 0.5*l, newdata[2] -  0.5*l) # modified to fix rotation at centre of square.
        ax.figure.canvas.draw()
        return line,

    ani = FuncAnimation(fig, frame, 1000, init_func=None,interval=10, blit=False)

    figManager = p.get_current_fig_manager()
    if p.get_backend() == 'Qt5Agg':
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using Qt5Agg backend")
        figManager.window.showMaximized()
    elif p.get_backend() == "wx":
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using wx backend")
        figManager.frame.Maximize(True)


    p.ylim(-13,13)
    p.xlim(-13,13)
    #p.grid() # no grid now!
    p.show()


def ex_f1():

    point_density = 50

    x = np.linspace(-50,50,point_density)
    y = np.linspace(-50,50,point_density)

    def f(x,y): return  ( x**3 - 3*x ) + ( y**3 - 3*y )

    data_matrix = np.array([ [f(i,j) for j in y] for i in x])
    # where row 0 is the y values for x = 0
    # row 1 is the y values for x = 1
    # etc.

    v_set =  np.array([ [  i, j, data_matrix[i,j] ] for j in range(point_density) for i in range(point_density) ]  )

    x = v_set[:,0]
    y = v_set[:,1]
    z = v_set[:,2]

    # pass it into newBx to convert to the desired basis set
    function_1_stack = set_stack(newBx(x,y,z,point_density))

    fig, ax = p.subplots()
    line, = ax.plot(x,z, 'b.')


    def frame(i):

        newdata = updateframex(function_1_stack, 0.0 * i, 0.0 * i, 0.05 * i,point_density)
        line.set_data(newdata[0], newdata[2])
        ax.figure.canvas.draw()
        return line,

    ani = FuncAnimation(fig, frame, 1000, init_func=None, interval=10, blit=False )

    figManager = p.get_current_fig_manager()
    if p.get_backend() == 'Qt5Agg':
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using Qt5Agg backend")
        figManager.window.showMaximized()
    elif p.get_backend() == "wx":
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using wx backend")
        figManager.frame.Maximize(True)

    p.ylim(-250000,250000)
    p.xlim(-70,70)
    p.grid()
    p.show()

def ex_f2():

    point_density = 50

    x = np.linspace(-20,20,point_density)
    y = np.linspace(-20,20,point_density)

    def f(x,y): return 2*x**2 + y**2

    data_matrix = np.array([ [f(i,j) for j in y] for i in x])
    # where row 0 is the y values for x = 0
    # row 1 is the y values for x = 1
    # etc.

    v_set =  np.array([ [  i, j, data_matrix[i,j] ] for j in range(point_density) for i in range(point_density) ]  )

    x = v_set[:,0]
    y = v_set[:,1]
    z = v_set[:,2]

    # pass it into newBx to convert to the desired basis set
    function_2_stack = set_stack(newBx(x,y,z,point_density))

    fig, ax = p.subplots()
    line, = ax.plot(x,z, 'b.')


    def frame(i):

        newdata = updateframex(function_2_stack, 0.0 * i, 0.0 * i, 0.05 * i,point_density)
        line.set_data(newdata[0] - newdata[0][ np.where(z==min(z))[0][0] ] , newdata[2]) # modification to fix rotation about minimum
        ax.figure.canvas.draw()
        return line,

    ani = FuncAnimation(fig, frame, 1000, init_func=None, interval=10, blit=False )

    figManager = p.get_current_fig_manager()
    if p.get_backend() == 'Qt5Agg':
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using Qt5Agg backend")
        figManager.window.showMaximized()
    elif p.get_backend() == "wx":
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using wx backend")
        figManager.frame.Maximize(True)

    p.ylim(-100,1500)
    p.xlim(-40,40)
    p.grid()
    p.show()

# torus
def ex_param():

    point_density = 50 # personally i think it is most beautiful set to 100 with point marker style ','. but it needs good hardware.
    theta = np.linspace(0,2*pi,point_density)
    phi = np.linspace(0,2*pi,point_density)
    R = 0.6
    r = 0.4

    # we need our three parametric functions in terms of our parameters theta and phi
    def x(theta=theta,phi=phi): return (R + r*cos(theta))*cos(phi)
    def y(theta=theta,phi=phi): return (R + r*cos(theta))*sin(phi)
    def z(theta=theta,phi=phi): return r*sin(theta)

    '''
        each of x, y, and z need a matrix containing their values for all combination pairs of parameters
        theta and phi, as before when we needed all combinations of the variables x and y for our function z.
        '''
    x_matrix = np.array([ [x(i,j) for j in theta] for i in phi]) #
    y_matrix = np.array([ [y(i,j) for j in theta] for i in phi]) #
    z_matrix = np.array([ [z(i,j) for j in theta] for i in phi]) #

    '''
        we then want to extract only the range of x, y, and z values by themselves. We can do without the corresponding
        theta and phi values because we are plotting in a plane described by cartesian coordinates.
        '''
    x_set =  np.array([ x_matrix[i,j] for j in range(point_density) for i in range(point_density) ]  ) # x values
    y_set =  np.array([ y_matrix[i,j] for j in range(point_density) for i in range(point_density) ]  ) # y values
    z_set =  np.array([ z_matrix[i,j] for j in range(point_density) for i in range(point_density) ]  ) # z values



    '''now we can put them into our tried and tested code.'''
    # pass it into newBx to convert to the desired basis set
    torus_stack = set_stack(newBx(x_set,y_set,z_set,point_density))

    fig, ax = p.subplots()
    line, = ax.plot(x_set, z_set,'w,') # change 'w,' to 'w.' if you need better clarity
    ax.set_facecolor('#000000') #black background

    def frame(i):

        newdata = updateframex(torus_stack, 0.05 * i, 0.1 * i, 0.1 * i,point_density)
        line.set_data(newdata[0], newdata[2])
        ax.figure.canvas.draw()

        return line,

    ani = FuncAnimation(fig, frame, 1000, init_func=None,interval=10, blit=False )

    figManager = p.get_current_fig_manager()
    if p.get_backend() == 'Qt5Agg':
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using Qt5Agg backend")
        figManager.window.showMaximized()
    elif p.get_backend() == "wx":
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using wx backend")
        figManager.frame.Maximize(True)

    p.ylim(-1,1)
    p.xlim(-2,2)
    #p.grid()
    p.show()


def z(f,xmin,xmax,ymin,ymax,density,linestyle,withgrid,background='#ffffff'):

    x = np.linspace(xmin-5,xmax+5,density)
    y = np.linspace(ymin-5,ymax+5,density)


    data_matrix = np.array([ [f(i,j) for j in y] for i in x])

    v_set =  np.array([ [  i, j, data_matrix[i,j] ] for j in range(density) for i in range(density) ]  )

    x = v_set[:,0]
    y = v_set[:,1]
    z = v_set[:,2]

    # pass it into newBx to convert to the desired basis set
    function_2_stack = set_stack(newBx(x,y,z,density))



    fig, ax = p.subplots()
    line, = ax.plot(x,z, linestyle)
    ax.set_facecolor(background)

    def frame(i):

        newdata = updateframex(function_2_stack, 0.0 * i, 0.0 * i, 0.05 * i,density)
        line.set_data(newdata[0] - newdata[0][ np.where(z==min(z))[0][0] ] , newdata[2]) # modification to fix rotation about minimum
        ax.figure.canvas.draw()
        return line,

    ani = FuncAnimation(fig, frame, 1000, init_func=None, interval=10, blit=False )


    figManager = p.get_current_fig_manager()
    if p.get_backend() == 'Qt5Agg':
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using Qt5Agg backend")
        figManager.window.showMaximized()
    elif p.get_backend() == "wx":
        p.rcParams['toolbar'] = 'None' # Remove tool bar (upper)
        fig.canvas.window().statusBar().setVisible(False) # Remove status bar (bottom)
        print("using wx backend")
        figManager.frame.Maximize(True)

    p.ylim(-100,1500)
    p.xlim(-40,40)
    if withgrid is True:
        p.grid()
    p.show()
