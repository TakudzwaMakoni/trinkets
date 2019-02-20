#!/bin/bash

bndcmp(){
    DEF=$( grep "~bndcmp:" ~/.trinkets/.defaults | cut -d":" -f 2 )
    if [ "$#" == 1 ]; then
        mpv "https://$DEF.bandcamp.com/album/$1";
    else
	mpv "https://$1.bandcamp.com/album/$2";
    fi
}

bcplay(){
    DEF=$( grep "~bndcmp:" ~/.trinkets/.defaults | cut -d":" -f 2 )
    if [ "$#" == 1 ]; then
        mpv "https://$DEF.bandcamp.com/track/$1";
    else
        mpv "https://$1.bandcamp.com/track/$2";
    fi
}

pg(){
    python3 "${HOME}/.trinkets/pygrams/$1/main.py";
}
