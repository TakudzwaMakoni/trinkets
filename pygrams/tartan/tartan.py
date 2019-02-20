#tartan 2019 by Takudzwa Makoni (c)
import PIL.Image as I
import subprocess, os, gc, math, time

def bessie(title, version, repo, company, year, language, author, git ):
    """
    print('\n')
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n\n        {} {},   {}, {}.    \n                                 {}                   \n                         Written in {} by            \n                             {}                 \n\n           github: {}     \n\n                              \n\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n".format(title, version, repo, company, year, language, author, git) )
    print('\n')
    
    #subprocess.Popen(['afplay','-v', '0.075','trinkets/login.wav']) #run process in terminal (for terminal application) - is powerful.
    """

    subprocess.call('~/.trinkets/exec/./gws', shell=True)
    time.sleep(1)

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

    count = getsett(filename)
    with open(filename) as f_object:

        if canvas_size == 'sett':
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
            return sett, canvas_size
        elif SorR == 'r':
            for i in range(scale):
                halfsett.extend(halfsett)
            sett = halfsett
            return sett, canvas_size
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


def weaver(sett, pallet, canvas_size=1000,unit_length=1):
    canvas = I.new('RGB', (canvas_size, canvas_size), 'white')
    threads = unpacksett(sett, pallet, unit_length)
    offset = 0
    for i in threads:
        meshgrid(canvas, canvas_size, unit_length, offset, i[1], i[3])
        diagonal(canvas, unit_length, offset, i[1], i[2])
        offset += unit_length * i[1]
    gc.collect()
    
    canvas.save('patterns/'+ input('save as (png): ') + '.png')
    canvas.show()




