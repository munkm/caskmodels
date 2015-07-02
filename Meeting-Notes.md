### Meeting List
* [Meeting: 2015/06/30](#meeting-20150630)
* [Meeting: 2015/06/29](#meeting-20150629)
* [Meeting: 2015/06/23](#meeting-20150623)
* [Meeting: 2015/06/22](#meeting-20150622)
* [Meeting: 2015/06/17](#meeting-20150617)
* [Meeting: 2015/06/15](#meeting-20150615)

***
### Meeting 2015/06/30
Attendees: Rachel, Garrett, Madicken

Main Notes:
* Garrett showed Rachel the progress he made on adding rebar to the cask model.
  * As of today, he thinks he is finished with adding the rebar
  * He is going to make a subtemplate to turn on and off the rebar in the cask model
* Cask model subnotes:
  * The rebar structure is plotted in regular scale. Fulcrum has issues with plotting ring structures. When we send the model back to ORNL that will be an important thing to note. 
  * We'd also like to test transport on the model before we send it back to ORNL. Right now the model is pretty much finished (as we know it), but we need to install software on savio to make sure that there aren't issues when we run it in scale. 
* Garrett also summarized his goals for the week
* Which assembly to use? 
  * Look at the one with the highest neutron emission rate
  * And the one with the highest photon emission rate



### Meeting 2015/06/29
Attendees: Garrett, Madicken
Main Notes:
* Garrett added rebar to the cask
  * The dry cask can be described and put on the public repo
  * Data for the dry cask was taken from publicly available documents, so a plotted geometry of that information should not be subject to export control restrictions. 
* All of the vertical rebar has been added
  * Still need to add axial rings of rebar
    * Fulcrum doesn't have the ability to plot ring geometry, so rendering the geometry for rings had some issues. 

Questions:
* Which assembly do we want to use?
  * Maybe the one with the highest burnup
    * High burnup has more interesting n-capture radioisotopes
  * Shorter cooling time
    * Less time for short-ish-length radioisotopes to decay away

Other things:
* Garrett plans to have all cask rebar structures modelled this week. 
  * We'd like to give the model back to ORNL when this is finished.
    * We should test that the model doesn't have transport or geometry errors. We can't run the model on garrett's local machine because the source files and the setup for the input are strucutred to run on a UNIX-like system. 
       * Probably need to wait to give model to ONRL until testing is done
  * ACTION: Get stuff installed on savio so we can run the problem. 

### Meeting 2015/06/23
Attendees: Rachel, Garrett, Madicken

Main Notes:
* Got an e-mail back from kaushik; he wants garrett to model the rebar.
* We want to do continuous energy monte carlo in hybrid calculations. 
* Rachel wrote an ANS summary on choosing parameters for FW-CADIS. 
  * She put it in the dropbox group folder. See for review. 
  * Both the abstract and the presentation are in the background folder. 
* Garrett was looking into making a surface source in scale. 
  * MCNP and SCALE are not compatible with source terms. 
* Fuel source terms are binary files form origen.
  * Need to find out how to get these files to an MCNP-readable format.
  * Maybe we need to e-mail kaushik to get the input that was put into origin to get these material sources. 
* **Discussion** Converting the template to MCNP vs. making a pseudo-volume source:
  * Converting the template to MCNP would take time
    * Maybe it is possible to change the sub-templates to an MCNP format? 
    * Not all of the same fuel assemblies are in the cask, so changing to MCNP would involve changing all of those sub templates? 
    * Maybe we could use the same assembly repeated 24 times instead of 24 different assemblies?
    * Garrett could parse the scale file with regex to copy over numbers and dimensions and then manually construct the MCNP deck around that. 
      * this is probably the path of least resistance. 
  * The pseudo volume source could be a tally from scale, then put that tally information into a simpler geometry MCNP file.
    * The tally in scale could either be before the overpack and before the canister.   
* **Decision** Garrett will parse the scale file with regular expressions to get numbers and dimensions of the canister. Then the mcnp deck will be built manually around that. 
   * 1. The fuel source term can be converted to a MCNP format with monteburns somehow. 
   * 2. Or we could e-mail kaushik to get the original input for origin and put it into an MCNP format directly -- is this possible with origin? 
   
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


