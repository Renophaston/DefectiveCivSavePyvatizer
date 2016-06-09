#!/usr/bin/env python

import argparse
from os.path import splitext

### "config" kind of...?
# the extension of Civ5 save files
extension = 'Civ5Save'

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


with open(inputfile, 'rb') as f:
    # read the entire save file into memory
    data = f.read()
with open(outputfile, 'wb') as f:
    # write the data out to a new file
    f.write(data)
