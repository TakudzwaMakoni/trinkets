from matplotlib import pyplot as p
import math, os, subprocess

def checkforinstructions():
    cont = 'y'
    while cont == 'y':
        if os.path.isfile('turtleinstructions.txt'):
            usercommand = input("Instructions already exist in 'turtleinstructions.txt' file. enter 'ow' to overwrite, or 'ap' to append to.\ntype 'path' to ignore and use a external instruction file in the working directory or using a path. ")
            if usercommand == 'ap':
                cont = 'n'
            elif usercommand == 'ow':
                os.remove('turtleinstructions.txt')
                cont = 'n'
            elif usercommand == 'path':
                return False
            else:
                print('invalid entry.')
                cont = 'y'
        else:
            promptforfile = input("no instruction file 'turtleinstructions.txt' exists in the working directory.\nenter 'type' to type instructions in terminal, and 'path' to enter the path\nof an external instrucion file, or the name of that instruction file if it\nexists in the working directory. ")
            if promptforfile == 'type':
                cont = 'n'
            elif promptforfile == 'path':
                return False
            else:
                print("invalid entry")
                cont = 'y'
    return True

def typewriter(inputtype, filename):
    print("info: enter '|end' on a new line to end entry any time.")
    while True:
        with open(filename, 'a') as f1:
            message = input("insert " + inputtype + ": ")
            if message == '|end':
                f1.close()
                break
            else:
                f1.write(message + '\n')
        f1.close()

def bessie():
    print('\n')
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n    Airhead 1.2.1   freedomfighter (ff), Milli group (c).    \n                                 2017-2018                   \n                         Written in Python 3.6 by            \n                             Takudzwa Makoni                 \n\n     GitHub: https://github.com/Millisoft/freedomfighter     \n\n                 use ’.quit’ to exit the program             \n\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n" )
    print('\n')
    
    subprocess.Popen(['afplay','-v', '0.075','trinkets/login.wav']) #run process in terminal (for terminal application) - is powerful.


def draw(points):                                   # draw function from 2.5; takes the x and y values and plots them in the forward down condition
    x = []
    y = []
    for i in range(0,len(points)):
        x.append(points[i][0])
        y.append(points[i][1])
        p.plot(x,y)
def fileLen(filename):                              # get number of commands/argument lines in file
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
def forward(penState, magnitude):                   #  will update penState and therefore moves the turtle forward and draws onto the graph in the down condition
    # print(penState, magnitude) for debugging (remove to see line by line instructions carried)
    x = penState[0]
    y = penState[1]
    angle = penState[2]
    state = penState[3]
    newX = x + magnitude*math.cos(angle)
    newY = y + magnitude*math.sin(angle)
    updateTurtle = (newX, newY, angle, state)
    if state == False:
        return updateTurtle
    if state == True:
        listOfTuples = [(x,y),(newX,newY)]
        draw(listOfTuples)                          # draw line from previous x and y to new x and y
        return updateTurtle                         # returns the updated position of the turtle for ned iteration
def rotate(penState, magnitude):
    x = penState[0]
    y = penState[1]
    angle = penState[2]
    state = penState[3]
    updateAngle = angle + magnitude                 # updates heading of turtle
    updateTurtle = (x,y,updateAngle,state)
    return updateTurtle                             # returns updated penState tuple
def Pen(penState, turtleState):
    x = penState[0]
    y = penState[1]
    angle = penState[2]
    state = penState[3]
    if turtleState == "UP":
        state = False
        updateTurtle = (x, y, angle, state)
        return updateTurtle                         # returns updated PenState tuple
    else:
        state = True
        return x, y, angle, state
def test(x,y,angle,state):                          # tests for error in functions
    testPen =  (x,y,angle,state)
    fwdtest = forward(testPen, 100)
    if fwdtest == (0,0,0,False):
        x = None
    else:
        exit('forward function is broken')
    rotateTest = rotate(testPen,1)
    if rotateTest == (0,0,1,False):
        x = None
    else:
        exit('rotate function is broken')
    upTest = Pen(testPen, 'UP')
    if upTest == (0, 0, 0, False):
        x = None
    else:
        exit('pen function is broken in up parameter')
    downTest = rotate(testPen, "DOWN")
    if downTest == (0, 0, 1, True):
        x = None
    else:
        exit('pen function is broken in down parameter')

def partition(file):
    with open(file, 'r') as f:
        instructions = f.readlines()
        chunks = [instructions[x:x+500] for x in range(0, len(instructions), 500)]
        num = 0
        for i in chunks:
            with open('partitionfile' + str(num) + '.txt', 'w') as fi:
                fi.write('PEN,DOWN\n')
                for j in i:
                    fi.write(j)
            num += 1
    numofinst = len(chunks)
    return numofinst
#append multiple file

def turtlecommand(file):
    x = 0
    y = 0
    angle = 0
    p.axis('square')
    p.axis([-500, 500, -500, 500])
    state = False
    turtle = (x, y, angle, state)
    f = open(file, 'r')
    numberOfInst = fileLen(file)                        # assigns variable to number of command/argument instruction lines in file
    print('processing ' + str(numberOfInst) + ' instructions...')   # for debugging
    for li in f:
        listOfInst = li.split(',')
        try:
            command = listOfInst[0]
            argument = listOfInst[1]
        except:
            pass
        if command == "PEN":
            # print('apples') for debugging
            argument = argument.rstrip()
            turtle = Pen(turtle, argument)
        elif command == "FWD":
            # print('pears') for debugging
            turtle = forward(turtle, float(argument))
        elif command == "ROT":
            # print('carrots') for debugging
            argument = float(argument)
            argument = math.radians(argument)
            turtle = rotate(turtle, argument)
        else:
#            print('error: commmand is invalid')
#            exit(2)
            pass
def appendmode(num):
    print(num)
    listoffiles = []
#    typewriter('filenames','partitionedfilenames.txt')
    for i in range(num):
        listoffiles.append('partitionfile' + str(i) + '.txt')
    print(listoffiles)
    for i in listoffiles:
        turtlecommand(i)



