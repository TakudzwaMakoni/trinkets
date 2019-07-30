#include <iostream>
#include <sys/ioctl.h>
#include <stdio.h>
#include <cstdlib>
#include <unistd.h>
#include <string>
#include <iomanip>
#include <stdlib.h>
#define arraysize(ar)  (sizeof(ar) / sizeof(ar[0]))

using namespace std;

void eol(int v=1){ // print end of line to terminal
    for (int i=0; i<v; i++){
        cout << endl;
    }
}
void pf(string str, int winwidth){ // print formatted
    
    int widthA = ( winwidth + str.length()) / 2; // calc centre of terminal window position
    cout << setw(widthA) << right << str;
}

int gws(){
    
    struct winsize w;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
    int siz [2] = {w.ws_row, w.ws_col};
    return siz[1];
    
}

int main(int argc, char* argv)
{
    
    string spc = " "; // space string for easier reading.
    string marginline = "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"; // border
    string title = argv[1] + spc;
    string version = argv[2] + spc;
    string repo = argv[3] + spc;
    string company = argv[4] + spc;
    string year = argv[5] + spc;
    string langauge = argv[6] +spc;
    string author = argv[7] + spc;
    string git = argv[8] + spc;
    string login = "afplay -v 0.075 ~/.trinkets/sounds/login.wav";
    /* string cmdlist = "osascript ~/trinkets/as/ocean.scpt;osascript ~/trinkets/as/redsands.scpt;osascript ~/trinkets/as/grass.scpt;osascript ~/trinkets/as/novel.scpt;osascript ~/trinkets/as/ocean.scpt;osascript ~/trinkets/as/redsands.scpt;osascript ~/trinkets/as/grass.scpt;osascript ~/trinkets/as/novel.scpt;osascript ~/trinkets/as/makoni.scpt;"; */
    
    // should redirect osacripts paths to OSX terminal directory.
    
    int w = gws(); // window
    int* wptr = &w; // pointer to memory address of intger w.
    int& twref = *wptr; // reference assigned to value at memory address w.
    

  
    ////////////////////////////////////
    
    popen(login.c_str(),"r");
    //popen(cmdlist.c_str(),"r"); not for the epileptic...

    
    eol(2); // padding
    pf(marginline, twref); //
    eol(3);
    pf(title + "v" + version + ", " + repo, twref);
    eol();
    pf(company + year + ", " + "written in " + langauge, twref);
    eol(2);
    pf("by " + author, twref);
    eol();
    pf("git: " + git,twref);
    eol(3);
    pf(marginline,twref);
    eol(2); // padding
    
    return 0;  // make sure your main returns int
}
