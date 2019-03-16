#tartan by Takudzwa Makoni (c) 2019
import tartan as t
import gc, os, subprocess

def help():
    subprocess.run("cat $HOME/.trinkets/pygrams/tartan/.help")
gc.collect()

pallet = {'HG':'#285800','K':'#101010','R':'#C80000','W':'#E0E0E0','Y':'#E8C000', 'LN':'#C0C0C0','TK':'#8C7038','RB':'#0C585C','DR':'#880000','GO':'#FFD700','MB':'#3474FC','RC':'#5C5C5C','BB':'#14283C','EG':'#004028','DB':'#202060','DGR':'#003C14','RSB':'#1C0070','WW':'#FCFCFC','MU':'#D09800','G':'#006818','YT':'#D8B000','NB':'#5C4827','WB':'#5D432C','THB':'#32282B','KCO':'#252321','BRG':'#004225','CHA':'#F7E7CE','TB':'#1375A1'}

canvas_size0 = input('canvas size (pixels): ')
while not str.isdigit(canvas_size0):
    print(canvas_size0)
    if canvas_size0 == '.q':
        exit(0)
    elif canvas_size0 == '.h':
        help()
        canvas_size0 = input('try again, or ".h"/".q" for "help"/"quit": ')
    else:
        print('error: canvas size must be an integer.')
        canvas_size0 = input('try again, or ".h"/".q" for "help"/"quit": ')


unit_length = 1

filename = input('path to threadcount file (txt): ') + '.txt'
while not os.path.isfile(filename):
    print(filename)
    if filename == '.q':
        exit(0)
        print('test')
    elif filename == '.h':
        help()
        filename = input('try again, or ".h"/".q" for "help"/"quit": ')
    else:
        print('error: no such file found.')
        filename = input('try again, or ".h"/".q" for "help"/"quit": ')

SorR = input('symmetric or repetitive pattern (s/r): ')
while SorR is not 'r' and SorR is not 's':
    if SorR == '.q':
        exit(0)
    elif SorR == '.h':
        help()
        SoR = input('try again, or ".h"/".q" for "help"/"quit": ')
    else:
        print('error: you must choose either "s" or "r"')
        SorR = input('try again, or ".h"/".q" for "help"/"quit": ')

sett, canvas_size1, directory_check = t.modlist(filename,SorR, canvas_size0)
print('weaving...')
t.weaver(sett, pallet, canvas_size1, unit_length, directory_check)
gc.collect()

