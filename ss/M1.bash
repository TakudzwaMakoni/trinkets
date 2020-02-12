#!/bin/bash

create(){
if [ $# -eq 1 ]; then
if [  -d "$1"  ]; then
echo "${bold}$1${normal} already exists.";
elif [  -f "$1"  ]; then
echo "${bold}$1${normal} already exists.";
else
if [[ $1 == *"."* ]]; then
touch "$1"
echo "${bold}$1${normal} saved as file in working directory."
else
mkdir "$1"
echo "${bold}$1${normal} saved as directory in working directory."
fi

fi

elif [ $# -eq 2 ]; then
if [[ $1 == *"-f"* ]]; then
if [  -d "$2"  ]; then
echo "${bold}$2${normal} already exists.";
elif [  -f "$2"  ]; then
echo "${bold}$2${normal} already exists.";
else
touch "$2"
echo "${bold}$2${normal} saved as extensionless file in working directory."
fi

elif [[ $1 == *"-o"* ]]; then
if [  -d "$2"  ]; then
echo "${bold}$2${normal} already exists.";
cd "$2";
elif [  -f "$2"  ]; then
echo "${bold}$2${normal} already exists.";
open "$2";
else
if [[ $2 == *"."* ]]; then
touch "$2"
open "$2"
echo "${bold}$2${normal} saved as file in working directory."
echo "opened file ${bold}$2${normal}"
else
mkdir "$2"
cd "$2"
echo "${bold}$2${normal} saved as directory in working directory."
echo "in new directory ${bold}$2${normal}"
fi

fi
fi

elif [ $# -eq 3 ]; then
if [[ ( $1 == *"-f"*  &&  $2 == *"-o"* ) || ( $1 == *"-o"*  &&  $2 == *"-f"*  ) ]]; then
if [  -d "$3"  ]; then
echo "${bold}$3${normal} already exists.";
cd "$3";
elif [  -f "$3"  ]; then
echo "${bold}$3${normal} already exists.";
open "$3";
else
touch "$3"
emacs "$3"
echo "${bold}$3${normal} saved as extensionless file in working directory."
echo "opened file ${bold}$3${normal}"
fi
fi
fi
}

sb(){
cd ~/sandbox;
}

setsc(){

    sortalg="radixsort.py"
    I="$HOME/.trinkets/.shortcuts"
    O="$HOME/.trinkets/.shortcutsx"

    if [ "$2" "==" "" ]; then
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

remsc(){
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

sc(){
cd $( grep ";$1:" ~/.trinkets/.shortcuts | cut -d":" -f 2 | sed "s#;##" );
}

listsc(){
  listalg="listsc.py"
    pysc $listalg ~/.trinkets/.shortcuts;
}
