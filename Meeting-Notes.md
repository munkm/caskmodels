### Meeting List
* [Meeting: 2015/06/15](#meeting-20150615)
* [Meeting: 2015/06/17](#meeting-20150617)

***

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


