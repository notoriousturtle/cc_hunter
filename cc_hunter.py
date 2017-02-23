#!/usr/bin/python

"""
Credit Card Finder by the most notorious of all turtles., notorious_turtle

Run in the directory you want to recusrively scan from. 
Matches credit card without spacings only

All rights reserved. Copyright 2017.
"""

import sys
import getopt
import mmap
import os
import re

scanCount = 0

def scan(dir):
    global scanCount

    if verbose:
        print("Scanning dir: "+dir)

    for file in os.listdir(dir):
        if os.path.isdir(file):
            scan(os.path.join(dir, file))
        else:
            if file == sys.argv[0]:
                continue

            if verbose:
                print("Checking file: "+os.path.join(dir, file))
            # read file
            with open(os.path.join(dir, file), 'rb', 0) as f:
                s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                search = re.search(br"(4[0-9]{15}|5[1-5][0-9]{14}|3[47][0-9]{13}|6(?:011|5[0-9]{2})[0-9]{12})", s)

                if search:
                    for found in search.groups():
                        print("!!! Found "+found+" in: "+os.path.join(dir,file))

                s.close()
                scanCount = scanCount + 1

if __name__ == '__main__':
    verbose = False

    try:
        opts, args = getopt.getopt(sys.argv[1:], "")
    except getopt.GetoptError:
        print("\n *** CC Hunter *** \n")
        print("Usage: cc_hunter.py")
        print("Options: -v, --verbose = Verbose")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-v", "--verbose"):
            verbose = True

    scan('.')

    print("Scan complete, "+str(scanCount)+" files scanned")