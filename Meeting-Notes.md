### Meeting List
* [Meeting: 2015/06/22](#meeting-20150622)
* [Meeting: 2015/06/17](#meeting-20150617)
* [Meeting: 2015/06/15](#meeting-20150615)

***

### Meeting 2015/06/22
Attendees: 
* Garrett, Madicken
* Refer to Weekly Updates 2015/06/19 for what these notes respond to. 

Main Notes:
* Garrett described issues of compatibility for an RSSA file for the surface source.
  * To do:
    * Find out if scale can produce an RSSA file that is compatible with MCNP
    * Can the RSSA file from scale be used for an MCNP surface source?
* Recursive point testing
  * Uses smaller and smaller blocks until each block contains only one material (up to some threshold value). It is a way of defining a (homogenized) macro-material when generating Denovo discretized input 
* Find out how Advantg and mavric use Denovo. What are their default parameters?
* We will probably start with a cylindrical mesh tally for the cask models, but we will likely test both cylindrical and rectangular meshes for the characterization of the method itself.
* Depending on the size of the MG library that you use for the forward calculation, that will influence how it bins the particles by energy group while you're tallying. 
  * Adjoint source particles 'energy' usually described by the detector response function.
  * Does the energy resolution of the cross section library limit what we can tally in the monte carlo.   
* Garrett was looking through the Advantg manual and found an interesting sample problem that might be useful as a starting point for our method. 
  * Simplified portal monitor

Other things:
* Garrett could start looking for various shielding benchmark problems that will be improved with angular information (literature review info) 
* Make new page on github for problems that you find. 
* Also can improve and add information on the cask model if necessary
* Also make a page for options that we can alter in Denovo (what Sn options are available? Legendre orders? etc.)
  * What options to mavric and advantg use? Do they recommend parameters for certain problems or do they default the same for each problem. 
  * List information on defaults for both monte carlo and denovo transport.   

### Meeting 2015/06/17
Attendees:
* Rachel, Garrett, Madicken

Main Notes:
* Garrett described the documents that he found on the ADAMS database on the "notes" page. 
* Garrett also described his progress on converting the transport model to a dry cask model. It looks AWESOME. 
* Garrett has been experimenting with making subtemplates 

Other Things:
* Do we want to do hybrid modelling of the casks with Advantg?
  * If so, how do we convert the scale input to an MCNP input? 
    * Should Madicken e-mail ORNL?
  * Decision: E-mail ORNL/Tara to see if a converter exists. 
  * Worst case: use scale to make a source term, then use that source term as a surface source in the MCNP model. 
* What stuff is 'okay' to put up on the github repo? Drawings without scale/material info? Original enrichment info?
  * Decision: Move all potentially sensitive documents to a private repo. 
* What level of fidelity should we be adding to the dry cask model? Include rebar sub-structure?
  * Decision: e-mail kaushik

To Do:
* Madicken: Make private repo to store sensitive documents.  
* Madicken: E-mail kaushik and ask him if he wants the rebar strucutring in the model. 
  * Also ask if they maybe just want the information and the high fidelity model isn't necessary right now. 
* Madicken: Send e-mail to tara to confirm if a scale to mcnp converter exists, and how to obtain one. 
* Garrett: find out what parameters you need to run the scale model. 
* Garrett: Start figuring out how to do a surface tally in mavric or keno (maybe only for criticality) or monaco. Probably for mavric to get the source description. So that when we actually get the software on the cluster we'll be ready to run. 
* Garret: (Far future plans) -- help madicken with simple test problems for the hybrid method. 

### Meeting: 2015/06/15
Main Notes:
* Github page is well on its way to being a repository for useful (publicly available) information on the project. 
  * Talked about linking inline images and .pdfs with the gh-pages branch (refer to munkm.github.io/caskmodels/.....) to do this. 
* Garrett added airflow pipes to the top of the cask. 
  * Garrett thinks that most of the geometry is done. 
    * Should we add rebar structuring inside the concrete overpack in the model? 
      * Is this something ORNL would want? I don't see it affecting transport significantly. 
      * Maybe need to look in to how frequently the rebar lattices occur axially. 

Other things:
* If Garrett runs out of modelling things to do:
  * Make a document in github page that summarizes the following:
    * What was the transportation cask that we were given? Fuel type? Burnup? Where was it from?
    * What is the dry cask information that you obtained from ADAMS? What is the type/manufacturer of that cask? (I know you've basically summarized this elsewhere, but it will be useful to put it all in the same place.)
    * What changes did you make from the transportation cask to get to the dry cask model? Just generally summarize this. 
* We need to find out if we'll just be using Advantg or both Advantg and Mavric. 
  * If we are just using Advantg, then MCNP is the monte carlo code we'll be using. We need to find a way to convert a scale input to an MCNP input for our project.  


