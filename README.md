# pyAkalabeth
Python port of the Apple II game Akalabeth by Richard Garriott (1979)

This is my Python3 port of Akalabeth, based on the code presented by https://github.com/videogamepreservation/akalabeth.
It all started as a line-by-line port from Applesoft BASIC to Python3, but I got tired of that pretty quickly and implemented an Applesoft abstraction layer. This made for a simple line-by-line port, but I'm an amateur with Python, so don't expect great code.

Requires PyGame Python library.

To run:  
_start.py_ to show the splash screen and instructions. Once the instructions are done the game will automatically launch.  
_Akalabeth.py_ to skip the instructions and launch the game immediately.

Notes:  
AKALABETH.TXT is the original source of the game: https://github.com/videogamepreservation/akalabeth.  
INSTRUCTIONS.TXT is the original source of the instructions.  
The Apple II font file PrintChar21.tff: https://www.kreativekorp.com/software/fonts/apple2/.  
MicroM8 Apple II emulator was useful for examining disk images and printing out code: https://paleotronic.com/software/microm8/.  
jtauber's Apple disk image reader and BASIC detokenizer: https://github.com/jtauber/a2disk.  
