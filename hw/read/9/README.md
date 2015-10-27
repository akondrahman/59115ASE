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
* iii1: *Motivational Statement*: The literature was divisive on the issues of the quality of process metrics and code metrics for use in defect prediction.  The authors cited papers that perfered process metrics over code metrics, papers that preferred code metrics over process metrics, and papers that qualified the use of both.  The goal of their research is to understand *why* and *how* each metric class (process or code) is effective, and under what conditions.

* iii2: *Sampling Procedures*: The authors selected 12 Java-based, Apache Software Foundations (ASF) projects from diverse domains.  For each project, they extracted the commit history from each project's GIT repository, while also using GIT *BLAME* on every file at each release to get detailed contributor information.  All 12 projects used JIRA, from which the authors extracted defect information and the defect-correcting commits.  The JIRA commits were diffed with the GIT commits to label the modified files as defective.  The following table includes information on the 12 selected projects:

![output](projects.png?)

* iii3: 
* iii4: *Anti-Patterns*:  The authors acknowledge the work of Posnett et al. in *Threats to Validity* for avoiding generalization.  They note that in order to avoid risk of the *ecological fallacy*, they have taken measures to compare their findings in a per project setting, reporting similar results.  In a previous paper by Rahman [2], it was noted that the file-level was chosen for analysis in response to the risk of *ecological fallacy*, while the same decision was made for this work without explicit declaration.

#### Suggestions for Improvement 
* iv1: 
* iv2: 
* iv3:

#### Connection to Initial Paper

#### Reference
1. Rahman, Foyzur, and Premkumar Devanbu. "How, and why, process metrics are better." Proceedings of the 2013 International Conference on Software Engineering. IEEE Press, 2013.
