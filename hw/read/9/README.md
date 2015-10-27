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

* iii3: *Statistical Tests*: The output of all prediction models was the probability of defect proneness of files.  Minimum thresholds for defect classification varied, while the authors recorded the *accuracy*, *precision*, *recall*, *f-measure*, *receiver operating characteristic (ROC)*, and *cost-effectiveness*, stating that different thresholds could alter these values. The authors began by "comparing the performance of process and code metrics in release based prediction settings using *AUC*, *AUCEC* and F<sub>50</sub>". And in their own jargon:

>> We compared the AUC performance for all types of metrics for a given learning technique using Wilcoxon tests and corrected the p-values using Benjamini-Hochberg (BH) correction. We also do the same to compare the performance of different learning techniques for a given set of metrics.


* iii4: *Anti-Patterns*:  The authors acknowledge the work of Posnett et al. in *Threats to Validity* for avoiding generalization.  They note that in order to avoid risk of the *ecological fallacy*, they have taken measures to compare their findings in a per project setting, reporting similar results.  In a previous paper by Rahman [2], it was noted that the file-level was chosen for analysis in response to the risk of *ecological fallacy*, while the same decision was made for this work without explicit declaration.

#### Suggestions for Improvement 
* iv1: The authors have an *ad hoc* way of describing procedures, as they often augment statistical analyses to produce clearer results. It would, perhaps, be helpful to clear up the order of changes and throught processes through a list or some other structure.  In paragraph form, discerning the important from the unimportant is tedious.

* iv2: From the way in which the procedures are communicated, the paper also seems to be model-heavy, with not much effort attributed to sampling procedures and variable extraction other than blanket statements.  Submitted papers tend to have length requirements, but it would be helpful to understand how certain features were extracted and why particular projects were chosen (other than they were the ones available).

* iv3: Is using only file-level defect prediction really the answer to the *ecological fallacy*?  From my understanding, the ecological fallacy restricts generalization of results to a different level of aggregations, not necessarily stating that the file-level is the answer.  Perhaps this should have been made more clear:  "These results only apply to file-level analysis of defect prediction in projects."

#### Connection to Initial Paper
It seems like every paper that follows Posnett et al's *ecological fallacy* has to, in some way at least once, describe some measure to taken to avoid the risk of it occuring.  This paper is not an exception.  In threats to validity, as mentioned previously, the authors describe an extra measure taken to cross-compare their results with analyses run per project.  It appears that, even today, researchers in defect prediction are still determining what the ecological fallacy means in terms of the organization of their research and their analysis and results.

#### Reference
1. Rahman, Foyzur, and Premkumar Devanbu. "How, and why, process metrics are better." Proceedings of the 2013 International Conference on Software Engineering. IEEE Press, 2013.
2. Rahman, Foyzur, Daryl Posnett, and Premkumar Devanbu. "Recalling the imprecision of cross-project defect prediction." Proceedings of the ACM SIGSOFT 20th International Symposium on the Foundations of Software Engineering. ACM, 2012.
