#Reading Assignment # 8
##Date October 18, 2015 
### Summary of *Recalling the "Imprecision" of Cross-Project Defect Prediction* [1] 

#### Download Link
http://goo.gl/oTWyA0

#### Keywords
* ii1: *Empirical Software Engineering*: "focuses on experiments involving software systems (software products, processes, and resources). The purpose of these experiments is to collect data that can be used to validate theories about the processes involved in software engineering [2]."
* ii2: *Fault Prediction*: To make "use of a plethora of structural measures in order to predict faults, even in
the absence of a fault history... Example structural measures include lines of code, operator counts, nesting depth, message passing coupling, information flow-based cohesion, depth of inheritance tree, number of parents, number of previous releases the module occurred in, and number of faults detected in the module during the previous release [3]."  Accurate fault prediction at an early stage of development, despite the lifecyle phase, allow for code to be fixed at a lower cost [3].
* ii3: *(Code) Inspection*: The practice of reviewing code for any defects or process improvements. May be performed by person, team of people, and/or a model built for fault detection.
* ii4: *Cross-Project Prediction*: "using data from one project to predict defects in another [1]."  As the title of the paper suggests, this is an imprecise practice.

#### Key Points
* iii1: *Motivation Statements*: Because new projects are slight on historical data, there is growing interest in *cross-project prediction*--using data from existing projects to predict defects in another.  However, to date the results of these studies have been underwhelming.  Past projects have used the standard IR-based measures of *precision*, *recall*, and *f-score*, with specific threshold settings determined by methods such as logistic regression.  Rahman et al, argue that these are not well suited for cross-project predition.  The authors propose that a variety of tradeoffs (*viz*, 5%, 10%, or 20% of files tested or inspected) would be more suitable.
* iii2: *Sampling Procedures*: The authors "collected defect data and predictive metrics for several projects". They chose data sets and process metrics considering the following features:
  * *Commits* - "Number of commits made to this file during release"
  * *Active Devs* -  "Number of developers who made changes during this release"
  * *Added* - "LOC during this release normalized by file size"
  * *Deleted* - "Deleted LOC during this release normalized by file size"
  * *Changed* - "Changed LOC during this release normalized by file size"
  * *Features* - "Number of new features in this file during this release"
  * *Improvements* - "Number of improvements in this file during this release"
  * *Log* - "SLOC Log source lines of code"
Project List: Axis2, CXF, Camel, Cayenne, Derby, Lucene, OpenEJB, Wicket, XercesJ
* iii3: 
* iii4:

#### Suggestions for Improvement 
* iv1:
* iv2:
* iv3:

#### Connection to Initial Paper

#### Reference
1. Rahman, Foyzur, Daryl Posnett, and Premkumar Devanbu. "Recalling the imprecision of cross-project defect prediction." Proceedings of the ACM SIGSOFT 20th International Symposium on the Foundations of Software Engineering. ACM, 2012.
2. https://en.wikipedia.org/wiki/Experimental_software_engineering
3. Binkley, David, et al. "Software fault prediction using language processing." Testing: Academic and Industrial Conference Practice and Research Techniques-MUTATION, 2007. TAICPART-MUTATION 2007. IEEE, 2007.


