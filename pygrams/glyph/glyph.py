import os,re, base30, subprocess
import PIL.Image as I


imdb = ['glyphs/space.png', 'glyphs/la1.png', 'glyphs/lb.png', 'glyphs/lc.png', 'glyphs/ld.png', 'glyphs/le1.png',
        'glyphs/lf.png', 'glyphs/lg.png', 'glyphs/lh.png', 'glyphs/li1.png', 'glyphs/lj.png',
        'glyphs/lk.png','glyphs/ll.png','glyphs/lm.png', 'glyphs/ln.png', 'glyphs/lo1.png','glyphs/lp.png', 17, 18, 19, 20, 21,
        22, 23, 24, 25, 26, 'glyphs/ca1.png','glyphs/cb.png', 'glyphs/cc.png', 'glyphs/cd.png', 'glyphs/ce1.png',
        'glyphs/cf.png', 'glyphs/cg.png', 'glyphs/ch.png', 'glyphs/ci1.png', 'glyphs/cj.png', 'glyphs/ck.png',
        'glyphs/cl.png', 'glyphs/cm.png', 'glyphs/cn.png', 'glyphs/co1.png', 'glyphs/cp.png', 43, 44, 45, 46, 47, 48, 49, 50, 51, 52,
        'glyphs/la2.png', 'glyphs/le2.png', 'glyphs/li2.png', 56, 57, 58, 59, 60, 61,
        'glyphs/ca2.png', 'glyphs/ce2.png', 'glyphs/ci2.png', 65, 64, 67, 68, 69, 70, 'glyphs/stop.png',
        'glyphs/comma.png', 73, 74, 75, 76, 77, 78, 79]

imdb2 = ['redglyphs/1.png','redglyphs/2.png','redglyphs/3.png','redglyphs/4.png','redglyphs/5.png','redglyphs/6.png','redglyphs/7.png','redglyphs/8.png',
         'redglyphs/9.png','redglyphs/10.png','redglyphs/11.png','redglyphs/12.png','redglyphs/13.png','redglyphs/14.png','redglyphs/15.png','redglyphs/16.png',
         'redglyphs/17.png','redglyphs/18.png','redglyphs/19.png','redglyphs/20.png','redglyphs/21.png','redglyphs/22.png','redglyphs/23.png','redglyphs/24.png',
         'redglyphs/25.png','redglyphs/26.png','redglyphs/27.png','redglyphs/28.png','redglyphs/29.png','redglyphs/0.png',
         
         'newglyphs/1.png','newglyphs/2.png','newglyphs/3.png','newglyphs/4.png','newglyphs/5.png','newglyphs/6.png','newglyphs/7.png','newglyphs/8.png',
         'newglyphs/9.png','newglyphs/10.png','newglyphs/11.png','newglyphs/12.png','newglyphs/13.png','newglyphs/14.png','newglyphs/15.png','newglyphs/16.png',
         'newglyphs/17.png','newglyphs/18.png','newglyphs/19.png','newglyphs/20.png','newglyphs/21.png','newglyphs/22.png','newglyphs/23.png','newglyphs/24.png',
         'newglyphs/25.png','newglyphs/26.png','newglyphs/27.png','newglyphs/28.png','newglyphs/29.png','newglyphs/0.png']



def bessie():
    print('\n')
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n        glyph 2.0.1   freedomfighter (ff) (c), Milli (c).    \n                                 2017-2018                   \n                         Written in Python 3.6 by            \n                             Takudzwa Makoni                 \n\n     GitHub: https://github.com/Millisoft/freedomfighter     \n\n                              \n\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n" )
    print('\n')
    subprocess.Popen(['afplay','-v', '0.075','trinkets/login.wav']) #run process in terminal (for terminal application) - is powerful.


#converts elements to string splits up the string characters
#in an element into separate elements of a list, also converts any
#integers to base 30
def fix(li):
    li2 = []
    for el in li:
        if isinstance(el,str):
            for i in el:
                li2.append(i)
        else:
            li2.append(el)

    li3 = []
    for el in li2:
        if isinstance(el,int):
            c = base30.converter(el)
            c.append('\n')
            li3 += c
        else:
            li3.append(el)
    return li3


#cleanup will automatically remove the generated imagelines
#once they have been used to make the final image.
#It will also ask the user if they want to keep the message imageline.txt
def cleanup(count):
    for i in range(count):
        os.remove('line'+str(i)+'.png')


#will ask the user if they want to add character spacing, and what to
#set the linespacing to
def getspacingopt():
    while True:
        linespacing = input('enter line spacing ')
        if linespacing == '.quit':
            print('exiting program')
            exit(1)
        else:
            try:
                ilinespacing = int(linespacing)
                return ilinespacing
            except:
                print('you have not entered an integer!')
                subprocess.Popen(['afplay','-v', '0.075','trinkets/error.wav'])

#add characters between list or string
def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

#find and replace (for words). the same function can be modified for
#numbers abover 9
def frw(string):
    a = [('ch','x'),('th','q'),('sh','c'),('ih','y')]
    for ch in a:
        if ch[0] in string:
            string = string.replace(ch[0],ch[1])
    # for el in string.split():
    #    if el.isdigit():
    #        el = ''.join(str(x) for x in base30.converter(el))
    return string
#will read the message in imageline.txt character by character and
#produce an ordered list of imagefiles containing symbols to  translate
#the message
def translate(message,database=imdb2):
   
    a = message
    b = a.split(' ')
    c = intersperse(b,'-')
    
    newlist = []
    for j in c:
        try:
            newlist.append(int(j))
        except:
            newlist.append(j)

    d = intersperse(fix(newlist),' ')

    dict1 ={"-":"glyphs/space.png"," ":"glyphs/smallspace.png",1:database[0],2:database[1],3:database[2],4:database[3],5:database[4],6:database[5],7:database[6],8:database[7],9:database[8],10:database[9],11:database[10],12:database[11],13:database[12],14:database[13],15:database[14],16:database[15],17:database[16],18:database[17],19:database[18],20:database[19],21:database[20],22:database[21],23:database[22],24:database[23],25:database[24],26:database[25],27:database[26],28:database[27],29:database[28],0:database[29],

    "l":database[30],"t":database[31] ,"g":database[32] ,"v":database[33] ,"k":database[34] ,"ee":database[35] ,"n":database[36] ,"w":database[37] ,"d":database[38] ,"m":database[39] ,"s":database[40] ,"x":database[41] ,"q":database[42] ,"i":database[43] ,"h":database[44] ,"å":database[45] ,"z":database[46] ,"e":database[47] ,"oo":database[48],"r":database[49] ,"oh":database[50] ,"j":database[51] ,"f":database[52] ,"p":database[53] ,"u":database[54] ,"a":database[55] ,"y":database[56] ,"b":database[57] ,"c":database[58] ,"o":database[59]}
    
    imagelist = ["glyphs/smallspace.png" if ch == "\n" else dict1[ch] for ch in d]
    return imagelist

#checks if there already is a message 'imageline.txt' and
#asks the user if they want to continue with that on or overwrite it
def checkforimagline():
    if os.path.isfile('imageline.txt'):
        os.remove('imageline.txt')


#opens file given by user and writes contents to imageline.txt
def getimportedfile():
    while True:
        importask = input('import file? (y/n) ')
        if importask == 'y':
            print('entering import mode...')
            checkforimagline()
            filename = input('enter file name (.txt) ')
            if filename == '.quit':
                print('exiting the program')
                exit(1)
            elif filename == '|type':
                print('exiting import mode...')
                typewriter()
                break
            else:
                try:
                    open('imageline.txt', 'w').writelines([frw(l) for l in open(filename).readlines()] + ['\n'])
                    print('the file "' + filename + '" was imported')
                    return True
                except:
                    print('error: could not open the file "' + filename + '.txt"')
                    subprocess.Popen(['afplay','-v', '0.075','trinkets/error.wav'])
        elif importask == '.quit':
            print('exiting program')
            exit(1)
        elif importask == 'n':
            print('exiting import mode...')
            typewriter()
            break
        else:
            print('invalid entry! enter "y" for yes or "n" for no.')
            subprocess.Popen(['afplay','-v', '0.075','trinkets/error.wav'])





#allows the user to type line by line into the terminal on prompt. the message is saved
#to imageline.txt
def typewriter():
    print('entering typewriter mode...')
    print('info: enter "|end" on a new line to end entry any time.')
    with open('imageline.txt', 'a') as f1:
        while True:
            message = frw(input('insert message '))
            if message == '|end':
                break
            elif message == '|import':
                print('exiting typwriter mode...')
                getimportedfile()
                break
            elif message == '.quit':
                print('exiting program')
                exit(1)
            else:
                f1.write(message + '\n')

#opens the imageline.txt file and reads it line by line.
#the translate function will then be performed onto each line
#it then pruduces a list containing lists of the imagefiles for each translated line, which is the
#returned translated message
def translatemessage(addspaces='n'):
    with open('imageline.txt', 'r') as f2:
        file = f2.readlines()
        translatedmessage = []
        for line in file:
            translatedline = translate(line)
            if addspaces == 'y':
                intersperse(translatedline,'glyphs/smallspace.png')
            translatedmessage.append(translatedline)
    return translatedmessage


def rsz(img_object,scale):
    nwidth, nheight = tuple( [ int(i * scale) for i in img_object.size ] )
    if nwidth <= 0:
        nwidth = 1
    if nheight <= 0:
        nheight = 1
    nimg = img_object.resize( (nwidth, nheight) , I.ANTIALIAS )
    return nimg



#the image is created using the translated message returned by the translatemessage
#function, done by attaching symbol images horizontally to create each line, then attaching the lines vertically -
#creating an image matrix.
def createmessageimage(listoftranslatedlines, numspaces, msize=3, hfsize=5):
    count = 0
    imlist = []
    newlinespace    =  'glyphs/newlinespace.png'
    smallspace      =    'glyphs/smallspace.png'
    
    for line in listoftranslatedlines:
        #adds the margin
        for i in range(msize):
            line.insert(0,smallspace)
            line.insert(-1,smallspace)
        
        images = list(map(I.open, line))
        #resize
#        rimages = []
#        for i in images:
#            rimages.append( rsz(i,0.1) )
        #transpose image
        imflip = []
        for i in images:
            new = i.transpose(I.FLIP_LEFT_RIGHT)
            imflip.append(new)
        widths, heights = zip(*(i.size for i in imflip))
        total_width = sum(widths)
        max_height = max(heights)
        new_im = I.new('RGB', (total_width, max_height), 'white')
        x_offset = 0
        for im in imflip:
            new_im.paste(im, ( x_offset ,0))
            x_offset += im.size[0]
        new_im.save('line'+ str(count) + '.png')
        imlist.append('line'+ str(count) + '.png')
        count += 1
    
                          
    #### modifications for reversal
    
    count = len(imlist)
    iterative = 1
    for i in range(count):
        for x in range(numspaces):
            imlist.insert(i + iterative, newlinespace)
        iterative += numspaces
    
    #adds the header and footer
    for i in range(hfsize):
        imlist.insert(-1,newlinespace)
        imlist.insert(0,newlinespace)
    
    finalimages = list(map(I.open, imlist))

    imrevf = []
    for i in reversed(finalimages):
        imrevf.append( rsz(i,0.2) )
        widths, heights = zip(*(i.size for i in imrevf))
        max_width = max(widths)
        total_height = sum(heights)
        new_im = I.new('RGB', (max_width, total_height), 'white')
        y_offset = 0
        for im in imrevf:
            new_im.paste(im, (0, y_offset))
            y_offset += im.size[1]
    msg = new_im.transpose(I.FLIP_LEFT_RIGHT)
    saveask = input('save image? (y/n) ')
    if saveask == 'y':
        saveasask = input('save image as: ')
        msg.save(saveasask +'.png')
    return count


