# AutoOOF

# THIS SHIT IS FUCKED BECAUSE ROBLOX CHANGED THE WAY THE CLIENT IS INSTALLED AND THIS SCRIPT WAS MADE IN A FEW MINUTES WITHOUT MUCH CONSIDERATION, THIS DOES NOT MEAN I WILL NOT EVER FIX IT, I JUST CANNOT BE BOTHERED RIGHT NOW.

Classic death sound replacer for Roblox Game Client (not affiliated in any way with the Roblox Corporation, obviously.)

Plans to eventually have a revamp with a background service so you don't have to run the script when Roblox updates.

# Usage

"Easy" method / exe version:

1. Click "Releases" on the right side of this screen.
2. Click oof.exe on the most recent listing.
3. Run the file.

Repeat step 3 when roblox updates. (recommended to make a shortcut on your desktop or just put the file there for ease of access)


"Hard" method / standalone python version / "old" instructions:


Install Python 3.8+ and add to PATH, if you haven't already.
Download main.py from releases and run with a terminal when roblox has updated. (Go to the folder where main.py is in cmd/powershell/etc.. and run using `python ./main.py`.

Detailed instructions:
1. Click "Releases" on the right side of this screen.
2. Click main.py on the most recent listing.
3. Go to python.org and click the download button
4. Run the installer, and check the "Add to PATH" checkbox.
5. Right click the file in your browsers downloads section, and press show containing folder.
6. Right click some blank space in the folder and then press "Open in Windows Terminal".
7. Type into the box `python ./main.py`

Repeat steps 6 and 7 when Roblox updates. You can also create a desktop or start menu shortcut to make this easier.

# Troubleshooting:

I don't know what the error is!

Try all steps below, I was tired of having people harass me so I just supressed all errors in the executable. Sorry.

I get a file not found error!

Uninstall "Roblox Player" in Programs and Features and reinstall. This error is caused by running Roblox or the installer as Administrator, which changes the folder path. You can also edit main.py to the correct path (you can repack the executable version if you really want to, but if you are editing the py file anyways you probably understand well enough how to use it standalone).

The sound is still the same!

Restart Roblox.

I get a 403/404 error!

Disconnect from any VPN/Proxy/TOR/etc.. and run again. Check that you can access Roblox `clientsettings` api [here](https://clientsettings.roblox.com/v2/client-version/WindowsPlayer). If that works fine but you are still getting a 403/404 you are probably having an issue with the TriHard.space CDN which is used to host the sound file, check first if you are in an export control restricted or embargoed region (e.g Iran) and if not please contact support on [this page](https://trihard.space).
