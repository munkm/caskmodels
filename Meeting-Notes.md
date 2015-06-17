### Meeting List
* [Meeting: 2015/06/15](#meeting-20150615)

***

### Meeting 2015/06/17
Attendees:
* Rachel, Garrett, Madicken

Main Notes:

Other Things:
* Do we want to do hybrid modelling of the casks with Advantg?
  * If so, how do we convert the scale input to an MCNP input? 
    * Should Madicken e-mail ORNL?
* What stuff is 'okay' to put up on the github repo? Drawings without scale/material info? Original enrichment info?
  * In general ......
* What level of fidelity should we be adding to the dry cask model? Include rebar substrucutre? 

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


