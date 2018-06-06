#! python3
#Launches the map in your browser using the address in command lineor clipboard

import sys,webbrowser
import pyperclip

if(len(sys.argv) > 1):
	#get address from command line
	address=' '.join(sys.argv[1:])
else:
	#from clipboard
	address=pyperclip.paste()

webbrowser.open("https://www.google.com/maps/place/"+address)



