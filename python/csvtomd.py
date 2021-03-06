#
#  csvtomd.py
#  Programming in Python
#
#  Created by Ojas Goyal on 7/30/16.
#  Copyright (c) 2016 Ojas Goyal. All rights reserved.
#

import csv

csv_path = 'build/readme/example.csv'
data_path = 'build/readme/data.md'

def addVertical(line):
    l = ""
    for word in line:
        l+=('| ' + word)
    l+=" | \n"
    return l

def addHeader(line):
    l = ""
    for i in range(0, len(line)):
        l += "| --- "
    l+=" | \n"
    return l

def main():
    fin = open(csv_path, 'r')
    fout = open(data_path, 'w')
    header = 1
    title = []
    for line in fin:
        line = line.strip()
        line = line.split(',')
        wline = addVertical(line)
        fout.write(wline)
        if header:
            hline = addHeader(line)
            fout.write(hline)
            header = 0
    fin.close()
    fout.close()

if __name__== "__main__":
    main()
