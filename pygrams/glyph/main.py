#glyph
import os
import glyph as g #test mode: testglyph

g.bessie()
def main():
    #g.checkforimagline()
    g.getimportedfile()
    spacingsettings = ('y', g.getspacingopt()) #set to 'y' to intersperse characters.
    characterspacing = spacingsettings[0]
    linespacing = spacingsettings[1]
    
    count = g.createmessageimage(
        g.translatemessage(characterspacing),
        linespacing
    )
    g.cleanup( count )
main()

