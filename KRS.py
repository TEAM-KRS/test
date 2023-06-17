import os

os.system('xdg-open https://www.facebook.com/groups/207678473842318/')
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

