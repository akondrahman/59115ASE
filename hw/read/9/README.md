#Reading Assignment # 9
##Date October 26, 2015 
### Summary of *How, and why, process metrics are better* [1] 

#### Download Link
http://goo.gl/FqTGs2

#### Keywords
* ii1: *performance*: authors "compare the *performance* of different models in terms of both traditional measures such as AUC and F-score, and the newer cost-effectiveness measures"

* ii2: *stability*: authors "compare the *stability* of prediction performance of the models across time and over multiple releases"

* ii3: *portability*: authors "compare the *portability* of prediction models: how do they perform when trained and evaluated on completely different projects?"

* ii4: *stasis*: authors "study *stasis*, *viz..*, the degree of change (or lack thereof) in the different metrics, and the corresponding models over time. [They] then releate these changes with their ability to prevent defects."

#### Key Points
* iii1: *Sampling Procedures*: The authors selected 12 Java-based, Apache Software Foundations (ASF) projects from diverse domains.  For each project, they extracted the commit history from each project's GIT repository, while also using GIT *BLAME* on every file at each release to get detailed contributor information.  All 12 projects used JIRA, from which the authors extracted defect information and the defect-correcting commits.  The JIRA commits were diffed with the GIT commits to label the modified files as defective.  The following table includes information on the 12 selected projects:

![output](projects.png?)

* iii2: 
* iii3:
* iii4:

#### Suggestions for Improvement 
* iv1: 
* iv2: 
* iv3:

#### Connection to Initial Paper

#### Reference
1. Rahman, Foyzur, and Premkumar Devanbu. "How, and why, process metrics are better." Proceedings of the 2013 International Conference on Software Engineering. IEEE Press, 2013.
