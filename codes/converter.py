# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 16:19:21 2015
@author: Garrett Baltz

This is a script designed to aid in the conversion of a SCALE input to an MCNP input.

"""

import sys
import re

def importLines(filepath, startLine, endLine):
    f = open(filepath, 'r')
    lines = f.readlines()
    lines = lines[startLine-1:endLine]
    f.close()
    return lines
    
def inputWriter(fileName, LineList):
    f = open(fileName, 'a')
    f.writelines(LineList)
    f.close()
    
def convertCylinder(entry, uni):
    comps = entry.split()
    label = comps[1]
    r = comps[2]
    zTop = float(comps[3])
    zBot = float(comps[4])
    if re.search(r'x=\S+', entry.lower()):
        x = re.search(r'x=\S+', entry.lower())
        x = float(x.group()[2:])
    else:
        x = 0.0
    if re.search(r'y=\S+', entry.lower()):
        y = re.search(r'y=\S+', entry.lower())
        y = float(y.group()[2:])
    else:
        y = 0.0
    if re.search(r'z=\S+', entry.lower()):
        z = re.search(r'z=\S+', entry.lower())
        z = float(z.group()[2:])
    else:
        z = 0.0
    Hx = 0.0
    Hy = 0.0
    Hz = abs(zTop) + abs(zBot)
    if uni != '0':
        newEntry = '{} RCC {} {} {} {} {} {} {} u={}\n'.format(label, str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), r, uni)
    else:
        newEntry = '{} RCC {} {} {} {} {} {} {}\n'.format(label, str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), r)
    return newEntry
    
def main():
    if len(sys.argv) != 2:
        print 'Missing Input Arguments \n', 'usage: python converter.py SCALE_input_file'
        sys.exit(1)
    
    scaleInputPath = sys.argv[1]
    startLine = int(raw_input("Line in SCALE input to start convsersion?\n"))
    endLine = int(raw_input("Line in SCALE input to stop convserion?\n"))
    cellMod = int(raw_input("Increase MCNP surface id's by what amount? (zero for no adjustment)\n"))
    uni = '0'
    newInput = []
    
    print scaleInputPath
    print startLine
    print endLine
    print cellMod

    lines = importLines(scaleInputPath, startLine, endLine)
    for line in lines:
        print line,
        
    for line in lines:
        match = re.search('cylinder', line)
        if match:
            newEntry = convertCylinder(line, uni)
            newInput += newEntry
            
    inputWriter('newInput.txt', newInput)
    
if __name__ == '__main__':
    main()