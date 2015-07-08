This folder contains codes used for the Cask Modeling Project

***

### Converter.py

**Description**

This is a python script designed to aid in the conversion of a SCALE input to an MCNP input. This script is to only be used for geometry conversion, and currently only converts special cases of cuboids, cylinders, and ycylinders. The script has builtin functionality for converting origin translations and rotations. The script will also add universe entries to the MCNP cards corresponding to the SCALE unit number the SCALE geometry is in, provided the line declaring the unit is included. The script will pass through any SCALE format comments into MCNP format comments.

The script will convert a specified section of SCALE input and output two new text files. One file named "MCNP_Surface_Input.txt", which will contain the converted MCNP surface cards to be added to the surfaces block of the MCNP input. The other output file is named "MCNP_Cell_Input.txt", which will contain cell cards to be added to the cells block of the MCNP input.

**Running**

The input argument line takes the path of the SCALE input file to convert. Below is an example running the script from the command line in the directory with the SCALE input and the converter.py script:

```
$ python converter.py SCALE_input.inp
```

The script will then prompt the user to enter the start line and end line of the SCALE input to specify what section to convert. The script will also ask at what number to start labeling the MCNP cells, as there is no corollary in SCALE. The script will finally ask if you want to add a factor to the labeling of the surfaces to account for the ability to reuse surface labels in SCALE in different units, but not in MCNP.

The script will automatically format the cell cards to include the materials, but some editing of the script must be done on the user's part to work for a desired SCALE input. In the main() function there is a dictionary labeled "d". This contains the material numbers as keys and the corresponding material density as the values. This is required as MCNP cell cards take the material density as an entry and this must be specified by the user as the script is not able to do this on its own.

**Tips & Tricks**
* It is suggested to only convert one unit at a time to assure you do not end up with duplicate surface and cell numbers.
* Any SCALE "holes" that place a unit into another unit (universe into another universe in MCNP) will have to be done manually.

