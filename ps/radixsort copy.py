# for sorting lines of file ".shortcuts" in alphabetical order based on the second character in the line

import sys
from itertools import chain

ALPHA = {'a':'00','b':'01','c':'02','d':'03','e':'04','f':'05','g':'06','h':'07','i':'08','j':'09',
'k':'10','l':'11','m':'12','n':'13','o':'14','p':'15','q':'16','r':'17','s':'18','t':'19','u':'20','v':'21','w':'22','x':'23','y':'24','z':'25'}

n0,n1,n2,n3,n4,n5,n6,n7,n8,n9 = [],[],[],[],[],[],[],[],[],[]
bin = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]

bindict={
'bin0':bin[0],
'bin1':bin[1],
'bin2':bin[2],
'bin3':bin[3],
'bin4':bin[4],
'bin5':bin[5],
'bin6':bin[6],
'bin7':bin[7],
'bin8':bin[8],
'bin9':bin[9]
}

def unpack(binlist):
    return [ w[0] for w in binlist]


def reorder(oldorderlines, neworder):
    return [ oldorderlines[ neworder[ i ] ] for i in range(len(neworder)) ]

def binrefresh():
    n0,n1,n2,n3,n4,n5,n6,n7,n8,n9 = [],[],[],[],[],[],[],[],[],[]
    bin = [n0,n1,n2,n3,n4,n5,n6,n7,n8,n9]
    return bin

def local_radix_sort(lines,letter,charnum=0):
    subline = [ line for line in lines if line[charnum] == letter ]
    return global_radix_sort(subline,charnum+1,False)

def global_radix_sort(iterable,charnum=0,isfile=True,ALPHA=ALPHA,bin=bin,bindict=bindict):
    if isfile == True:
        f = open(iterable)
        lineorder = f.readlines()
    else:
        lineorder = iterable
    _pass_ = 1
    while _pass_ >= 0:
        indexlines = enumerate(lineorder)
        vals = [ [ line[0] , ALPHA[ line[1][charnum] ][_pass_] ] for line in indexlines ]
        # contains the line number and the weight on nth pass
        for val in vals:
            bin[ int(val[1]) ].append(val[0])
        # since we are appending we will need to empty each pass
        # assign weights to bins and stores line number in bins
        print(val)
        neworder = list(chain.from_iterable(bin))
        lineorder = reorder(lineorder,neworder)
        bin = binrefresh()
        _pass_ -=1
    return lineorder

inputfile = sys.argv[1]
outputfile = sys.argv[2]
initchar = int(sys.argv[3])

lineorder = global_radix_sort(inputfile,initchar)

f = open(outputfile,'w')
for i in lineorder:
    f.write(i)
f.close()

print(lineorder)



