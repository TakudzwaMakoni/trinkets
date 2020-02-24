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

cursor-position-utility-y(){
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
	col=$((${pos[1]} - 1))

	echo "$row,$col"
}

cursor-position-utility-y(){
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
	col=$((${pos[1]} - 1))

	echo "$row"
}

cursor-position-utility-x(){
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
	col=$((${pos[1]} - 1))

	echo "$col"
}

navigate-dir(){
cursor_pos_y=$(cursor-position-utility-y)
${HOME}/.trinkets/exec/NavigateDir $cursor_pos_y
file="/tmp/navigationDirectory.txt"
path=$(cat "$file")
cd $path
}
