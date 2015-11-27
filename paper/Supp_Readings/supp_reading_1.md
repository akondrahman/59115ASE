#Supplementary Reading - 1 
##Date Nov 19, 2015 
### Summary of *Cross-project Defect Prediction (A Large Scale Experiment on Data vs. Domain vs. Process)* [1]

#### Download Link 
http://dl.acm.org/citation.cfm?id=1595713

#### Keywords	 
* ii1: Post-release Defects: Defects of a project that are discovered after the release of the software.   
* ii2: Cross-project Defect Prediction: A methodology to use one defect prediction model, to predict defects of another project.
* ii3: Similarity between Projects: Metrics that measure the similarity between two projects 


#### Key Points
* iii1: Related Work: The authors of have paper cited multiple papers that are related to defect prediction, and cross-project predictions. For example, Turhan et al. [] analyzed 12 NASA projects which were considered to be _cross company_. Turhan et al. [] identified cros project metrics to be helpful in cross-project defect prediction, along with the increase of false positives.     
* iii2: Study Instruments: 
  * Open-source and in-house projects source code respositories.  
  * Code measures: added line of code (LOC), total LOC, chrun, pre-release bugs, and cyclomatic complexity   
  
    ![output](images/supp_1_projects.png?raw=true=100x80)    
    
* iii3: Logistic regression, precision, recall, and accuracy   
* iii4: Decision tree: A machine learning technique to improve precision, recall, and accuracy

  ![output](images/supp_1_dec_tree.png?raw=true=100x80)  

#### Suggestions for Improvement 
* iv1: Perform analysis on local and global level and observe how the results differ    
* iv2: Consider other factors related to software projects namely, developer dependency in a project, fan-in, fan-out, C&K metrics etc.    

#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [3]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. This paper does not address the findings achieved at local and global level of software projects.

#### Reference
[1] T. Zimmermann, N. Nagappan, H. Gall, E. Giger, and B. Murphy,  Cross-project defect prediction: a large scale experiment on data vs. domain vs. process. In Proceedings of the the 7th joint meeting of the European software engineering conference and the ACM SIGSOFT symposium on The foundations of software engineering (ESEC/FSE '09). ACM, New York, NY, USA 

[2] B. Turhan, T. Menzies, A. B. Bener, and J. Stefano, On the relative value of cross-company and within-company data for defect prediction. Empirical Softw. Engg. 14, 5 (October 2009), 540-578

[3] D. Posnett, V. Filkov, and P. Devanbu. 2011. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE '11). IEEE Computer Society, Washington, DC, USA, 362-371.