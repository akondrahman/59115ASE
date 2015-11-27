#Supplementary Reading - 3
##Date Nov 19, 2015 
### Summary of *Predicting Failures with Developer Networks and Social Network Analysis* [1]

#### Download Link 

http://dl.acm.org/citation.cfm?id=1453106


#### Keywords	 
* ii1: Developer network: A network that infers the developer dependencies for the developed software artifacts. 
* ii2: Social network analysis (SNA): Analyzing the collaborative structure that can be inferred directly, and indirectly from software module depenedencies, and developer dependencies.       
* ii3: Failure prediction: A methodology to predict failures by minign and analyzing software repositories.



#### Key Points
* iii1: Related Work: The authors of have paper cited multiple papers that are related to failure prediction, and network analysis. For example, that authors cited the work of Arisholm et al. [2] that examined several data mining techniques for fault prediction for a telecommunications project. Arisholm et al. [2] used multiple techniques such as decision trees, neural networks, and logistic regression. 

* iii2: Study Instruments: 
  * Project respository from a telecommunications company called _Nortel Networks_.  
  * File-based metrics: updates, code churn, developers, number of hub developers      
  
    ![output](images/supp_3_metrics.png?raw=true=100x80)    
    
* iii3: Model selection: system testing model, post-release model
* iii4: Model validation: cross-fold validation

#### Suggestions for Improvement 
* iv1: Perform analysis on local and global level and observe how the results differ    
* iv2: Consider other factors related to software projects namely, developer dependency in a project, fan-in, fan-out, C&K metrics etc.    


#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [3]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. This paper performed a holistic approach where social network analysis was performed on one level. 

#### Reference
[1] Andrew Meneely, Laurie Williams, Will Snipes, and Jason Osborne. 2008. Predicting failures with developer networks and social network analysis. In Proceedings of the 16th ACM SIGSOFT International Symposium on Foundations of software engineering (SIGSOFT '08/FSE-16). ACM, New York, NY, USA, 13-23.

[2] Erik Arisholm, Lionel C. Briand, and Magnus Fuglerud. 2007. Data Mining Techniques for Building Fault-proneness Models in Telecom Java Software. In Proceedings of the The 18th IEEE International Symposium on Software Reliability (ISSRE '07). IEEE Computer Society, Washington, DC, USA, 215-224.

[3] D. Posnett, V. Filkov, and P. Devanbu. 2011. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE '11). IEEE Computer Society, Washington, DC, USA, 362-371.