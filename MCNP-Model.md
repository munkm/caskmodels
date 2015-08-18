### Model Info
* The MCNP model is based off the SCALE VCC cask model that was developed from the original transportation cask (see [Cask-Information](./Cask-Information.md)).
* The MCNP model has all the same dimensions as the SCALE model, as it was developed primarily by using the SCALE to MCNP converter that automatically pulled in the correct dimensions.
  * Instead of containing 24 unique fuel assemblies, the MCNP model is filled with one characteristic fuel assembly. This fuel assembly is assembly #9 in the original SCALE model. This assembly was chosen because it had the highest burnup and the shortest cooling time, meaning it would have the highest activity.

***
  
### SCALE to MCNP conversion
* The model was primarily constructed using the SCALE to MCNP python converter that was developed for this project (see [Codes](https://github.com/munkm/caskmodels/tree/master/codes)).
  * The converter script was used to pull in SCALE geometery cards and convert them into MCNP surface and cell cards with the same dimensions. This process helped ensure the MCNP model was identical to the SCALE model.
* The converter script is not able to convert materials, so this process was performed manually with help of the SCALE and MCNP manuals.
* As the fuel assembly geometry is very complex containing multiple universes and lattices, this was primarily constructed by hand. All dimensions were hand copied and pasted from the SCALE input.
* The converter was used to convert the TSC-1 cannister, the base weldment structure, air inlets and air outlets, and the concrete overpack.

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


