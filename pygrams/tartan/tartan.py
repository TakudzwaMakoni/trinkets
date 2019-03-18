#tartan 2019 by Takudzwa Makoni (c)
import PIL.Image as I
import subprocess, os, gc, math

pallet = {'HG':'#285800','K':'#101010','R':'#C80000','W':'#E0E0E0','Y':'#E8C000', 'LN':'#C0C0C0','TK':'#8C7038','RB':'#0C585C','DR':'#880000','GO':'#FFD700','MB':'#3474FC','RC':'#5C5C5C','BB':'#14283C','EG':'#004028','DB':'#202060','DGR':'#003C14','RSB':'#1C0070','WW':'#FCFCFC','MU':'#D09800','G':'#006818','YT':'#D8B000','NB':'#5C4827','WB':'#5D432C','THB':'#32282B','KCO':'#252321','BRG':'#004225','CHA':'#F7E7CE','TB':'#1375A1'}

manual = { "canv":(25,26), "path":(16,23), "pattern":(64,65), "colour":(32,62), "thread":(28,30), "section":(6,14) }


def help(params, manual=manual):
    try:
        ref = params.split()[1]
        start, stop = manual[ref]
        padding = int(subprocess.run(['tput', 'cols'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\n'))
        border = ' *' * int( 1/4 * padding)
        print( '\n', ' '*( (padding-len(border)) // 2) + border ,'\n' )
        print('MAN'+ref)
        with open(os.path.expanduser("~/.trinkets/pygrams/tartan/.help")) as f:
            manpage = f.readlines()[ start:stop ]
            for line in manpage:
                print(line,end="")
        print( '\n', ' '*( (padding-len(border)) // 2) + border ,'\n' )
    except:
        padding = int(subprocess.run(['tput', 'cols'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\n'))
        border = '* ' * int( 1/4 * padding)
        print( '\n', ' '*( (padding-len(border)) // 2) + border ,'\n' )
        print('MAN0')
        with open(os.path.expanduser("~/.trinkets/pygrams/tartan/.help")) as f:
            for line in f:
                print(line.strip("\n"))
        print( '\n', ' '*( (padding-len(border)) // 2) + border ,'\n' )
def getsett(filename):
    with open(filename) as f:
        lines = f.readlines()
        count = 0
        for i in lines:
            numbers = i.split()[1]
            count += int(numbers)
    return count


def modlist(filename, SorR, canvas_size):

    if os.path.isfile(filename) == False:
        filename = 'threadcounts/' + filename
        directory_check = False
    else:
        directory_check = True

    count = getsett(filename)
    with open(filename) as f_object:

        if int(canvas_size) == 0:
            canvas_size = count
        else:
            canvas_size = int(canvas_size)

        scale = canvas_size // count
        if scale > 8:
            scale = 8
        halfsett = f_object.readlines()
        if SorR == 's':
            sett = halfsett + halfsett[::-1]
            for i in range( scale  // 2 ):
                sett.extend(sett)
            return sett, canvas_size, directory_check
        elif SorR == 'r':
            for i in range(scale):
                halfsett.extend(halfsett)
            sett = halfsett
            return sett, canvas_size, directory_check
        else:
            exit(1)

def unpacksett(sett,pallet, unit_length):
    truesett = []
    for i in sett:
        pixel_data = i.split()
        pixel_colour, pixel_size = pallet[pixel_data[0]], int(pixel_data[1])
        pixel = I.new('RGB', (unit_length * pixel_size, unit_length * pixel_size), pixel_colour)
        m_pixel = I.new('RGB', ( unit_length, unit_length ), pixel_colour)
        truesett.append( [pixel_colour,pixel_size, pixel, m_pixel] )
    gc.collect()
    return truesett

def meshgrid( canvas, canvas_size, unit_length, offset, pixel_size, m_pixel ):
    offset2 = offset
    for j in range(pixel_size):
        x_offset_diverge = offset
        y_offset_diverge = offset
        x_offset_diverge2 = offset
        y_offset_diverge2 = offset
        for i in range(canvas_size):
            canvas.paste( m_pixel, (x_offset_diverge + j, offset2 ) )
            canvas.paste( m_pixel, (offset2,y_offset_diverge + j) )
            y_offset_diverge += unit_length
            x_offset_diverge += unit_length
            canvas.paste( m_pixel, (x_offset_diverge2 + j, offset2 ) )
            canvas.paste( m_pixel, (offset2,y_offset_diverge2 + j) )
            y_offset_diverge2 +=  -2 * unit_length
            x_offset_diverge2 += -2 * unit_length
        gc.collect()
        offset2 += unit_length
    gc.collect()

def diagonal( canvas, unit_length, offset, pixel_size, pixel ):
    canvas.paste(pixel, ( offset , offset))
    canvas.paste(pixel, ( unit_length + offset , offset)) #horizontal paste
    canvas.paste(pixel, ( offset , unit_length + offset))


def weaver(sett, canvas_size=1000, unit_length=1, directory_check=True, pallet=pallet):
    canvas = I.new('RGB', (canvas_size, canvas_size), 'white')
    threads = unpacksett(sett, pallet, unit_length)
    offset = 0
    for i in threads:
        meshgrid(canvas, canvas_size, unit_length, offset, i[1], i[3])
        diagonal(canvas, unit_length, offset, i[1], i[2])
        offset += unit_length * i[1]
    gc.collect()

    if directory_check == False:
        canvas.save('patterns/'+ input('save as (png): ') + '.png')
    else:
        canvas.save( input('save as (png): ') + '.png')
    canvas.show()




