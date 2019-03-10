# for sorting lines of file ".shortcuts" in alphabetical order based on the second character in the line

import sys, array as arr
from itertools import chain

ALPHA = {'-':25,'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,
'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25, = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
bin =[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25]





def reorder(oldorderlines, unpack):
    return [ oldorderlines[i] for i in unpack ]

def binrefresh():
    n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25, = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
    bin =[n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19,n20,n21,n22,n23,n24,n25]
    return bin

def local_radix_sort(lines,letter,charnum=0):
    subline = [ line for line in lines if line[charnum] == letter ]
    print(subline)
    return global_radix_sort(subline,charnum+1,False)

def getvars(iterable,isfile=True):
    if isfile == True:
        f = open(iterable)
        iterable = f.readlines()
    variables = []
    for i in iterable:
        v=i.split(':')[0]
        v=v.lstrip(';')
        variables.append(v)
    return variables

def global_radix_sort(iterable,charnum=0,charlim=1,isfile=True,ALPHA=ALPHA,bin=bin):
    if isfile == True:
        f = open(iterable)
        lineorder = f.readlines()
    else:
        lineorder = list(enumerate(iterable)) # preserve the true line number by casting enumerate generator 1
    while charnum <= charlim:
        indexlines = enumerate(lineorder) # reassign a virtual line number
        vals = [ ( line[0] , ALPHA[ line[1][1][charlim] ] ) for line in indexlines ]
        # contains the line number and the weight on nth pass
        for val in vals:
            bin[ val[1] ].append(val[0])
        # since we are appending we will need to empty each pass
        # assign weights to bins and stores line number in bins
        unpack = list(chain.from_iterable(bin)) # list of lines in bins
        lineorder = reorder(lineorder,unpack)
        bin = binrefresh()
        charlim -=1
    return lineorder

inputfile = sys.argv[1]
outputfile = sys.argv[2]
initchar = int(sys.argv[3])

v = getvars(inputfile)
padfactor = len(max(v,key=len).rstrip('\n'))
for i in range(len(v)):
    v[i] = v[i] + '-' * (padfactor - len(v[i].strip('\n')))
lineorder = global_radix_sort(v,initchar,padfactor - 1,False)

#lineorder = global_radix_sort(v,initchar,0,False)
#print(lineorder, padfactor)

f = open(outputfile,'w')
f2 = open(inputfile)
lines = f2.readlines()
f2.close


for i in lineorder:
    f.write(lines[i[0]])
f.close()

#neworder isnt the latest order?
