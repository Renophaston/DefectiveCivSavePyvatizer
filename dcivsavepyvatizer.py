#!/usr/bin/env python

import argparse
from os.path import basename

### "config" kind of...?
# the extension of Civ5 save files
extension = 'Civ5Save'

# for parsing the command line arguments
parser = argparse.ArgumentParser()

# set up the parser
parser.add_argument('inputfile', help='input save file')
parser.add_argument('--outputfile', '-o', help='output save file')

args = parser.parse_args()

if args.outputfile:
    outputfile = args.outputfile
else:
    outputfile = basename(args.inputfile) + '_priv.' + extension


print(outputfile)
