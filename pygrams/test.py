
import subprocess

proc = subprocess.Popen("./test",
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE)


#inputmessage = input("Message to CPP>> ").encode()
    

proc.stdin.write( b'test' )



