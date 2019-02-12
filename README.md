#trinkets

prerequisites:

- youtube-dl

- shell integration with (imgcat)

- mplayer

- iTerm2 is the recommended Terminal Application


Installation --> copy the 'to_bashrc.sh' and 'to_bash_profile.sh' files to their respective /usr/.bashrc and /usr/.bash_profile files.


compiled scripts and tools for customising terminal window

with modifications to :

apples by David Miller --> https://github.com/davidfmiller
youtube-dl --> https://github.com/rg3/youtube-dl/

commands for iTerm2:

- prof [PROFILE] # change the profile in the current window for iTerm2
- terminal-profile [PROFILE] # change the profile in the current window for Terminal app. (MacOS)

- inv # inverts the profile colours

- rev # reverts the profile colours

- img [PATH/TO/IMAGE] # is an alias for imgcat. shows the image of the first argument in terminal. Compatible with iTerm2. Is installed by line 8 in 'to_bashrc'

- start [OPTION] [OPTION] [FILE/DIRECTORY] 

#- Can take 1 to 3 arguments.  with options -o for open and -f for extensionless file.

#^ With one argument, E.G. "start example.txt" as the file or directory, the command  will create a file if the string passed contains a dot file extension, and a directory if without. 

#^ With two argments such as "start -o examplefile.txt", the command creates and opens the text file.
#^ With two argments such as "start -o exampledir", the command creates and enters the directory in terminal.

#^ With two argments such as "start -f examplefile", the command creates the extensionless text file.
#^ NOTE With two argments such as "start -f examplefile.txt", the command will create the file with the extension.

#^ With three argments such as "start -f -o examplefile" or "start -o -f examplefile", the command creates and opens the extensionless text file.

ytsave [SAVE AS] [YOUTUBE URL] #modification of youtube-dl, save youtube file to directory.

ytsave [SAVE AS] [YOUTUBE URL] #modification of youtube-dl, save youtube file to directory, and play play the video. (requires mplayer)

vplay [PATH/TO/VIDEO]

 
