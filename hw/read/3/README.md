#Reading Assignment # 3 
 
### Summary of *Does Distributed Development Affect Software Quality? An Empirical Case Study of Windows Vista* [1]

#### Download Link 
http://ieeexplore.ieee.org.prox.lib.ncsu.edu/stamp/stamp.jsp?tp=&arnumber=5070550

#### Keywords	 
* ii1: Distributed Development: This term refers development of software that is spread across various levels - building, campus, locality, continent, world. Different teams working at different locations work together to build a complex software system. 
* ii2: Collocated Development: This refers to development of software systems in which the teams are working in the same location - say same building or floor. In collocated development, teams can reach out to each other and communication and collaboration becomes relatively easy.
* ii3: Software Quality: This refers to the quality of software that is being produced. Quality is typically measured in terms of failure/bugs found in the software. A poor quality software will have more bugs and encounter failures.
* ii4: Outsourcing: It is a special case of distributed development model in which different companies work on building a complex software system.

#### Key Points
* iii1: Related Work: The paper provides a brief survey of the important work done in the area of globally distributed software development. The authors discuss the effects of distributed development on bug resolution. Some papers conclude that it indirectly introduces delay while some say it does not have a strong effect. Some conclude only feasible decisions should be made in a project. Previous works have also focused on the effects on quality and productivity. It has been found that there is little, if any, correlation between geographic distance of developers and productivity and defect density. Offshoring can lead to several drawbacks such as more documentation needs. Some previous papers also focused on risk factors and categorized them. They found that globally distributed model did not increase defect density and they come up with key actions that make a successful global development model.
* iii2: Motivational Statements: 
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