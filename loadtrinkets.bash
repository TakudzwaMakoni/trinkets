#!/bin/bash

test -e "${HOME}/.trinkets/ss/M0.bash" &&
# display label if exists
{
. "${HOME}/.trinkets/ss/M0.bash";
if [ -f ${HOME}/.trinkets/exec/gws ] && [ -f ${HOME}/.trinkets/.about  ]
then
	clear && aboutTrinkets
fi
}

test -e "${HOME}/.trinkets/ss/M1.bash" && . "${HOME}/.trinkets/ss/M1.bash"
test -e "${HOME}/.trinkets/ss/M2.bash" && . "${HOME}/.trinkets/ss/M2.bash"
