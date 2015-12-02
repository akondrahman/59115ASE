# Implementing and Analyzing the  Integrated Project Model Defect Flow Chain 

## Team Members 
* ### Akond Rahman (aarahman@ncsu.edu)
* ### Bennett Nyarron (bynarron@ncsu.edu) 
* ### Manish Singh (mrsingh@ncsu.edu)


## Date Dec 01, 2015



## Abstract 

Software teams spend a lot of effort in reducing errors, and fixing the errors that have been generated as part of the development process. Software models that illustrate and predict the resources needed to reduce development errors, and predict estimation rate to reduce development errors can be of great help to software practitioners. _The goal of this project is to help software engineering researchers to analyze the Integrated Project Model Defect Flow Chain proposed by Abdel-Hamid and Madnick, by implementing the model, and optimizing the model using a standard optimizer_. In this project we implemented a standard software model that takes development effort into account and calculates the amount of development errors with certain assumptions, and considering a subset of the full development resource inputs. To optimize the development resources needed to reduce development errors we use differential algorithm (DE). We observe that a subset of the complete list of development resource inputs is required to provide an optimal solution for reducing errors for this software model of interest. We also observe real world software project resource inputs for optimal output.  

## Introduction 

The impact of software defects on software product delivery is significant and a well-studied topic amongst software practitioners and academicians. According to a study conducted by NASA Johnson Space Center, the cost of fixing software defects increases exponentially in the latter stages of the project . Jones in his book [] showed that cost of fixing a defect increases significantly during testing, and maintenance phase of the project. To help software practitioners in assessing the costs of software defects and optimizing allocation of resources, Hamid and Madnick proposed several models that can integrates different sectors of the software team such as manpower allocation, testing, and coding. These models illustrated different aspects of software engineering such as reducing defects and errors in software development, importance of early detection errors in a software project, and optimizing allocation of resources. Madachy in his book provided simplified versions of these models in his book []. 

_The goal of this project is to help software engineering researchers to analyze the Integrated Project Model Defect Flow Chain proposed by Abdel-Hamid and Madnick, by implementing the model, and optimizing the model using a standard optimizer_.  

We state our contributions as following: 
* A modular, extendible implementation of the Integrated Project Model Defect Flow Chain * An implementation that integrates a standard optimizer with the Integrated Project Model Defect Chain to facilitate further analysis 
Rest of the report is organized as follows Section II describes necessary background information, and related work. In Section III we state the assumptions of our project. Section IV illustrates our implementation of the model, and the optimizer. Section V describes the methodology of the project. In Section VI we explain our findings. Section VII discusses the threats to validity for the project. In Section VIII we state the future directions of the project. Finally we conclude our report in Section IX.     

## Background and Related Work 
### Background 

Storn and Price invented differential evolution (DE) to generate optimal solutions without making any assumption about the problem space. DE does not guarantee that it will always find an optimal solution. Researchers have successfully used different variants of DE to solve optimization problems in different domains such as, grid computing[], computational electro magnetics [], and software engineering []. 

Abdel-Hamid and Madnick proposed the integrated defect model that illustrates the interaction between different teams inside a software organization team namely the QA team, testing team, and the personnel allocation sector. Madachy in his book proposed a simplified version of Abdel-Hamid and Madnick’s proposed model and termed it as the ‘Integrated Project Model Defect Flow Chains (IPMDFC)’. Figure X shows IPMDFC. According to Figure X, flow that leads to error generation, detection, and correction. In contrast to the model proposed by Abdel-Hamid and Madnick, the flow chains are simplified. The model considers two types of errors namely active, and passive. According to Madachy, active errors can contribute to other errors, but passive errors do not contribute to other errors. Madachy considers all design errors to be active errors, and coding errors may be either active or passive. 

As shown in Figure X, there are two parts of the whole model. The ‘top’ part has four stocks namely, ‘Potentially Detectable Errors’, ‘Escaped Errors’, ‘Detected Errors’, and ‘Reworked Errors’. The ‘bottom’ part has two stocks namely ‘Undetected Active Errors’, and ‘Undetected Passive Errors’. Madachy does not show any connection between the ‘top’ and the ‘bottom’ part, and thus we had to assume the connection as described in the next section. 

### Related Work 

Our project is closely related to applications of DE is different domains of science and engineering, as well as research studies that have investigated software quality and software defects. 

Nasar and Johri used differential evolution to find optimal values for software testing effort allocation. The authors focused their analysis on  resources  for  testing and  debugging  that involved three variables namely, failure detection professionals, failure rectification professionals, and computer time used to measure cost for testing effort. 
## Assumptions 
## Implementation 
## Methodology 
## Results 
## Threats to Validity 
## Future Work 
## Conclusion 

## References 
[1] T. Abdel-Hamid, and S. Madnick, "Software Project Dynamics: An Integrated Approach", Prentice Hall, NJ, USA, 1990 

[2] R. Becerra, R. Sagarna, and X. Yao, "An evaluation of Differential Evolution in software test data generation," in Proceedings of IEEE Congress on Evolutionary Computation (CEC), Vienna, Austria, pages 2850-2857, May, 2009

[3] C. Jones, "Software Assessments, Benchmarks, and Best Practices", 1st Edition, Addison-Wesley Professional, MA, USA, 2000

[4] T. Liao, "Two Hybrid Differential Evolution Algorithms for Engineering Design Optimization", in Applied Soft Computing, vol. 10, no. 4, pages 1188-1199, September 2010

[5] R. Madachy, "Software Process Dynamics", Wiley Interscience, Wiley & Sons, NJ, USA, 2008

[6] A. Meneely, L., W. Snipes, and J. Osborne, "Predicting Failures With Developer Networks and Social Network Analysis", in Proceedings of the 16th ACM SIGSOFT International Symposium on Foundations of Software Engineering, 2008. 

[7] N. Nagappan, T. Ball, and A. Zeller, "Mining Metrics to Predict Component Failures", in Proceedings of the 28th international conference on Software engineering (ICSE '06), pages 452-461, 2006. 

[8] M. Nasar, and P. Johri, "A Differential Evolution Approach for Software Testing Effort Allocation", in Journal of Industrial 
and Intelligent Information vol. 1, no. 2, June, 2013 

[9] Rocca, P.; Oliveri, G.; Massa, A., "Differential Evolution as Applied to Electromagnetics," in Antennas and Propagation Magazine, IEEE , vol.53, no.1, pp.38-49, Feb. 2011

[10] R. Storn, and K. Price, "Differential Evolution: A Simple and Efficient Heuristic for global Optimization over Continuous Spaces", in Journal of Global Optimization, vol. 11, no. 4, pages 341-359, December, 1997 

[11] A. Talukder, M. Kirley, and R. Buyya, "Multiobjective Differential Evolution for Scheduling Workflow Applications on Global Grids", in Journal of Conncurrency & Computation, pages 1742-1756 vol. 21 no. 13, September 2009  