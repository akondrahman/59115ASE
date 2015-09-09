#Reading Assignment # 2 
##Date September 08, 2015 
### Summary of *The Influence of Organizational Structure on Software Quality: An Empirical Case Study* [1] 

#### Keywords	 
* ii1: Organizational Structure: The hypothetical structure that is used to categorize the responsibilities and assigner-assignee relationship inside that organization. 
* ii2: Software Quality Metric: Empirical concepts to evaluate the quality of a software
* ii3: Traditional Software Quality Metrics: Empirical concepts that are derived from software artifacts to quantify/or predict software quality 
* ii4: Organizational Software Quality Metrics: Empirical concepts that are derived from organizational aspects of a software organization  

#### Key Points
* iii1: Related Work: The paper provides a brief, yet comprehensive overview of empirical studies that discuss the implications of software organization, traditional software metrics such as code churn, code coverage, code complexity, and code dependencies. 
* iii2: Study Instruments: 
  * Version control of system used during the release point of Windows Vista, a Microsoft product
  * Step-wise regression, principal component analysis, precision, recall etc.  
* iii3: Baseline Results: The prediction accuracy can be used as a *baseline* for empirical studies that addresses the impact of organizational structure for software quality of software binaries 
* iii4: Informative Visualizations
  * The paper presents a very simple, but informative way to compare their proposed organizational model, with traditional models as shown below 
  ![output](res.png?raw=true=150x100)  
  * The paper presents a simple hierarchical snapshot where team heads and team members interact in a complex manner, as shown below   
  ![output](org.png?raw=true=150x100)    

#### Suggestions for Improvement 
* iv1: Organizations that often rush into deadlines, tend to add a lot of bugs in releases; the concept of deadline/project management can be added in the proposed organizational model  
* iv2: The binaries that are generated from source code can be assumed to follow a certain design, and project planning that are specific to an organization. This aspect of organization, can affect test design, software design which in the process can software quality. Would be interesting to see an empirical study that considers theses factors as well. 
* iv3: The metric task/engineer is also an organizational aspect that can affect software quality. Quantifying the tasks assigned for each engineer might vary across the organization, and can affect software quality 

#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [2]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. In this paper, the authors take a holistic organizational approach, disregarding the difference of aggregated and dis-aggregated levels.  

####Reference
[1] Nachiappan Nagappan, Brendan Murphy, and Victor Basili. The Influence of Organizational Structure on Software Quality: An Empirical Case Study, in *Proceedings of the 30th International conference on Software engineering (ICSE '08)*, pages 521-530, ACM, 2008

[2] D. Posnett, V. Filkov, and P. Devanbu. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM Inter- national Conference on Automated Software Engineering, pages 362–371. IEEE Computer Society, 2011. 