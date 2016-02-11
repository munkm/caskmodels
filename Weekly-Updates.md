### Update List
* [Update: 2016/02/11](#update-20160211)
* [Update: 2015/10/07](#update-20151007)
* [Update: 2015/08/24](#update-20150824)
* [Update: 2015/08/14](#update-20150814)
* [Update: 2015/07/24](#update-20150724)
* [Update: 2015/07/17](#update-20150717)
* [Update: 2015/07/10](#update-20150710)
* [Update: 2015/07/06](#update-20150706)
* [Update: 2015/06/26](#update-20150626)
* [Update: 2015/06/19](#update-20150619)
* [Update: 2015/06/12](#update-20150612)
* [Sample Update: 2000/01/01](#update: 2000/01/01)

***

### Update: 2016/02/11
Oh my, we've been away for some time.

**Progress Since Last Update:**
* Ran cask models for cylindrical and cartesian tally meshes.
* Figured out how to mcplot on cluster using x windows to generate tally plots.

**This Weeks Progress:**
* Characterization Problems Input Generation:
    * Generated input deck for prob_1 based on the image on the angular methods dropbox.
        * the mesh tally would still have to be edited for this problem if FW-CADIS desired.
    * Generated input deck for prob_2.
        * same thing regarding mesh tally.
        
**Future Plans:**
* Generate all simple characterization problems on angular methods dropbox.
* Generate reflected beam problem.
* Discuss other simple/more intermediate characterization problems at next meeting.
* Generate advantage inputs, run characterization problems.



### Update: 2015/10/07
**Progress Since Last Update:**
* Finished source terms for all assemblies in MCNP cask model.
* Created MCNP inputs for 3 different tallying setups:
  * Spherical detector on side of cask
  * Spherical detector above cask on vertical axis.
  * Mesh tally over outside area of cask.


### Update: 2015/08/24
**This Weeks Progress:**
* Added MCNP model information page detailing conversion and showing pictures of cask model.
* Successfully edited and ran ORIGAMI to get source terms for assembly.
  * Extracted all source terms into an excel file for manipulation.
* Took notes on MCNP SDEF card.
* Started developing SDEF card. Completed source description for assembly #1.

**Future Plans**
* Finish source terms for all assemblies in cask.

### Update: 2015/08/14
**This Weeks Progress:**
* MCNP model without rebar was complete last week.
  * Input added to private repository.
* MCNP model with rebar was completed this week.

**Future Plans/ Items Remaining:**
* Waiting on MCNP source distributions from Kaushik.
* Add information page on MCNP models.
* Finish SCALE input?
  * Still need to make discretized mesh for CADIS
  * wanted to test before give to Kaushik?



### Update: 2015/07/24
**This Weeks Progress**
* Further devloped concrete overpack
  * Modeled full base weldment structure
  * Modeled air inlets
  * Started modeling top air outlets
  


### Update: 2015/07/17
**This Weeks Progress**
* Made major progress on MCNP model
  * Got Lattice to work for fuel pin structure
  * Made canister and basket assembly geometry and replicated fuel assembly

**Plan for Next Week:**
* Develop concrete overpack geometry.


### Update: 2015/07/10
**This Weeks Progress**
* Finished SCALE to MCNP conversion script
  * Added readme file to codes folder with information on script
  * Added inline comments to script for reference
* Started MCNP Cask model
  * Converted all SCALE materials in MCNP materials
  * Constructed first assembly guide tube. Working on fuel pin lattice
  
**Plan for Next Week:**
* Continue working on MCNP model (Yay)


### Update: 2015/07/06
**This Weeks Progress**
* Added all rebar structures to SCALE VCC model.
* Created subtemplate for VCC model with rebar.
* Researched parallels between SCALE and MCNP inputs.
* Started developing a python script for SCALE to MCNP conversion.
* Added dry cask images to public repo and added rebar structures description to the Cask-Information page.

**Plan for this Week:**
* Continue developing SCALE to MCNP conversion script.
* Start making MCNP input.


### Update: 2015/06/26
**This Weeks Progress**
* Added all vertical rebar structures to concrete overpack.
* Figured out how to plot cask geometry by running scale and using built-in plot card. I had to learn how to do this due to Fulcrum (geometry viewer for SCALE inputs) not being able to process a ring structure (feature not yet supported in beta version).

**Questions**
* Pick which assembly we want to use to replace all other assemblies in the models (The One Assembly). One with high enrichment and burnup?

**Goals for Next Week**
* Have all cask rebar structures modeled.
* Make new sub-template for VCC dry overpack with all rebar structures. I am planning to make this in addition to the subtemplate I already made. This way you could choose if you wanted to use the cask model with or without rebar.
* Start researching parallels between SCALE and MCNP geometry, specifically arrays and universes for converting the input.
* Research regex (planning to use python), generate script to help SCALE to MCNP conversion



### Update: 2015/06/19
**This Weeks Progress**
* Generated Cask-Information page. This page has information on the original cask model and information on the new cask model, including what changes were made.
* Researched test problems.
* Researched creating surface sources in SCALE.
* Researched what parameters are needed for running SCALE dry cask input.

**Questions/Results of Research**
* Parameters for SCALE Input
  * Tally
	* Assuming we will use a mesh tally.
	  * Cylindrical or rectangular
	* Response
	  * Use flux-to-dose factors?
	  * Binning by energy groups? (this will be affected by what mode we run in. See "General Parameters" below)
  * Adjoint/ FW-CADIS parameters (assuming we are using FW rather than regular CADIS)
	* There is an example for mesh sizing for a cask in the MAVRIC manual. May be a good example to follow.
	* Changing any of the default parameters for Denovo. There are A LOT of options.
	  * S_n number, Legendre order, polar and azimuthal angles per octant.
	  * What solver to use. 
	* What method to use to create macro-materials
	  * Ray-tracing or recursive point testing
	    * Due to complexity and the sheer amount of different materials in the fuel assemblies, probably best to use ray-tracing?
  * General Parameters
	* What mode or library to run Monaco in?
	  * The original ORNL input performs the FW-CADIS calcs with a 27n19g, and then runs the monaco Monte Carlo calculations using a continuous energy library (which monaco in SCALE 6.2 apparently has the ability to do).
	  * Other option is to use a larger (or same library used in CADIS) multi-group library. Can go all the way up to like a 200 group library.
	* Number of particle histories to run/ use a time limit
	  * dependent on how many cores are used
	* Leave on default fission neutron and secondary gamma generation?
	  
* Creating surface source for use in MCNP model
  * I could not find any built-in functionality for generating a surface source or using a surface source in SCALE.
  * The closest thing I found was creating what is called a "Mesh source file", but I don't think this is what we need.
  * Also the format of the surface source file for use in MCNP is a binary .RSSA file. Anything produced by SCALE would have to be compatible with this.
  * I think if we were to use a surface source in the manner we had discussed it would have to be done manually somehow. It would probably be best to consult with someone who knows SCALE better than I do to:
    * 1. verify there is no built-in surface source functionality in monaco/MAVRIC/KENO, and 
	* 2. see if a different method already exists to create a surface source in SCALE (for eventual use in MCNP).
		

### Update: 2015/06/12
**This Weeks Progress:**
* Git
  * Development of VCC cask now under Git version control
  * Set-up backup of local Git files and repos onto External Hard Drive
  * This public Github repo/website was setup
* VCC Cask Model
  * Added all air outlets to cask model.
  * Added shield plug and cask lid to model
* Template Engine
  * Test ran TemplateEngine in cmd and was able to produce the same input we were provided with.
  * Determined best way to integrate VCC cask model with existing subtemplate by using the "analysis_type" key.

  
**Questions:**
* Cask model completed/ How much detail to include?
  * Possible additions include rebar inside concrete, various bolts, chamfering of cask?
* Investigate MCNP input options further
  * Code that converts SCALE -> MCNP
  
**Goals for Next Week:**
* To be determined on Monday meeting.

**Other Updates:**
* RE: The existentialism of Octocat
  * The only feasible conclusion is Octocat thinks, therefore, it is. QED


### Update: 2000/01/01
Author: Madicken

**Notes:**
* This is really just a sample update so you have an idea of what subsections you might want to include in an update. You by no means need to follow this strictly; feel free to add or remove sections as you feel fit. 
* This update is written in markdown, which isn't too hard once you get used to the formatting. I've included two links for reference.
  * [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for quick referencing
  * [Github Markdown introduction](https://help.github.com/articles/markdown-basics/)
 
**Goals from last time:**
* **Done** Had a fascinating discussion about GoT
* **Not Done** Thoroughly research the story of Iphigenia to understand Stannis' sacrifice

**Other Updates:**
* Still trying to understand Octocat's origins

**Questions:**
* Why does octocat exist, anyways?
  * And who would ever own an octodog?

**Goals for Next week:**
* Clean up this page and update stuff!  

