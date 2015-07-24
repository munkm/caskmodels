# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 16:19:21 2015
@author: Garrett Baltz

This is a script designed to aid in the conversion of a SCALE input to an MCNP input. This script is to only be used for geometry conversion, and currently only converts special cases of cuboids, cylinders, and ycylinders.

The input argument line takes the path of the SCALE input file to convert. The script will then prompt the user to enter the start line and end line to specify what section of the input to convert. The script will also ask at what number to start labeling the MCNP cells, as there is no corollary in SCALE. The script will finally ask if you want to add a factor to the labeling of the surfaces to account for the ability to reuse surface labels in SCALE but not in MCNP.

** Warning **
This script is NOT a comprehensive converter and is currently tailored to convert a specific input.

"""

import sys
import re

# This function opens the SCALE input and imports the lines into memory to be used by other functions
def importLines(filepath, startLine, endLine):
    f = open(filepath, 'r')
    lines = f.readlines()
    lines = lines[startLine-1:endLine]
    f.close()
    return lines
    
# This function is called at the end to create and write the new MCNP input to the two output files
def inputWriter(fileName, LineList):
    f = open(fileName, 'a')
    f.writelines(LineList)
    f.close()
    
# This function is a helper to identify if a regular expression exists in a line. Returns true or false.
def Find(pat, text):
    match = re.search(pat, text)
    if match:
        bool = True
    else:
        bool = False
    return bool
 
# This function creates a transform card for a given x-axis angle tranform (angle). Returns the tranform card.   
def transform(angle):
    h1 = angle
    h2 = 90-angle
    h3 = 90
    h4 = 90 + angle
    h5 = angle
    h6 = 90
    tr= '*TRn 3J {} {} {} {} {} {}'.format(h1, h2, h3, h4, h5, h6)
    return tr
    
# This function converters SCALE cylinder objects into MCNP RCC macrobody surfaces.
# Input: Takes the line containing the SCALE cylinder (entry), and the value to increase the surface id by (cellMod)
# Returns the final MCNP surace card entry
def convertCylinder(entry, cellMod):
    # break the SCALE entry up into its separate parts
    comps = entry.split()
    label = comps[1]
    r = comps[2]
    zTop = float(comps[3])
    zBot = float(comps[4])
    
    label = int(label) + cellMod
    
    Hx = 0.0
    Hy = 0.0
    Hz = zTop - zBot
    
    # Determine if the surface origin is translated and what the coordinates are
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
        z = float(z.group()[2:]) + zBot
    else:
        z = zBot
        
    
    # Determine if the surface is rotated or not and also concatonates the final MCNP card
    if Find('a1=', entry) == True:
        theta = re.search('a1=\S+', entry.lower())
        theta = float(theta.group()[3:])
        tr = transform(theta)
        newEntry = '{} n RCC {} {} {} {} {} {} {}\nc replace n with number and place following tr card in data cards: \'{}\'\n'.format(str(label), str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), r, tr)
    else:
        newEntry = '{} RCC {} {} {} {} {} {} {}\n'.format(str(label), str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), r)
        
    return newEntry
    
# This function converters SCALE ycylinder objects into MCNP RCC macrobody surfaces.
# Input: Takes the line containing the SCALE cylinder (entry), and the value to increase the surface id by (cellMod)
# Returns the final MCNP surace card entry
def convertYCylinder(entry, cellMod):
    # break the SCALE entry up into its separate parts
    comps = entry.split()
    label = comps[1]
    r = comps[2]
    yTop = float(comps[3])
    yBot = float(comps[4])
    
    label = int(label) + cellMod
    
    if re.search(r'x=\S+', entry.lower()):
        x = re.search(r'x=\S+', entry.lower())
        x = float(x.group()[2:])
    else:
        x = 0.0
    if re.search(r'y=\S+', entry.lower()):
        y = re.search(r'y=\S+', entry.lower())
        y = float(y.group()[2:])
    else:
        y = yBot
    if re.search(r'z=\S+', entry.lower()):
        z = re.search(r'z=\S+', entry.lower())
        z = float(z.group()[2:])
    else:
        z = 0.0
        
    Hx = 0.0
    Hy = yTop - yBot
    Hz = 0.0
    
    if Find('a1=', entry) == True:
        theta = re.search('a1=\S+', entry.lower())
        theta = float(theta.group()[3:])
        tr = transform(theta)
        newEntry = '{} n RCC {} {} {} {} {} {} {}\nc replace n with number and place following tr card in data cards: \'{}\'\n'.format(str(label), str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), r, tr)
    else:
        newEntry = '{} RCC {} {} {} {} {} {} {}\n'.format(str(label), str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), r)
        
    return newEntry
    
# This function converters SCALE cuboid objects into MCNP RPP macrobody surfaces.
# Input: Takes the line containing the SCALE cuboid (entry), and the value to increase the surface id by (cellMod)
# Returns the final MCNP surace card entry
def convertCuboid(entry, cellMod):
    comps = entry.split()
    label = comps[1]
    
    label = int(label) + cellMod
    
    xmax = comps[2]
    xmin = comps[3]
    ymax = comps[4]
    ymin = comps[5]
    zmax = comps[6]
    zmin = comps[7]
    
    # Determine if the cuboid is rotated and concatonate the MCNP input
    if Find('a1=', entry) == True:
        theta = re.search('a1=\S+', entry.lower())
        theta = float(theta.group()[3:])
        tr = transform(theta)
        newEntry = '{} n RPP {} {} {} {} {} {}\nc replace n with number and place following tr card in data cards: \'{}\'\n'.format(str(label), xmin, xmax, ymin, ymax, zmin, zmax, tr)
    else:
        newEntry = '{} RPP {} {} {} {} {} {}\n'.format(str(label), xmin, xmax, ymin, ymax, zmin, zmax)
        
    return newEntry

# This function converters SCALE cone objects into MCNP TRC macrobody surfaces.
# Input: Takes the line containing the SCALE cone (entry), and the value to increase the surface id by (cellMod)
# Returns the final MCNP surace card entry    
def convertCone(entry, cellMod):
    comps = entry.split()
    label = comps[1]
    
    label = int(label) + cellMod
    
    Rt = comps[2]
    Zt = float(comps[3])
    Rb = comps[4]
    Zb = float(comps[5])
    
    Hx = 0.0
    Hy = 0.0
    Hz = Zt - Zb
    
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
        z = float(z.group()[2:]) + Zb
    else:
        z = Zb
    
    newEntry = '{} TRC {} {} {} {} {} {} {} {}\n'.format(str(label), str(x), str(y), str(z), str(Hx), str(Hy), str(Hz), Rb, Rt)
    return newEntry
    
# This function converts SCALE media objects into MCNP cell cards. Also adds the SCALE unit to the MCNP input as a universe entry
# Input: SCALE media line (entry), what number to start labeling the MCNP cells (cellNum), what factor surfaces are modified by (cellMod), the materials dictionary (matdict), cell's universe (uni)
# returns the MCNP cell card
def makeCell(entry, cellNum, cellMod, matdict, uni):
    comps = entry.split()
    mat = comps[1]
    defs = comps[3:]
    
    newEntry = '{} {} {}'.format(cellNum, mat, str(matdict[mat]))
    
    # The convention for defining cells is opposite in SCALE and MCNP. This fixes the convention and adds the surface label modification factor
    for i in defs:
        i = float(i)
        if i > 0:
            i = (i + cellMod)*-1
        else:
            i = i*-1 + cellMod
        i = str(i)[:-2]
        newEntry = newEntry + ' ' + i
    if uni != '0':
        newEntry += ' u={}\n'.format(uni)
    else:
        newEntry += '\n'
    return newEntry
        

# This is the main function called when the script is run
def main():
    if len(sys.argv) != 2:
        print 'Missing Input Arguments \n', 'usage: python converter.py SCALE_input_file'
        sys.exit(1)
    
    scaleInputPath = sys.argv[1]
    # Prompt the user for input for required variables
    startLine = int(raw_input("Line in SCALE input to start convsersion?\n"))
    endLine = int(raw_input("Line in SCALE input to stop convserion?\n"))
    cellNum = int(raw_input("What cell number to start from?\n"))
    cellMod = int(raw_input("Increase MCNP surface id's by what amount? (zero for no adjustment)\n"))
    uni = '0'
    # Initialize the lists containing the converter MCNP input lines to write to output files
    newSurfaceInput = []
    newCellInput = []
    
    # This is the material dictionary that must be manually adjusted for each SCALE input
    d = {'1': -7.94, '2':-2.702, '3': 0.1001, '5':-0.0012, '9':-0.0012, '99':-0.0012, '300':0.1169, '304':0.0852, '305':0.033, '306':0.0874, '307':-2.3, '19':-6.56, '109':-6.56, '1145':-9.997, '1146':-9.997, '1147':-9.997, '1148':-9.997, '1149':-9.997, '1150':-9.997, '1151':-9.997, '1152':-9.997, '1153':-9.997, '1154':-9.997, '1155':-9.997, '1156':-9.997, '1157':-9.997, '1158':-9.997, '1159':-9.997, '1160':-9.997, '1161':-9.997, '1162':-9.997, '409':-1.48, '509':-0.71, '609':-0.86, '709':-0.7}
    
    print '\n\nConverting the SCALE input:', scaleInputPath

    # Inport the desired SCALE input lines to convert
    lines = importLines(scaleInputPath, startLine, endLine)
    for line in lines:
        print line,
     
    print '\n\nConverting to MCNP Input...'
    # This determines what is in each line and then calls the appropriate function to convert the line for MCNP
    for line in lines:
        if Find(r'unit \d+',line) == True:
            match = re.search(r'unit \d+', line)
            uni = match.group()[5:]
        elif Find('com=', line) == True:
            match = re.search(r'com=[\S\s]+', line)
            newEntry = 'c {}'.format(match.group()[4:])
            newSurfaceInput += newEntry
            newCellInput += newEntry
        elif line[0] == '\'':
            newEntry = 'c {}'.format(line[1:])
            newSurfaceInput += newEntry
            newCellInput += newEntry
        elif Find('ycylinder', line) == True:
            newEntry = convertYCylinder(line, cellMod)
            newSurfaceInput += newEntry
        elif Find('cylinder', line) == True:
            newEntry = convertCylinder(line, cellMod)
            newSurfaceInput += newEntry
        elif Find('cuboid', line) == True:
            newEntry = convertCuboid(line, cellMod)
            newSurfaceInput += newEntry
        elif Find('cone', line) == True:
            newEntry = convertCone(line, cellMod)
            newSurfaceInput += newEntry
        elif Find('media', line) == True:
            newEntry = makeCell(line, cellNum, cellMod, d, uni)
            newCellInput += newEntry
            cellNum += 1
    
    print '\n\nFinished Conversion, Writing ouput files...'
    # Writes the complete MCNP surface and cell inputs to their corresponding output file.       
    inputWriter('MCNP_Surface_Input.txt', newSurfaceInput)
    inputWriter('MCNP_Cell_Input.txt', newCellInput)
    
    
    print 'Conversion complete.'
    
if __name__ == '__main__':
    main()