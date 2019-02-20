#!/usr/bin/bash

tput cols;
tput lines;
numchar(){
    wc -m "$1" | awk '{printf $1}';
}
