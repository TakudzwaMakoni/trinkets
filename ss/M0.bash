#!/bin/bash

pr(){ . ~/.bashrc; }

inv(){
printf "\e[?5h"
}

rev(){
printf "\e[?5l"
}

fndr(){
if [ -d "$1" ]; then
open "$1";
elif [ "$1" "==" ""  ]; then
open "$PWD";
else
echo "${bold}$1${normal} is not a directory"
fi
}
