import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://github.com/FB-KING')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from a import main
 
        main()
 
 
 
elif bit == "32bit":
 
        from a import main
 
 
        main()
        
