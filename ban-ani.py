import sys, time
#Banner Animation
def banner():
    name = '''\x1b[1;33m
 ____                                   _          _           
| __ )  __ _ _ __  _ __   ___ _ __     / \   _ __ (_)_ __ ___  
|  _ \ / _` | '_ \| '_ \ / _ \ '__|   / _ \ | '_ \| | '_ ` _ \ 
| |_) | (_| | | | | | | |  __/ |     / ___ \| | | | | | | | | |
|____/ \__,_|_| |_|_| |_|\___|_|    /_/   \_\_| |_|_|_| |_| |_|
 \n'''
    credit = "\n\x1b[1;36m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;36m\xe2\x95\x91 \t\x1b[1;37mAuthor   \x1b[1;37m: \x1b[1;32mmr-rat\x1b[1;36m                   \t\t\xe2\x95\x91\n\x1b[1;36m\xe2\x95\x91 \t\x1b[1;37mgithub   \x1b[1;37m: \x1b[1;32mhttps://github.con/mr-rat\x1b[1;36m\t\t\xe2\x95\x91\n\x1b[1;36m\xe2\x95\x91 \t\x1b[1;37mFacebook \x1b[1;37m: \x1b[1;32mhttps://www.facebook.com/mr.bule.rat\x1b[1;36m \xe2\x95\x91\n\x1b[1;36m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\t                 \x1b[1;36m[\x1b[1;32mTool Name\x1b[00m\x1b[1;36m]\n"
    i = (name+credit)
    for x in i + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(1.0 / 1000)
banner()
