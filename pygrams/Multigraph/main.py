
import Multigraph as db, os #gets all functions from the function module as database 'db'
from matplotlib import pyplot as plt
db.bessie()
# the database file is declared here to be later used by SD function called in multifile.
# it is not expected to change so it is not a user input
economicdata = 'WB_DATA_PSS.txt'
economicheaders = db.create_qfile(economicdata,'quantities.txt')
def main():
    db.master(economicdata,'quantities.txt')
    show_condition = input(db.color.end +
    'exited program. ' + db.color.prompt + 'show graph? (y/n) ' + db.color.prompt + db.color.end)
    if show_condition == 'y':
        plt.xlabel('Year')  # add label to x-axis
        plt.legend(loc = 'upper left')  # add legend to graph
        # will show the graph
        plt.show()
        os.remove('quantities.txt')
main()

