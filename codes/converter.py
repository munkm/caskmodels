# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 16:19:21 2015
@author: Garrett Baltz

This is a script designed to aid in the conversion of a SCALE input to an MCNP input.

"""

import sys

def importLines(filepath, startLine, endLine):
    f = open(filepath, 'r')
    lines = f.readlines()
    lines = lines[startLine-1:endLine]
    f.close()
    return lines
    
def inputWriter(fileName, LineList):
    f = open(fileName, 'a')
    f.writelines(LineList)
    f.write(d['a'])
    f.close()
    
    
def main():
    if len(sys.argv) != 2:
        print 'Missing Input Arguments \n', 'usage: python converter.py SCALE_input_file'
        sys.exit(1)
    
    scaleInputPath = sys.argv[1]
    startLine = int(raw_input("Line in SCALE input to start convsersion?\n"))
    endLine = int(raw_input("Line in SCALE input to stop convserion?\n"))
    cellMod = int(raw_input("Increase MCNP surface id's by what amount? (zero for no adjustment)\n"))
    
    print scaleInputPath
    print startLine
    print endLine
    print cellMod
    
    d = {}
    d['a'] = 'alpha'
    
    lines = importLines(scaleInputPath, startLine, endLine)
    for line in lines:
        print line,
        
    inputWriter('new_file.txt',lines)
    
if __name__ == '__main__':
    main()