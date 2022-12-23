import board
import busio
import sdcardio
import storage
import sys
import os

spi = busio.SPI(board.GP2, board.GP3, board.GP4)
cs = board.GP5

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)# Write your code here :-)

storage.mount(vfs, "/sd")
sys.path.append("/sd")

def print_directory(path, tabs=0):
    for file in os.listdir(path):
        stats = os.stat(path + "/" + file)
        filesize = stats[6]
        isdir = stats[0] & 0x4000

        if filesize < 1000:
            sizestr = str(filesize) + " by"
        elif filesize < 1000000:
            sizestr = "%0.1f KB" % (filesize / 1000)
        else:
            sizestr = "%0.1f MB" % (filesize / 1000000)

        prettyprintname = ""
        for _ in range(tabs):
            prettyprintname += "   "
        prettyprintname += file
        if isdir:
            prettyprintname += "/"
        print('{0:<40} Size: {1:>10}'.format(prettyprintname, sizestr))

        # recursively print directory contents
        if isdir:
            print_directory(path + "/" + file, tabs + 1)

print("Files on filesystem:")
print("====================")

print_directory("/sd")

import hellodave

#with open("/sd/hellodave.py", "w") as f:
#    f.write("print('Hello big davey boy')")

