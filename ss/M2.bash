#!/bin/bash

pygram(){
if	[ -d "${HOME}/.trinkets/pygrams/$1" ]
then
	aboutfile="${HOME}/.trinkets/pygrams/$1/.about"
	clear
	about $aboutfile
    	python3 "${HOME}/.trinkets/pygrams/$1/main.py"
else
	echo "no such program"
fi
}

pysc(){
    set --  "${HOME}/.trinkets/ps/$1" "${@:2}"
    python3 "$@"
}

cursor-position-y(){
	exec < /dev/tty
	oldstty=$(stty -g)
	stty raw -echo min 0
	# on my system, the following line can be replaced by the line below it
	echo -en "\033[6n" > /dev/tty
	# tput u7 > /dev/tty    # when TERM=xterm (and relatives)
	IFS=';' read -r -d R -a pos
	stty $oldstty
	# change from one-based to zero based so they work with: tput cup $row $col
	row=$((${pos[0]:2} - 1))    # strip off the esc-[

	echo "$row"
}

cursor-position-x(){
	exec < /dev/tty
	oldstty=$(stty -g)
	stty raw -echo min 0
	# on my system, the following line can be replaced by the line below it
	echo -en "\033[6n" > /dev/tty
	# tput u7 > /dev/tty    # when TERM=xterm (and relatives)
	IFS=';' read -r -d R -a pos
	stty $oldstty
	# change from one-based to zero based so they work with: tput cup $row $col
	col=$((${pos[1]} - 1))

	echo "$col"
}

navigate-dir(){

OPTIND=1 # Reset in case getopts has been used previously in the shell.
showHidden="0" # c++ interpretation of 'false'.

while getopts a opt; do
	case $opt in
		a) showHidden="1" # true.
		;;
		*) return
		;;
	esac
	shift
done

DIR=${1:-${PWD}}
if [ -d $DIR ]
then
	${HOME}/.trinkets/exec/NavigateDir $showHidden $DIR
	exitStatus=$?
	if [ $exitStatus != 0 ]
	then
		echo " "
		echo "user exited"
		return 1
	fi
else
	echo "$DIR is not a directory"
	return 1
fi

file="/tmp/navigationDirectory.txt"
path=$(cat "$file")
if [ -d $path ]
then
	cd $path
elif [ -f $path ]
then
	if [[ $EDITOR == "" ]]
	then
		echo "no EDITOR environment variable set"
	else
		if [ -r $path ] && [ -w $path ]
		then
		$EDITOR $path
		else
			sudo $EDITOR $path
		fi
	fi
fi
}
