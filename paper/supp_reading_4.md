#Supplementary Reading - 4
##Date Nov 19, 2015 
### Summary of *Mining Metrics to Predict Component Failures* [1]

#### Download Link 

http://dl.acm.org/citation.cfm?id=1134349


#### Keywords	 
* ii1: Software metrics: Measurement tools derived from software repositories to perform quantitative analysis. 
* ii2: Failure prediction: A methodology to predict failures by minign and analyzing software repositories.



#### Key Points
* iii1: Related Work: The authors of have paper cited multiple papers that are related to defects and failures, complexity metrics, and historical data. For example, that authors cited the work of Hudepohl et al. [2] that predicted software failures from software design metrics, and reuse information from software repositories.  

* iii2: Study Instruments: 
  * Five project respositories namely, Internet Explorer 6, IIS W3 Server Core, Process Messaging Component, DirectX, and NetMeeting   
  
      ![output](images/supp_4_projects.png?raw=true=100x80)    
      
  * File-based metrics: module metrics, per-function metrics, per-class metrics        
  
      ![output](images/supp_4_metrics.png?raw=true=100x80)  
  * logistic regression 
  * principal component analysis (PCA)   
  * correlation measures: Pearson, Spearman   

#### Suggestions for Improvement 
* iv1: Perform analysis on local and global level and observe how the results differ    
* iv2: Consider other factors related to software projects namely, developer dependency in a project, fan-in, fan-out, C&K metrics etc.    


#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [3]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. This paper performed a holistic approach where analysis was performed on one level (did not differentiate between aggregated or dis-aggregated level). 

#### Reference
[1] Nachiappan Nagappan, Thomas Ball, and Andreas Zeller. 2006. Mining metrics to predict component failures. In Proceedings of the 28th international conference on Software engineering (ICSE '06). ACM, New York, NY, USA, 452-461. 

[2] Hudepohl, J.P.; Aud, S.J.; Khoshgoftaar, T.M.; Allen, E.B.; Mayrand, J., "Emerald: software metrics and models on the desktop," in Software, IEEE , vol.13, no.5, pp.56-60, Sep 1996. 

[3] D. Posnett, V. Filkov, and P. Devanbu. 2011. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE '11). IEEE Computer Society, Washington, DC, USA, 362-371.