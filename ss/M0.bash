#!/bin/bash

about(){
if [ -f $1 ]
then

	title=$(cut -d"," -f 1 "$1")
	version=$(cut -d"," -f 2 "$1")
	repo=$(cut -d"," -f 3 "$1")
	company=$(cut -d"," -f 4 "$1")
	year=$(cut -d"," -f 5 "$1")
	language=$(cut -d"," -f 6 "$1")
	author=$(cut -d"," -f 7 "$1")
	git=$(cut -d"," -f 8 "$1")
	${HOME}/.trinkets/exec/gws "$title" "$version" "$repo" "$company" "$year" "$language" "$author" "$git"
fi
}

aboutTrinkets(){
	about "${HOME}/.trinkets/.about"
}

create(){
if [ $# -eq 1 ]; then
if [  -d "$1"  ]; then
echo "${bold}$1${normal} already exists.";
elif [  -f "$1"  ]; then
echo "${bold}$1${normal} already exists.";
else
if [[ $1 == *"."* ]]; then
touch "$1"
echo "${bold}$1${normal} saved as file in working directory."
else
mkdir "$1"
echo "${bold}$1${normal} saved as directory in working directory."
fi

fi

elif [ $# -eq 2 ]; then
if [[ $1 == *"-f"* ]]; then
if [  -d "$2"  ]; then
echo "${bold}$2${normal} already exists.";
elif [  -f "$2"  ]; then
echo "${bold}$2${normal} already exists.";
else
touch "$2"
echo "${bold}$2${normal} saved as extensionless file in working directory."
fi

elif [[ $1 == *"-o"* ]]; then
if [  -d "$2"  ]; then
echo "${bold}$2${normal} already exists.";
cd "$2";
elif [  -f "$2"  ]; then
echo "${bold}$2${normal} already exists.";
open "$2";
else
if [[ $2 == *"."* ]]; then
touch "$2"
open "$2"
echo "${bold}$2${normal} saved as file in working directory."
echo "opened file ${bold}$2${normal}"
else
mkdir "$2"
cd "$2"
echo "${bold}$2${normal} saved as directory in working directory."
echo "in new directory ${bold}$2${normal}"
fi

fi
fi

elif [ $# -eq 3 ]; then
if [[ ( $1 == *"-f"*  &&  $2 == *"-o"* ) || ( $1 == *"-o"*  &&  $2 == *"-f"*  ) ]]; then
if [  -d "$3"  ]; then
echo "${bold}$3${normal} already exists.";
cd "$3";
elif [  -f "$3"  ]; then
echo "${bold}$3${normal} already exists.";
open "$3";
else
touch "$3"
emacs "$3"
echo "${bold}$3${normal} saved as extensionless file in working directory."
echo "opened file ${bold}$3${normal}"
fi
fi
fi
}

invert-screen(){
printf "\e[?5h"
}

list-children(){
	OPTIND=1 # Reset in case getopts has been used previously in the shell.
	showHidden="False"
	while getopts a opt; do
	  case $opt in
	    a) showHidden="True"
			;;
			*) return
			;;
	  esac
		shift
	done
	listalg="list.py"
	DIR=${1:-${PWD}}
	if [ -d $DIR ]
	then
	pysc "$listalg" "$showHidden" "$DIR"
	else
		echo "$DIR is not a directory"
	fi
}

reload-shell(){
# reset && . ~/.bashrc; 
exec bash
}

refresh-shell(){
if [ "$1" == "--hard" ] || [ "$1" == "-h"  ]
then
	# reset terminal and load trinkets startpage
	reset && aboutTrinkets
else
	clear && aboutTrinkets
fi
}

revert-screen(){
printf "\e[?5l"
}
