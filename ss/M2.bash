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

pg(){
	aboutfile="${HOME}/.trinkets/pygrams/$1/.about"
	about $aboutfile
    	python3 "${HOME}/.trinkets/pygrams/$1/main.py"
}

pysc(){
    set --  "${HOME}/.trinkets/ps/$1" "${@:2}"
    python3 "$@"

}
