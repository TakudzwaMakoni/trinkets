#tartan by Takudzwa Makoni (c) 2019
import tartan as t
import gc

title, version, repo, company, year, language, author, git = 'tartan','alpha','freedomfighter (c)','Milli (c)', '2018','Python 3.6', 'Takudzwa Makoni','https://github.com/Makoni-Milli/'

t.bessie(title, version, repo, company, year, language, author, git)

gc.collect()

pallet = {'HG':'#285800','K':'#101010','R':'#C80000','W':'#E0E0E0','Y':'#E8C000', 'LN':'#C0C0C0','TK':'#8C7038','RB':'#0C585C','DR':'#880000','GO':'#FFD700','MB':'#3474FC','RC':'#5C5C5C','BB':'#14283C','EG':'#004028','DB':'#202060','DGR':'#003C14','RSB':'#1C0070','WW':'#FCFCFC','MU':'#D09800','G':'#006818','YT':'#D8B000','NB':'#5C4827','WB':'#5D432C','THB':'#32282B','KCO':'#252321','BRG':'#004225','CHA':'#F7E7CE','TB':'#1375A1'}

canvas_size0 = input('canvas size (pixels): ')
unit_length = 1
filename = input('threadcount file (txt): ') + '.txt'
SorR = input('symmetric or repetitive (s/r): ')
sett, canvas_size1 = t.modlist(filename,SorR, canvas_size0)
print('weaving...')
t.weaver(sett, pallet, canvas_size1, unit_length)
gc.collect()

