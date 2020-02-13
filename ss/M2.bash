#!/bin/bash

pg(){
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
