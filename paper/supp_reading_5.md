#Supplementary Reading - 5
##Date Nov 20, 2015 
### Summary of *Studying the Impact of Social Structures on Software Quality* [1]

#### Download Link 

http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5521754


#### Keywords	 
* ii1: Measure of Discussion Contents: Metrics related to software project development discussion that can be extracted from bug reports, stack traces, source code, and software repositories to measure software quality and software defects. 
* ii12: Measure of Social Structures: Metrics related to developer dependencies during software development, and maintenance that can be extracted from source code, and software repositories to measure software quality and software defects. 
* ii13: Measure of Communication Dynamics: Metrics related to developer communications during software development, and maintenance namely number of messages, length of messages, reply time, and interestingness, and workflow measures. These measures can be extracted from source code, and software repositories to measure software quality and software defects. 
* ii14: Post-Release Defects: Software defects and failures discovered after deployment or release of software. 


#### Key Points
* iii1: Related Work: The authors of the paper have cited multiple papers that are related to defects prediction, and social analysis. For example, that authors cited the work of Ahlberg et al. [2] that predicted failure-prone software modules using object-oriented code metrics.  

* iii2: Study Instruments: 
  * Six months of data obtained from the release of Ecplise 6.0
       
  * Social interaction measures such as centrality, interestingness, and workflow measures          
      ![output](images/supp_5_metrics.png?raw=true=100x80)  
  * pairwise correlation of social interaction measures   
      ![output](images/supp_5_corr.png?raw=true=100x80)  
  * hierarchical analysis of logistic regression model    
      ![output](images/supp_5_regr.png?raw=true=100x80)  

#### Suggestions for Improvement 
* iv1: Perform analysis on local and global level and observe how the results differ    
* iv2: Consider other factors related to software projects namely, fan-in, fan-out, and C&K metrics.    


#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [3]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. This paper performed a holistic approach where analysis was performed on one level (did not differentiate between aggregated or dis-aggregated level). 

#### Reference
[1] Bettenburg, Nicolas; Hassan, A.E., "Studying the Impact of Social Structures on Software Quality," in Program Comprehension (ICPC), 2010 IEEE 18th International Conference on , vol., no., pp.124-133, June 30 2010-July 2 2010

[2] Ohlsson, N.; Alberg, H., "Predicting fault-prone software modules in telephone switches," in Software Engineering, IEEE Transactions on , vol.22, no.12, pp.886-894, Dec 1996

[3] D. Posnett, V. Filkov, and P. Devanbu. 2011. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE '11). IEEE Computer Society, Washington, DC, USA, 362-371.