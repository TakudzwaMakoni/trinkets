import framex

examples = {'cube': framex.ex_cube,'f1': framex.ex_f1,'f2': framex.ex_f2,'param': framex.ex_param }

while 1:
    user_in = input('-> ')
    try:
        examples[user_in]()
    except:
        if user_in == '.q' or user_in == 'exit':
            exit()
        else:

            type,f,xmin,xmax,ymin,ymax, density, linestyle,withgrid, background = user_in.split(',')
            
            if type == 'z':
                framex.z(f,xmin,xmax,ymin,ymax, density, linestyle,withgrid, background)
        
        print('that is its own function.')

