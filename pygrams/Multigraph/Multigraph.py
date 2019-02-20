from matplotlib.pyplot import plot
import os, subprocess


# the master function is the main function of the program
# the main power in the master function is its ability
# to run as many times as the user needs, creating as many files,
# containing all data for a single country, as the user wishes in one
# run of the program. the user can decide which of these countries they
# wish to plot to a graph whilst keeping the files even for the countries
# they dont wish to graph. the user does not have to rerun the program if
# it fails to find data for a country. the master function takes the most
# advantage of the modularity of the rest of the functions
def master(database_file, quantities_file):
    # continueprompt is initialised as string 'y' so that the below while code can start.
    # the user can continue to write files containing datasets for different
    # countries until entering some other value than 'y' when prompted
    continueprompt = 'y'
    page = 0
    while continueprompt == 'y':
        show_help = input(color.prompt + 'show user manual? (y/n), or any key to continue ' + color.end)
        if show_help == '.quit':
            print('exiting the program')
            exit(1)
        if show_help == 'y':
            start_info()
        # the 'master-value' is a tuple containing the dataset, output
        # filename, and the users decision to rerun the program.
        # master will call multifile and plot the data if the user chooses 'y'
        master_value = multi_file(database_file, quantities_file)

        if master_value[0] == None:
            # master[0] returning none implies there was no error in finding the data
            # the program should not ask to plot data if no data was found,
            # so askplot is only defined if master[0] is None.
            # if there was an error then the file will not have been created in multifile, and
            # the country name/code may have likely been miskeyed. so 'country' and 'outputfile',
            # so both these values only need to be defined if the master[0] is None.

            outputfile = master_value[1] + '.txt'
            # gets name and code of specified country as exact in database
            # file from search_called in multifile by the master function.
            # master_value[3] is a tuple containing the the country name
            # and the country code in [0] and [1] respectively.
            country = master_value[2]
            get_name_and_code = master_value[3]

            askplot = input(color.prompt + 'plot data for ' + get_name_and_code[0] +
                            " (" + get_name_and_code[1] + ")" + '? (y/n) ' + color.end)

            if askplot == '.quit':
                print('exiting the program')
                return
            # if user confirmed to plot the data it will use the values retrieved from
            # multifile by master to plot the graph
            if askplot == 'y':
                print('reading file "' + outputfile + '".')
                xlist = list(range(2000, 2016))
                # print(outputfile)  # for debugging
                a = get_quantity(quantities_file)
                # print(a) #for debugging

                print('plotting data options are as listed:\n')

                # will show the user in console which number to enter to get plot for specific quantity type
                show_data_options(a)

                # the number chosen by user is stored into variable 'plot_data'

                invalid = 'y'
                while invalid == 'y':
                    plot_data = input(color.prompt + '\nplotting for which data? ' + color.end)
                    try:
                        if plot_data == '.quit':
                            print('exiting the program')
                            return
                        if 0 > int(plot_data):
                            print(
                                color.error + '\ninvalid range; enter an integer within the range for data' + color.end)
                            invalid = 'y'
                        # -2 is the correction from calling file_len (which adds 1)
                        elif int(plot_data) > (file_len(quantities_file) - 1):
                            print(file_len(quantities_file))
                            print(
                                color.error + '\ninvalid range; enter an integer within the range for data' + color.end)
                            invalid = 'y'
                        else:
                            invalid = 'n'
                    except:
                        print(color.error + '\ninvalid input; value must be a number' + color.end)
                        invalid = 'y'

                if plot_data == '.quit':
                    print('exiting the program')
                    return

                # the outputfile created by multifile pulled retrieved from master will be read
                # to reduce to a single list of data for y values
                f = open(outputfile, 'r')
                b = f.readlines()
                b = b[int(plot_data)]  # outputfile is ordered in symmetry to quantities file
                b = b.strip('\n')  # newline character is removed
                b = b.split('/')  # string is converted to list of strings containing the data as strings
                # print(b)           #for debugging
                del b[-1]  # deletes the excess '' element in list.
                # print(b)
                f.close()

                # format_to_float will return the list with each element converted
                # into floating point values, to be assigned to variable 'yvalues'
                yvalues = format_to_float(b)
                # print(yvalues) #for debugging


                # print(file_len(quantities_file)) #for debugging
                # will plot the data onto a graph with label
                # being as chosen by user. Imported from matplotlib.pyplot

                plot(xlist, yvalues, label=a[int(plot_data)] + ' "' + get_name_and_code[1] + '"')
                print(color.info + '\nplotted data for "' + country + '".' + color.end)
            else:
                # if the condition 'master[0] == None' was not met the above code should
                # not be performed. instead do nothing and wait to prompt user to try to run
                # again.
                pass
                # else:
                # askplot = None
        if master_value[0] != None:
            # master[0] returned a string value, so multifile was unable to find data.
            # multifile already asked if the user wanted to retry at that point (y/n); continueprompt
            # will assume this value.
            continueprompt = master_value[0]
        else:
            # master[0] from calling multifile returned none value, so the program
            # ran as normal. The program still needs to ask user if they wish to run program again
            # to create new data file or plot another graph on same figure.
            print('\nDone.\n')

            keep_file_prompt = input(
                color.prompt + 'do you want to keep the file "' + outputfile + '"? (y/n) ' + color.end)
            if keep_file_prompt == 'n':
                confirm_delete = input(color.prompt + 'the file "' + outputfile + '" will be deleted. are you'
                                                                                  ' sure? (y/n) ' + color.end)
                if confirm_delete == 'y':
                    print(color.info + '\nthe file "' + outputfile + '" was deleted.\n' + color.end)
                    os.remove(outputfile)
                elif confirm_delete == 'n':
                    print(color.info + '\nkeeping file "' + outputfile + '" in local directory.' + color.end)
                else:
                    print(color.error + '\ninvalid input; keeping the file in local directory.\n' + color.end)
            elif keep_file_prompt == 'y':
                print(color.info + '\nkeeping file "' + outputfile + '" in local directory.' + color.end)
            else:
                print(color.error + '\ninvalid input; keeping the file in directory.\n' + color.end)

            print(color.info + "you may add more plots/create more files.\n(run again to add more plots to graph)\n"
                               "(if plotting again, this will be on the same figure)\n" + color.end)
            continueprompt = input(color.info + "if opted to plot, plot will show after exiting." + color.end +
                                   color.prompt + "\nrun again? (y/n), or enter any other key to exit. " + color.end)
            print(
                color.prompt + "\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:." + color.end,
                end=' ')
        print(color.prompt + 'page', page, '\n\n' + color.end)
        page = page + 1


def show_data_options(data_list):
    n = 0
    for i in data_list:
        if n < 10:
            print('enter    ', color.info + str(n) + color.end, '    for', end='      ')
            print(i)
        # below is a very subtle formatting correction when printing to screen to
        # ensure all tabulated info is in line. the number of spaces in the
        # print statement for n > 10 (two digits) is less by one than others.
        else:
            print('enter   ', color.info + str(n) + color.end, '    for', end='      ')
            print(i)
        n = n + 1


# silent mode OFF (n) or default prints all running processes, useful for debugging.
# the smvalue, to be later used by functions, is assigned to either True or False.
# using string smprompt in the function set_silent_mode.
def multi_file(inputfile, qfile, silent_mode=False):
    try:
        smprompt = input(color.prompt + 'run in silent mode? (y/n) ' + color.end)

        if smprompt == '.quit':
            print('exiting the program')
            return '.quit'
        smvalue = set_silent_mode(smprompt)

        confirm = 'n'
        while confirm == 'n':
            country = input(color.prompt + 'enter country name or country code: ' + color.end)
            if country == '.opt':
                show_country_opts(inputfile, qfile)
                country = input(color.prompt + 'enter country name or country code: ' + color.end)
            if country == '.quit':
                print('exiting the program')
                return '.quit'
            # runs an initial search_data operation to verify/retrieve the exact country name and code
            # so that the user is best informed which country the data will be found for.
            # search_data(get_quantity(qfile)[0],inputfile,country,True)[1] is a
            # tuple containing the exact country name and code for the given country entry.
            # it takes a sample search reading using search_data and, arbitrarily the nth element in qfile;
            # in this case qfile[0], but it can be any valid element index in qfile.
            exact_to_db = search_data(get_quantity(qfile)[0], inputfile, country, True)[1]
            print('found country name and code as exact to database: ' + color.info + exact_to_db[0]
                  + ' (' + exact_to_db[1] + ')' + color.end)
            confirm = input(
                color.prompt + "is this the correct country? 'y' (or any key) to continue or 'n' to try search again. " + color.end)
            if confirm == '.quit':
                print('exiting the program')
                return '.quit'

        conflict_check = 'y'
        while conflict_check == 'y':
            filename = input(color.prompt + 'create name of output file for ' + exact_to_db[0]
                         + ' (' + exact_to_db[1] + ')' + ': ' + color.end)
            if filename == '.quit':
                print('exiting the program')
                return '.quit'

            if os.path.isfile(filename + '.txt'):
                print(color.error + 'file exists!' + color.end)
                replace_prompt = input(color.prompt + "type 'y' to replace file. or any other key to rename. " + color.end)
                if replace_prompt == 'y':
                    os.remove(filename)
            else:
                conflict_check = 'n'
        # get_quantity(qfile) is the list containing all of the datatypes
        for i in get_quantity(qfile):
            x = search_data(i, inputfile, exact_to_db[0], smvalue)
            add_data(x[0], filename, smvalue)
            if silent_mode == False:
                pass  # can add debugging info here
        print('the file "' + filename + '.txt" was created containing the data.')
        return None, filename, exact_to_db[0], x[1]
    except:
        # the file is empty as the program could not
        # find any data. the created file is removed from local directory where it was created
        #  as it will be empty and will be costing resources. when removing it must have
        # '.txt' at its end, as added below. since filename is earlier changed to
        #  filename.txt in add_data function.
        # os.remove(filename + '.txt')    DO NOT NEED NO MO BUT LATER ASK USER IF THEY WANT TO KEEP THE (ACTUALLY POPULATED WITH DATA) FILE

        # SEARCHTEST BECOMES OBSOLETE SO PUT THE ERROR MESSAGE HERE
        print(color.error + '\nError: The search returned empty list; no entries found.' + '\n' +
              'Check that country name/code is entered as exactly in ' + '\n' +
              'file (e.g. Capital letters), or check file format is correct.\n' + color.end)

        retry = input(
            "cannot plot data:\n"
            "(data from last iteration is missing or incomplete, no file/graph will be created.)\n"
            + color.prompt + "retry? ('y' to retry, or enter any other key to exit) " + color.end)
        print(color.prompt + "\n\n.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:._.:*~*:_.:*~*:." + color.end, end=' ')
        # in this exception codeblock, multi_file will return a tuple replacing filename
        # and country to None, because the master function will not use the empty data
        return retry, None, None


# line counting starts at 0, adding 1 to make reader friendly
# function 'Add Data' will create an output file and add data from an input list to the file.
def add_data(data, filename, silent_mode=False):
    if data != []:
        filename = filename + '.txt'
        with open(filename, 'a') as f:
            for x in range(len(data)):
                f.write(data[x] + '/')
            f.write('\n')
            f.close()
            if silent_mode == False:
                print('     data is added to output file "' + filename + '". \n')
                # print(data) for debugging
    else:
        pass


def show_country_opts(dbfile, qfile):
    with open(dbfile, 'r') as f:
        # to ignore the first line
        f.readline()

        for x in range(file_len(dbfile)):
            a = f.readline()
            a = a.split('/')
            # get_quantity(qfile)[0] takes some quantity of arbitrary index
            # datatype from the quantities file and gets every
            # country name and code for that datatype
            # fixing to nth index prevents repeating same countries being re-printed.
            if get_quantity(qfile)[0] in a:
                print(a[1], '(', a[2], ')')


# 'Search Data'. When, called the function will search data for a given country
# (string) and datatype (string). Returns the data into a list.
def search_data(datatype, DOF, countryname, silent_mode=False):
    f = open(DOF, 'r')
    len_of_file = file_len(DOF)
    if silent_mode == False:
        print('searching ' + str(len_of_file) + ' entries from file "' + DOF + '"')
    list_of_values = []
    file = f.readlines()
    for i in file:
        if datatype in i and countryname in i:
            a = i.strip('\n')
            a = a.split('/')
            # name_and_code only meaningfully needs to be defined if the datatype
            # and countryname (or country code) are found in the search, so it is
            # defined when the above condition is true
            name_and_code = (a[1], a[2])
            for n in a:
                list_of_values.append(n)
    if list_of_values == []:
        # other functions later called, such as add_data will expect the return
        # value from search_data to be of the same format as if it were a
        # successful search, so like in the elif condition below, this
        # condition returns a tuple. because name_and_code are not needed,
        # None will take its place when the search was unsuccessful.
        return list_of_values, None
    elif list_of_values != []:
        if silent_mode == False:
            print('   Match for datatype "' + datatype + '" found.')
        return list_of_values, name_and_code
    f.close()


# 'Get Quantity' gets the table of quantities from a
# file and stores the into a list.
def get_quantity(DOF):
    f = open(DOF, 'r')
    num_of_quants = file_len(DOF)
    a = f.readlines()
    # print(a) #for debugging
    q_list = []
    for n in a:
        n = n.strip('\n')
        q_list.append(n)
    f.close()
    del q_list[-1]  # delete excess '' element in list.
    # print(q_list) #for debugging
    return q_list


# format to float will take a list of data
# as strings and change each element into
# a float. it then returns a list of the
# same data as a float in the same order
def format_to_float(y_list):
    y_float = []
    for n in y_list:
        # print(y_list)
        # print(type(n))

        # if the for loop encounters
        # a string that cannot be converted to a number
        # (i.e text) it will skip an iteration and move onto the next.
        # (this may not be strictly allowed use of try/except)
        try:
            if n == '..':
                y = 0
            else:
                y = float(n)
            y_float.append(y)
        except:
            continue
    return y_float


# setsilentmode converts the user entered list into a boolean depending on the string character,
# functions will use this boolean as a condition on whether to print process information to console or not.
def set_silent_mode(mode):
    if mode == 'y':
        print('running in silent mode')
        return True
    elif mode == 'n':
        print('running in silent mode off; all processes will print to screen.')
        return False
    else:
        print(color.error + 'invalid input, running in default mode (silent mode off)' + color.end)
        return False


# 'filelen' will get length of file by line.
# returns the length of the file.
def file_len(filename):
    with open(filename) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


# start_info will print useful information to the screen upon startup
# of each iteration of the program. information here will be useful
# to the user on how to use the program.
def start_info():
    print(color.info + 'user guide --\n\n'

                       'shortcuts -\n' + color.end +
          "when prompted to input at any time, type " + color.prompt + '.quit' + color.end +
          " to exit the\nprogram and go directly to the option to show the graph\n"
          "(this option is not available when asked whether to keep/delete files.).\n"
          "any previously created file in that iteration (shown by page number) will automatically be kept."
          "\nwhen prompted to enter the country name/code, type "
          + color.prompt + "'.opt'" + color.end + " to see availabe options\nfrom database."
                                                  '\n\n'

          + color.info + 'silent mode  -\n' + color.end +
          'silent mode is a debugging feature that allows the user to choose whether they want to see\n'
          'all processes on screen. ' + "type 'y' to set silent mode On (don't print to screen),\n"
                                        "and 'n' to set silent mode Off (print to screen). silent mode 'Off' (n) is recommended to\nsee all running processes.\n\n"

          + color.info + "file creation -\n" + color.end + "throughout each run of the code, and until the user exits the code, the user may create\n"
                                                           "files containing all data for an entered country. if the search was unable to find data for an\n"
                                                           "entered country name or country code, it may likely be a miskey, or the name/code is not exact\nto the database file."
                                                           " the program will not create files for failed searches and will allow\nthe user to retry the search.\n\n"
                                                           ""
          + color.info + "integrated plotting -\n" + color.end +
          "for each run, the option to plot chosen data of the entered country to a graph will be given.\nif the data search returns"
          " empty, the search found no matches for the country given\nand the progam will not plot any data. no match implies "
          "the country name or code has been\nmiskeyed and is not exact to the database file. the program will allow\n"
          "the user to try again, or .quit to exit the program. after all iterations,\noption to show the graph is"
          " after exiting the program.\n ")

def create_qfile(database, filename):
    with open(database,'r') as f:
        file = f.readlines()
        qdata = []
        for line in file:
            if '$^-' and '-^$' in line:
                continue
            else:
                a = line.strip('\n')
                a = a.split('/')
                qdata.append(a[0])
    f.close()
    result = list(set(qdata))
    if os.path.isfile(filename):
        os.remove(filename)
    with open(filename,'a') as fw:
        for i in result:
            fw.write(i + '\n')
    fw.close()
    return result

# the header title for the program,
# reads 'BESSIE'.
def bessie():
    print('\n')
    print(" * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n\n    Multigraph 2.1.1   freedomfighter (ff), Milli group (c).    \n                                 2017-2018                   \n                         Written in Python 3.6 by            \n                             Takudzwa Makoni                 \n\n     GitHub: https://github.com/Millisoft/freedomfighter     \n\n                 use ’.quit’ to exit the program             \n\n * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * \n" )
    print('\n')
    subprocess.Popen(['afplay','-v', '0.075','trinkets/login.wav']) #run process in terminal (for terminal application) - is powerful.
# this codeblock is needed to add color to some text in the console to differentiate
# types of text such as prompts, errors and processed information.
class color:
    prompt = '\033[0;94m'
    error = '\033[1;91m'
    info = '\033[0;1m'
    end = '\033[0m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[1;36m'
    BLUE = '\033[1;94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[1;93m'
    RED = '\033[1;91m'


###################################### for Part 2 ######################################################################

def convert_to_real_GDP(data, inflation):
    j = 15
    real = []
    while j > -1:
        i = j
        d = (1 + inflation[i] / 100)
        while i > 0:
            d = d * (1 + inflation[i - 1] / 100)
            i = i - 1
        normalised_per_capita = data[j] / d
        real.append(normalised_per_capita)
        j = j - 1
    real.reverse()
    return real


def real_GDPPC(country, database, colour='b', askplot=False, keepfile=False):
    qfile = 'TableOfQuantities.txt'
    datafile = country + ' data'
    GDP = get_quantity(qfile)[1]
    TP = get_quantity(qfile)[0]
    inf = get_quantity(qfile)[10]
    xvalues = format_to_float(
        search_data('Series Name', database, 'Country Name', True)[0]
    )

    for i in get_quantity(qfile):
        x = search_data(i, database, country, True)
        add_data(x[0], datafile, True)

    datafile = datafile + '.txt'

    name_and_code = search_data(GDP, datafile, country, True)[1]

    GDPf = format_to_float(
        search_data(GDP, datafile, country, True)[0]
    )

    populationf = format_to_float(
        search_data(TP, datafile, country, True)[0]
    )

    GDPPC = []

    # performing loop over two lists, which are always
    # the same length
    i = 0
    while i < len(xvalues):
        normalised_GDP = GDPf[i] / populationf[i]
        GDPPC.append(normalised_GDP)
        i = i + 1

    inflationf = format_to_float(
        search_data(inf, datafile, country, True)[0]
    )
    rGDPPC = convert_to_real_GDP(GDPPC, inflationf)
    if askplot == True:
        plot(xvalues, rGDPPC, colour, label='Real GDP per Capita (US$)' + '  "' + name_and_code[1] + '".')
    if keepfile == False:
        os.remove(datafile)
    return rGDPPC


def GDP_per_C(country, database, colour='r', askplot=False, keepfile=False):
    qfile = 'TableOfQuantities.txt'
    datafile = country + ' data'
    GDP = get_quantity(qfile)[1]
    TP = get_quantity(qfile)[0]
    xvalues = format_to_float(
        search_data('Series Name', database, 'Country Name', True)[0]
    )

    for i in get_quantity(qfile):
        x = search_data(i, database, country, True)
        add_data(x[0], datafile, True)

    datafile = datafile + '.txt'

    name_and_code = search_data(GDP, datafile, country, True)[1]

    GDPf = format_to_float(
        search_data(GDP, datafile, country, True)[0]
    )

    populationf = format_to_float(
        search_data(TP, datafile, country, True)[0]
    )

    GDPPC = []

    # performing loop over two lists, which are always
    # the same length
    i = 0
    while i < len(xvalues):
        normalised_GDP = GDPf[i] / populationf[i]
        GDPPC.append(normalised_GDP)
        i = i + 1
    if askplot == True:
        plot(xvalues, GDPPC, colour,
             label='GDP per Capita (US$)' + '  "' + name_and_code[1] + '".')
    if keepfile == False:
        os.remove(datafile)
    return GDPPC


######################## for Part 3 ###############################



def add_data3(data, filename, silent_mode=False):
    if data != []:
        filename = filename + '.txt'
        with open(filename, 'w') as f:
            for x in range(len(data)):
                f.write(data[x])
            f.write('\n')
            f.close()
            if silent_mode == False:
                print('     data is added to output file "' + filename + '". \n')
                # print(data) for debugging
    else:
        pass


def getdatalist(datatype, database):
    GDPPC = open(database, 'r')
    li = []
    for x in GDPPC:
        if x[0: 28] != datatype:
            continue
        else:
            li.append(x)
    return li


def get2015data(filename):
    with open(filename + '.txt', 'r') as f:
        x = f.readlines()
        f.close()
        listfor2015 = []
        for i in x:
            a = i.rstrip('\n')
            a = a.rstrip('/')
            a = a.split('/')
            listfor2015.append(a[-1])
    return listfor2015


def gettop20(listofgdp):
    top_20 = []
    count = 0
    while count < 20:
        top_20.append(
            str(listofgdp[count])
        )
        count = count + 1
    return top_20


def gettopcountrynames(datafor20, database):
    q = 0
    country_list = []
    while q < 20:
        v = search_data('GDP per capita (current US$)', database, datafor20[q], True)[0][3]
        country_list.append(v)
        q = q + 1
    return country_list


def plotfor20(countries, database):
    for p in countries:
        k = format_to_float(search_data('CO2 emissions (metric tons per capita)', database, p, True)[0])
        del k[-1]
        b = list(range(2000, 2015))
        y = []
        for x in k:
            z = (x / k[0]) * 100
            y.append(z)
        plot(b, y, label='CO2 emissions % 0f 2000  ' + p)
