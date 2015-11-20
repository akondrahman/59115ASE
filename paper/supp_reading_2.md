#Supplementary Reading - 2
##Date Nov 19, 2015 
### Summary of *Studying the Impact of Dependency Network Measures on Software Quality* [1]

#### Download Link 

http://dl.acm.org/citation.cfm?id=1913303

#### Keywords	 
* ii1: Dependency network: An illustration where software modules are presented as nodes, and edges are represented for dependency between two mdoules.      
* ii2: Ego network: A network that consists of the modules itself and the other modules it is dependent on.
* ii3: Global network: A network that consists of all the modules and all the other modules each other is dependent on. 


#### Key Points
* iii1: Related Work: The authors of have paper cited multiple papers that are related to software metrics, code complexity metrics, and dependency network analysis. For example, that authors cited the work of Wolf et al. [2] that analyzed the effect of social developer networks, developer networks on predictign build failures. 
* iii2: Study Instruments: 
  * _Eclipse_ project respository.  
  * Network measures: density, broker, egoBetween, nEgoBetween, hierarchy, power, closeness, information, dwReach     
  
    ![output](images/supp_2_measures.png?raw=true=100x80)    
    
* iii3: Analysis tools: principal component analysis (PCA), Pearson, Spearman, and Recall  




#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [2]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. This paper analyzed social network analysis on two levels namely local, and global which were labeled as _ego_, and _global_, respectively.

#### Reference
[1] Thanh H. D. Nguyen, Bram Adams, and Ahmed E. Hassan. 2010. Studying the impact of dependency network measures on software quality. In Proceedings of the 2010 IEEE International Conference on Software Maintenance (ICSM '10). IEEE Computer Society, Washington, DC, USA, 1-10.

[2] Timo Wolf, Adrian Schroter, Daniela Damian, and Thanh Nguyen. 2009. Predicting build failures using social network analysis on developer communication. In Proceedings of the 31st International Conference on Software Engineering (ICSE '09). IEEE Computer Society, Washington, DC, USA, 1-11.