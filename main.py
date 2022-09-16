# Automatic OOF sound replacer for Roblox.
# main.py
# 

import requests
import os
import json
import wget

# Get current version of roblox to variable by querying roblox api
winplayersettings = requests.get('https://clientsettings.roblox.com/v2/client-version/WindowsPlayer')
winplayerdict = winplayersettings.json()
currentversion = list(winplayerdict.values())[1]


# Prepare folders/files to preform oof operation
appdata = os.getenv('LOCALAPPDATA')
targetfolder = appdata + '/Roblox/Versions/' + currentversion + '/content/sounds'
goofyahhsound = targetfolder + '/ouch.ogg'

# Remove goofy ahh "duh" sound and replace with the one and only

os.remove(goofyahhsound)
os.chdir(targetfolder)
oofurl = "https://str5.cdn.trolling.solutions/ouch.ogg"
wget.download(oofurl, "ouch.ogg")

# OOF!