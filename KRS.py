import os
os.system('git pull')

os.system('xdg-open https://www.facebook.com/100088555784538/posts/250941354534389/?substory_index=1245755729301381&app=fbl/')
import os, platform, time, sys

try:

    import requests

except:

    os.system('pip install requests')

os.system('git pull --quiet 2>/dev/null')

bit = platform.architecture()[0]

if bit == '64bit':

    

    import KRS64

    

elif bit == '32bit':

    

    import KRS32

