#!/bin/bash

set-shortcut(){

    sortalg="radixsort.py"
    I="$HOME/.trinkets/.shortcuts"
    O="$HOME/.trinkets/.shortcutsx"

    if [[ "$2" == "" ]]; then
	INDIR=$PWD
    elif [ -d "$2" ]; then
	INDIR=$2
    else
	echo "${bold}$2${normal} is not a directory."
	return 1
    fi

    INSC=$1

    if grep --silent ";$INSC:" ~/.trinkets/.shortcuts && grep -q ":$INDIR;" ~/.trinkets/.shortcuts; then
	PREDIR=$( grep ";$INSC:" ~/.trinkets/.shortcuts | cut -d":" -f 2 | sed "s#;##"; )
	PRESC=$( grep ":$INDIR;" ~/.trinkets/.shortcuts | cut -d":" -f 1 | sed "s#;##"; )

	if [[ "$INDIR" == "$PREDIR" && "$INSC" == "$PRESC" ]] ; then
	    echo "relationship already exists!"
	else
	    echo "conflict:"
	    echo "${bold}$INSC${normal} is already a shortcut for ${bold}$PREDIR${normal} and";
	    echo "${bold}$INDIR${normal} is already pointed to by ${bold}$PRESC${normal}";
	    echo "you need to replace either shortcut or path individually, or remove relations with remsc."
	fi
    elif grep --silent ":$INDIR;" ~/.trinkets/.shortcuts; then
	PRESC=$( grep ":$INDIR;" ~/.trinkets/.shortcuts | cut -d":" -f 1 | sed "s#;##" )
	echo "the directory ${bold}$INDIR${normal} is already pointed to by ${bold}$PRESC${normal}";
	while true; do
	    echo "use new shortcut ${bold}$INSC${normal} to point to this directory? "
	    read yn
	    case $yn in
		[Yy]* ) LINE=$( grep ":$INDIR;" ~/.trinkets/.shortcuts ); sed -i.bak  "s#$LINE#;$INSC:$INDIR;#g" ~/.trinkets/.shortcuts ; pysc "$sortalg" "$I" "$O" 0 ; mv "$O" "$I" ; echo "${bold}$INSC${normal} now points to ${bold}$INDIR${normal}" ;break;;
		[Nn]* ) echo "did nothing."; break;;
		* ) echo "Please answer yes or no.";;
	    esac
	done
    elif grep --silent ";$INSC:" ~/.trinkets/.shortcuts; then
	PREDIR=$( grep ";$INSC:" ~/.trinkets/.shortcuts | cut -d":" -f 2 | sed "s#;##" )
    	echo "the shortcut ${bold}$INSC${normal} already refers to ${bold}$PREDIR${normal}";
    	while true; do
   	    echo "use this shortcut to point to new directory? "
	    echo "y/n? "
	    read yn
       	    case $yn in
            	[Yy]* ) LINE=$( grep ";$INSC:" ~/.trinkets/.shortcuts ); sed -i.bak "s#$LINE#;$INSC:$INDIR;#g" ~/.trinkets/.shortcuts ; pysc "$sortalg" "$I" "$O" 0 ; mv "$O" "$I" ;
			echo "${bold}$INSC${normal} now points to ${bold}$INDIR${normal}" ;break;;
            	[Nn]* ) echo "did nothing."; break;;
            	* ) echo "Please answer yes or no.";;
      	    esac
    	done
    else
	echo ";$INSC:$INDIR;" >> ~/.trinkets/.shortcuts ; pysc "$sortalg" "$I" "$O" 0 ; mv "$O" "$I"
    fi

}

remove-shortcut(){
    I="$HOME/.trinkets/.shortcuts"
    O="$HOME/.trinkets/.shortcutsx"
    INSC=$1
    PREDIR=$( grep ";$INSC:" ~/.trinkets/.shortcuts | cut -d":" -f 2 | sed "s#;##" )
    echo "are you sure you want to remove the relationship:"
    echo "${bold}$INSC${normal} -> ${bold}$PREDIR${normal}"
    echo "y/n? "
    while true; do
            read yn;
            case $yn in
                [Yy]* ) LINE=$( grep ";$INSC:" ~/.trinkets/.shortcuts ); sed -i.bck "s#$LINE##g" ~/.trinkets/.shortcuts ;
			awk '!NF {f=0; next} f {print ""; f=0} 1' ~/.trinkets/.shortcuts > "$O";mv "$O" "$I";
			echo "relationship removed.";break;;
                [Nn]* ) echo "did nothing."; break;;
                * ) echo "Please answer yes or no.";;
            esac
        done
}

shortcut(){
cd $( grep ";$1:" ~/.trinkets/.shortcuts | cut -d":" -f 2 | sed "s#;##" );
}

list-shortcuts(){
  listalg="listsc.py"
    pysc $listalg ~/.trinkets/.shortcuts;
}
