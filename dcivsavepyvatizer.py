#!/usr/bin/env python

import argparse
from os.path import splitext
from sys import exit

### "config" kind of...?
# the extension of Civ5 save files
extension = 'Civ5Save'

### the patterns we're looking for
# We want to find this twice, and replace [7] (0x01) with 0x03
pattern1 = bytes.fromhex('000000030000000100000040')
# We want to find this once, then switch the byte three bytes back from this
# position from 0x00 -> 0x01.
# NOTE: this seems to be the only one needed sometimes. ??
pattern2 = bytes.fromhex('ffffffff00000040')

### let us go...!

# for parsing the command line arguments
parser = argparse.ArgumentParser()

# set up the parser
parser.add_argument('inputfile', help='input save file')
parser.add_argument('--outputfile', '-o', help='output save file')

# parse the command line arguments
args = parser.parse_args()

# the name of the input file
inputfile = args.inputfile

# use the output filename as given if given on the command line
if args.outputfile:
    outputfile = args.outputfile
else:
    # strip the file extension (final part) and add the extension
    outputfile = splitext(args.inputfile)[0] + '_priv.' + extension


# read the file into memory
with open(inputfile, 'rb') as f:
    # read the entire save file into memory
    data = bytearray(source=f.read())

# check to make sure it matches what we're expecting
if data.count(pattern2) != 1:
    # if it doesn't, then quit
    print("This file doesn't look like what I was expecting.")
    print("I give up.")
    exit()

# find the pattern in the data
pattern2_location = data.find(pattern2)

if pattern2_location < 3:
    print("Matched pattern way too close to beginning of file...")
    print("I give up.")
    exit()

# make the replacement
data[pattern2_location - 3] = 1

with open(outputfile, 'wb') as f:
    # write the data out to a new file
    f.write(data)
