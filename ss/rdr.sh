tput cols;
tput lines;
wc -m "$1" | awk '{printf $1}';
