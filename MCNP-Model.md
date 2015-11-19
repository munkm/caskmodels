### Model Info
* The MCNP model is based off the SCALE VCC cask model that was developed from the original transportation cask (see [Cask-Information](./Cask-Information.md)).
* The MCNP model has all the same dimensions as the SCALE model, as it was developed primarily by using the SCALE to MCNP converter that automatically pulled in the correct dimensions.
  * Instead of containing 24 unique fuel assemblies, the MCNP model is filled with one characteristic fuel assembly. This fuel assembly is assembly #9 in the original SCALE model. This assembly was chosen because it had the highest burnup and the shortest cooling time, meaning it would have the highest activity.
* NOTE: As of 11/19/2015 all the MCNP models used do not contain the rebar ring structures in the concrete overpack. This was due to an issue where particles were being lost in the toroid cells.

***
  
### SCALE to MCNP conversion
* The model was primarily constructed using the SCALE to MCNP python converter that was developed for this project (see [Codes](https://github.com/munkm/caskmodels/tree/master/codes)).
  * The converter script was used to pull in SCALE geometery cards and convert them into MCNP surface and cell cards with the same dimensions. This process helped ensure the MCNP model was identical to the SCALE model.
* The converter script is not able to convert materials, so this process was performed manually with help of the SCALE and MCNP manuals.
* As the fuel assembly geometry is very complex containing multiple universes and lattices, this was primarily constructed by hand. All dimensions were hand copied and pasted from the SCALE input.
* The converter was used to convert the TSC-1 cannister, the base weldment structure, air inlets and air outlets, and the concrete overpack.

***

### Source Terms
* The source used in the model was generated using the ORIGAMI code. The same input used to generate the source terms for the original SCALE model was modified to create source terms for use in the MCNP model.
  * The files used for source term generation are in the private repository [Source](https://github.com/munkm/caskmodels_private/tree/master/MCNP_Cask_Models/Source_files) folder.
* The file 2801_P028_bounding_05-06-2015.inp is the ORIGAMI input file that was used to generate the source terms. In order to successfully run this file, the path to the restart file linked in the beginning shell module must be working.
* The file 2801_P028_bounding_05-06-2015.out is the ORIGAMI output file that contains the energy distributions used in the MCNP source terms. The energy distributions are listed for gamma and neutron, for each of the 18 axial nodes in the fuel assembly. The energy distributions were extracted and placed into an excel file discussed below.
* The file 2801_P028_bounding_05-06-2015_MCNP_neutron has the total source strength for each of the 18 axial nodes in the fuel assembly. These were added together and multiplied by 24 to get the total source strength of the cask. This total source strength is used as the tally multiplier (fm card) to get correct fluxes for the cask source strength.
* The file neutron_source-strengths is an excel file containing the extracted energy distributions for the 18 axial nodes. They are separated by sheets in the excel workbook. Sheet 1 corresponds to axial node 1, sheet 2 to axial node 2, etc.

***

### MCNP VCC Dry Storage Cask Images
* These are images of the MCNP cask model.
* This is a view of a vertical slice of the dry cask. Here you can see the entire cask. Seen in the concrete overpack are the cross-sections of the axial rebar rings as well as 2 of the vertical rebars. Seen at the top of the cask is the shield plug and cask lid. At the bottom of the cask a slice through the weldment structure is seen, along with 2 of the air inlets which protrude from the base weldment to the outside of the cask. 
![image_1]
(http://munkm.github.io/caskmodels/Images/MCNP_side.png)
* This is a view of the cross section of the cask.
![image_1]
(http://munkm.github.io/caskmodels/Images/MCNP_xs.png)
* This is a view of the base weldment and air inlets at the bottom of the cask.
![image_1]
(http://munkm.github.io/caskmodels/Images/MCNP_base_weldment.png)


