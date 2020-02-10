#!/bin/bash

test -e "${HOME}/.trinkets/ss/M0.bash" && . "${HOME}/.trinkets/ss/M0.bash"
test -e "${HOME}/.trinkets/ss/M1.bash" && . "${HOME}/.trinkets/ss/M1.bash"
test -e "${HOME}/.trinkets/ss/M2.bash" && . "${HOME}/.trinkets/ss/M2.bash"

if [ -f ${HOME}/.trinkets/exec/gws ] && [ -f ${HOME}/.trinkets/.about  ]
then
 	about "${HOME}/.trinkets/.about"
fi
