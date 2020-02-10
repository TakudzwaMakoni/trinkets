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
       cout << "\n";
    }
}
void pf(string str, int winwidth){ // print formatted
    
    int widthA = ( winwidth + str.length()) / 2; // calc centre of terminal window position
    cout << setw(widthA) << right << str;
}

int getWinSize(){
    
    struct winsize w;
    ioctl(STDOUT_FILENO, TIOCGWINSZ, &w);
    int siz [2] = {w.ws_row, w.ws_col};
    return siz[1];
    
}

int main(int argc, char** argv)
{
    
    string spc = " "; // space string for easier reading.
    string marginline = "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *"; // border
   
    string title;
    string version;
    string repo;
    string company;
    string year;
    string language;
    string author;
    string git;

    if(argc>1){
    title = argv[1] + spc;
    version = argv[2] + spc;
    repo = argv[3] + spc;
    company = argv[4] + spc;
    year = argv[5] + spc;
    language = argv[6] +spc;
    author = argv[7] + spc;
    git = argv[8] + spc;
    }
    
    int w = getWinSize(); // window
    
    pf(marginline, w); //
    eol(2);
    pf(title + "v" + version + ", " + repo, w);
    eol();
    pf(company + year + ", " + "written in " + language, w);
    eol(2);
    pf("by " + author, w);
    eol();
    pf("git: " + git, w);
    eol(2);
    pf(marginline, w);
    eol(1); // padding
    
    return 0; 
}
