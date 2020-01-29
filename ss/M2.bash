#!/bin/bash

bndcmp(){
    DEF=$( grep "~bndcmp:" ~/.trinkets/.defaults | cut -d":" -f 2 )
    if [ "$#" "==" 1 ]; then
        mpv "https://$DEF.bandcamp.com/album/$1";
    else
	mpv "https://$1.bandcamp.com/album/$2";
    fi
}

bcplay(){
    DEF=$( grep "~bndcmp:" ~/.trinkets/.defaults | cut -d":" -f 2 )
    if [ "$#" "==" 1 ]; then
        mpv "https://$DEF.bandcamp.com/track/$1";
    else
        mpv "https://$1.bandcamp.com/track/$2";
    fi
}

pg(){
    if [ -f "${HOME}/.trinkets/pygrams/$1/.about" ]; then

	aboutfile="${HOME}/.trinkets/pygrams/$1/.about"
	title=$(cut -d"," -f 1 "$aboutfile")
	version=$(cut -d"," -f 2 "$aboutfile")
	repo=$(cut -d"," -f 3 "$aboutfile")
	company=$(cut -d"," -f 4 "$aboutfile")
	year=$(cut -d"," -f 5 "$aboutfile")
	language=$(cut -d"," -f 6 "$aboutfile")
	author=$(cut -d"," -f 7 "$aboutfile")
	git=$(cut -d"," -f 8 "$aboutfile")
	${HOME}/.trinkets/exec/gws "$title" "$version" "$repo" "$company" "$year" "$language" "$author" "$git"
    fi
    python3 "${HOME}/.trinkets/pygrams/$1/main.py";
}

pysc(){
    set --  "${HOME}/.trinkets/ps/$1" "${@:2}"
    python3 "$@"

}

echo "${bold}M2${normal}  successfully imported."
