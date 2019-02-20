import Airhead as A



A.bessie()

def main():
    
    ##
    while True:
        if A.checkforinstructions() == False:
            userInstFile = input('enter Instruction filename / path: ')
        else:
            userInstFile = 'turtleinstructions.txt'
            A.typewriter('instructions',userInstFile)
        
        if A.fileLen(userInstFile) > 4000:
            iteratenum = A.partition(userInstFile)
            print('instruction file is large. file has been partitioned into ' + str(iteratenum) + ' files.')
            A.appendmode(iteratenum)
            break
        A.turtlecommand(userInstFile)
        cont = input("continue? (y/n)")
        if cont == 'y':
            pass
        elif cont == 'n':
            break
        else:
            print('invalid response, exiting program.')
            break






#test(0,0,0,False)
main()
A.p.show()
