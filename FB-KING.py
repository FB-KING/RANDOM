import os, platform
 
try:
 
        import requests
  print('\033[1;32m[•] Congrats! Your Device Support This Tools \033[1;37m')
 
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
        
