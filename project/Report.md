# Implementing and Analyzing the  Integrated Project Model Defect Flow Chain 

## Team Members 
* ### Akond Rahman (aarahman@ncsu.edu)
* ### Bennett Nyarron (bynarron@ncsu.edu) 
* ### Manish Singh (mrsingh@ncsu.edu)


## Date: December 06, 2015



## Abstract 

Software teams spend a lot of effort in preemptively reducing errors and fixing the errors that have been generated as part of the development process. Software models that illustrate and predict the resources needed to reduce development errors and predict estimation rate to reduce development errors can be of great help to software practitioners. _The goal of this project is to help software engineering researchers to analyze the Integrated Project Model Defect Flow Chain proposed by Abdel-Hamid and Madnick, by implementing the model, and optimizing the model using a standard optimizer_. In this project we implemented a standard software model that accounts for software development and calculates the amount of development errors with certain assumptions, and considering a subset of the full development resource inputs. To optimize the development resources needed to reduce development errors we use the Differential Evoluion Algorithm (DE). We find that DE can minimize on the Integrated Project Model Defect Flow Chain. We observe that a subset of the complete list of development resource inputs is required to provide an optimal solution for reducing errors for this software model of interest. We also observe the necessity of real world software project resource inputs for optimal output.  

## Introduction 

The impact of software defects on software product delivery is significant and a well-studied topic amongst software practitioners and academicians. According to a study conducted by NASA Johnson Space Center, the cost of fixing software defects increases exponentially in the latter stages of the project . Jones, in his book [3], showed that cost of fixing a defect increases significantly during testing and again during the maintenance phase of the project. To help software practitioners in assessing the costs of software defects and optimizing allocation of resources, Hamid and Madnick [1] proposed several models that can integrates different sectors of the software team such as manpower allocation, testing, and coding. These models illustrated different aspects of software engineering such as reducing defects and errors in software development, importance of early detection errors in a software project, and optimizing allocation of resources. Madachy in his book provided simplified versions of these models in his book [5]. 

_The goal of this project is to help software engineering researchers to analyze the Integrated Project Model Defect Flow Chain proposed by Abdel-Hamid and Madnick, by implementing the model, and optimizing the model using a standard optimizer_.  

We state our contributions as following: 

* A modular, extendible implementation of the Integrated Project Model Defect Flow Chain 
* An implementation that integrates a standard optimizer with the Integrated Project Model Defect Chain to facilitate further analysis 

The rest of the report is organized as follows: Section II describes necessary background information, and related work; Section III states the assumptions of our project; Section IV illustrates our implementation of the model, and the optimizer; Section V describes the methodology of the project; Section VI reports our findings; Section VII discusses threats to validity for the project; Section VIII states future directions of the project. Finally, we conclude our report in Section IX.     

## Background and Related Work 

In this section we provide background information and prior academic work related to our project. 
### Background 

Storn and Price [11] invented differential evolution (DE) to generate optimal solutions without making any assumption about the problem space. DE does not guarantee that it will always find an optimal solution. Researchers have successfully used different variants of DE to solve optimization problems in different domains such as, grid computing [12], computational electro-magnetics [10], and software engineering [2, 9]. 

Differential Evolution solves the problem of over population in the forntier by replacing the worse solutions with better ones. For generating new candidate solutions it performs extrapolation by picking three members from the frontier. At some probability the extrapolation will be performed. Storn and Price's recommended size for a frontier was `number of objectives * 10`, however researchers have proposed and implemented different engineering decisions that have led to different variants of DE. In our project we followed Storn and Price's recommendation for frontier size.  


Abdel-Hamid and Madnick [1] proposed the integrated defect model that illustrates the interaction between different teams inside a software organization team namely the QA team, testing team, and the personnel allocation sector. Madachy in his book [5] proposed a simplified version of Abdel-Hamid and Madnick’s proposed model and termed it as the _Integrated Project Model Defect Flow Chains (IPMDFC)_. Figure 1 shows IPMDFC. In contrast to the model proposed by Abdel-Hamid and Madnick, the flow chains are simplified. The model considers two types of errors namely _active_, and _passive_. According to Madachy, active errors can contribute to other errors, while passive errors do not. Madachy considers all design errors to be active errors, though coding errors may be either active or passive. 

As shown in Figure 1, there are two parts of the whole model. The _top_ part has four stocks: (1) _Potentially Detectable Errors_; (2) _Escaped Errors_; (3) _Detected Errors_; and (4)  _Reworked Errors_. The _bottom_ part has two stocks: (1) _Undetected Active Errors_, (2) and _Undetected Passive Errors_. Madachy does not explicitly show any connection between the _top_ and the _bottom_ parts, and thus we had to assume the connection as described in the next section.

![IPMDFC](output/IPMDFC.png?raw=true=100x80)
Figure 1: Integrated Project Model Defect Flow Chains  

### Related Work 

Our project is closely related to applications of DE in different domains of science and engineering, as well as research studies that have investigated software quality and software defects. 

Nasar and Johri [9] used differential evolution to find optimal values for software testing effort allocation. The authors focused their analysis on resources  for  testing and  debugging  that involved three variables, namely failure detection professionals, failure rectification professionals, and computer time used to measure cost for testing effort.

Meneely et al. [7] inferred developer dependencies from a software repository 
and created a social network analysis to predict software failures. The authors of this paper performed a holistic approach where social network analysis was performed on one level.     

Nagappan et al. [8] mined different file level metrics such as module metrics, per-function metrics, and per-class metrics to predict software failures for five software project repositories. Their work, however, did not include contextual factors such as software development rate, different multipliers, and error generation rate for predicting software failures.  

Becerra et al. [2] applied DE to the automated generation of a test suite that consists a set of test inputs in order to achieve 100% branch coverage. The authors also compared the performance empirically with _Breeder Genetic Algorithm (BGA)_, an algorithm that also has been used in real world applications such as optimizing parcel distribution and impulse filtering. The authors suggested that DE is sensitive to the crossover factor that they referred to as the _differential constant for mutation_. 

Rocca et al. [10] conducted a survey on use of different variants of DE in computational electromagnetics. They studied 70 academic papers between 2000 and 2009 and found that _DE/best/1/bin_ was the most used variant of DE used in the domain of computational electromagnetics. 

Talukder et al. [12] used DE to optimize schedulers in grid computing. The authors studied two parameters _execution time_, and _data transmission time_ through simulation. The authors claimed DE performs better that the _Pareto-archived Evolutionary Strategy (PAES)_ algorithm for this particular problem. 

Liao [4] analyzed how two hybrid approaches of DE compare to the classical version of DE in the context of an engineering design problem. In the first hybrid approach, random walk is incorporated the classical version of DE. In the second, he included harmony search to the basic differential algorithm. Liao studied 14 engineering design problems including non-linear programming problems, manufacturing design problem, and non-linear chemical engineering problems. For all the 14 engineering design problems the two hybrid approaches outperformed the classical DE in terms of convergence rate.

Our work focuses on implementing IPMDFC proposed by Madachy, and running the classical version of Differential Evolution to optimize two objectives related to the model.

  


## Assumptions 

To implement the model we use the concepts of _stock_, _flow_, and _auxiliary_ that are defined below: 

* A flow is an entity that contributes to a stock over time. There are two types of flows, namely inflows and outflows. Inflows work as an aggregator to a stock, whereas outflows work as a depletory for a stock. Usually, flows are measured for a certain period of time.
* A stock is the entity that aggregates flows over time. Stocks are made larger over time by inflows and decreased by outflows. 
* An auxiliary is an entity that is used to hold input values or intermediates. In our implementation, we use auxiliaries as input to flows. The list of auxiliaries, flows, and stocks are present in Table I. For the remainder of the report, we will refer to the auxiliaries and flows by their respective truncated names (see table), and stocks by their full names. 

 
Table I: List of Auxiliaries, Flows, and Stocks in IPMDFC


|Auxiliaries   | Flows   | Stocks   | 
|-----|-----|-----|
|MultiplierSchedulePressure, MultiplierWorkforce, NominalError, SoftwareDevelopmentRate, PotentialErrorDetectRate, QARate, AverageErrorPerTask, ActualReworkMP, DailyMPRework, TimeToSmooth, MultiplierToRegeneration, ActiveErrorDensity, TestingRate, PassiveErrorDensity, FractionEscapingErrors, ActiveErrorsRetiringFraction, BadFixGenerationRate    |  ErrorGenerationRate, ErrorDetectionRate, ErrorEscapeRate, ReworkRate, ActiveErrorRegenerationRate, ActiveErrorDetectAndCorrectRate, ActiveErrorRetirementRate, PassiveErrorDetectAndCorrectRate, PassiveErrorGenerationRate, ActiveErrorGenerationRate |   PotentiallyDetectableError, DetectedError, EscapedError, ReworkedError, UndetectedActiveErrors, UndetectedPassiveErrors|



* We only considered the auxiliaries that were mentioned in Madachy’s book. The model itself is part of a larger model that included models for different sectors, namely testing, personnel allocation, and coding.  
* We assumed the connection between the detected part and the undetected part based on notations from Abdel-Hamid and Madnick [1]. We assume that flow _ErrorEscapeRate_ contributes to the auxiliary _FractionEscapingErrors_, and flow _ReworkRate_ contributes to auxiliary _BadFixGenRate_. 


## Implementation 
We conduct the discussion of this section in two sub-sections. The first subsection provides the details on implementation of the IPMDFC. The next subsection describes the implementation of DE and how it is integrated to the model. 

### Implementation of IPMDFC
We implemented IPMDFC using the concepts of domain specific language. We used the object-oriented features of Python. We created classes for _Auxiliary_, _Flow_, and _Stock_ that inherit from the base class _ModelComponent_. _ModelComponent_ has two properties namely _curr_, and _name_. _Auxiliary_, _Flow_, and _Stock_ classes have setInput methods to set the values for the created objects. 

In our implementation auxiliary objects are treated as inputs and contribute to the flows directly. Each stock is filled by inflows and depleted by outflows. To determine the current value of state, the inflows, and state values from the previous step were added, and the outflaws were subtracted.  Our implementation is provided in _ModelExecAll.py_. This file has three methods namely _executeModelForBaseline_, _executeModelForDE_,and _executeModelAll_. 

* The method _executeModelAll_ is used to run the model separately for synthetic values; these synthetic values are provided as a dictionary for seven days. The implementation of the dictionary can be found in method _createAuxiliaries_All_ in _utility.py_.               

* The method _executeModelForBaseline_ is used to run the model separately to get baseline values to run DE on IPMDFC. All the auxiliaries are provided by the _giveAuxiliariesForBaseline_ method in utility.py.                
* The method _executeModelForDE_ is used to run the model separately to run DE on IPMDFC. The method takes four parameters namely _auxListParam_, _currStateParam_, _prevStateParam_, and _dt_. In our implementation dt is always set 1. _currStateParam_, and _prevStateParam_ are two state objects that keeps tarck of the current state and previous state.  

To facilitate the integration of DE on IPMDFC we used another file called _integrator.py_, and _models.py_. The purpose of models.py was to implement IPMDFC as an object that has a _lowerRange_, _upperRange_, _objectives_, and _decisions_. In this model we had 17 auxiliaries, so the number of decisions were 17. The number of objectives was two as we wanted DE to minimize on two stocks namely _Undetected Active Errors_, and _Undetected Passive Errors_.  

The method _runDE_ in integrator.py passes the object _IntegratedDefectModel_. DE later creates the necessary objects for _IntegratedDefectModel_. Our implementation of DE can be found in _de.py_. Our implementation can be used to maximize and minimize objectives. In our implementation we use DE to minimize the two objectives _Undetected Active Errors_, and _Undetected Passive Errors_.     


The class IntegratedDefectModel also has two methods: _check_, and _getobj_. 

* The method ‘check’ makes sure that the decision vector created by DE satisfies the constraints of IntegratedDefectModel. 

* The purpose of getobj is to run the model for certain number of times and calculate the values of the two stocks of interest. In our experiments we fix n=365 mimicking 365 days of one year. The constraints for IntegratedDefectModel are provided in a CSV file. The name of the constraints file, and the directory where it resides must be provided while running DE on IntegratedDefectModel.    

### Implementing DE 

To implement DE we use the concept called _normalized score_ that aggregates 
the objective scores and normalizes with respect to a baseline score. Our DE implementation generates solutions based on this normalized score for each candidates. To obtain the baseline we run IPMDFC for a fixed number of iterations. The obtained baseline scores is passed to our implementation of the DE algorithm. Our DE algorithm updates the scores of baseline by the score obtained from each candidate solution. Our implementation of DE performs minimization on the normalized scores. We followed Storn and Price's recommendation for frontier size (`18 * number of decisons`).     

### Integrating DE with IPMDFC

Finally, _main.py_ acts as a placeholder to put all the pieces together and perform all experiments. To perform a sample run a set of synthetic values we use the _runIntegrator_ method in main.py. To get baseline for IntegratedDefectModel we use _getBaselineForModel_ method in main.py. Finally, to use DE on InteratedDefectModel we set the following parameters: _runCount_, _constFlagForBaseline_, _deRunCount_, and _dirToWriteP_. 

* Parameter _runCount_ specifies the number of times the model will run. This is set to 365 to imitate 365 days for running the model. 

* If _constFlagForBaseline_ is set to True, then regression equations will be used to run the model. ‘dirToWriteP’ specifies the directory name where the constraint file resides.

* _constraintFileNameParam_ is used to set the name of the constraint file. Please note that _createConstraintFile_ is an optional method to create constraint files based to set different ranges for the auxiliaries. In our implementation we have not used this method. 

## Methodology 

To observe how DE performs on optimizing two objectives for our model of interest namely, _Undetected Active Errors_, and _Undetected Passive Errors_. To run the experiment we provide the following parameters: _constraintFileNameParam_, _constFlagForBaseline_, _dirToWriteP_, _runCount_, and _deRunCount_. For different experiments we use different configurations of the five parameters. In our experiment runCount was set to 365 for all our experiments. The parameters constraintFileNameParam, and dirToWriteP were used to set a file name, and directory that used to read the constraints for the model. In our experiments we wanted to minimize the two objectives. For each configuration of the experiment, we recorded the output values and recorded the duration time of the time taken to perform the experiment. We present our findings in the next section.       


## Results

We conduct our discussion in three categories: first we show the values of all the stocks for a sample run of IPMDFC. Then we provide empirical eveidence stating whether or not DE is providing better results in terms of optimization. Finally we provide our findings for the two experiemnts that we used. 

### Sample Run of IPMDFC 

To test our implemention of IPMDFC we created a set of auxiliaries and observed the values of all the stocks. In Table II we list the values of all auxiliaries that we used. Please note that all the following values are for test purpose. 
  
Table II: Values of Auxiliaries Used 

|Auxiliary Name   | Day-1   |  Day-2 | Day-3  | Day-4  | Day-5  | Day-6  | Day-7  |
|------------------------------|-----|-----|-----|-----|-----|-----|-----|
| MultiplierSchedPressure      | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| MultiplierWorkforce          | 0  | 1  | 1 | 2  | 1  | 10 | -1 | 
| NominalErr                   | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| SoftwareDevelopmentRate      | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| PotentialErrorDetectRate     | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| AvgErrorPerTask              | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| QARate                       | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| ActualReworkMP               | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| DailyMPRework                | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| FractionEscapingErrors	    | 0  | 3  | 3 | 6  | 3  | 30 | -3 |
| BadFixGenRate                | 0  | 3  | 3 | 6  | 3  | 30 | -3 |
| TimeToSmooth	                | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| MPRegen	                    |   0  | 1  | 1 | 2  | 1  | 10 | -1 |
| ActiveErrorDensity            |   0  | 1  | 1 | 2  | 1  | 10 | -1 |
| ActiveErrorsRetiringFraction  | 0  | 1  | 1 | 2  | 1  | 10 | -1 |
| TestingRate                   |  0  | 1  | 1 | 2  | 1  | 10 | -1 |
| PassiveErrorDensity           |  0  | 1  | 7 | 8  | 13  | 16 | 59 |

The output that we get for stocks are shown in Table III. 

Table III: Values of Stocks  

|Auxiliary Name   | Day-1   |  Day-2 | Day-3  | Day-4  | Day-5  | Day-6  | Day-7  |
|------------------------------|-----|-----|-----|-----|-----|-----|-----|
| PotentiallyDetectableError | 0  | 0  | 1 | 2  | 4  | 5 | 15 |
| EscapedError               | 0  | 0  | 2 | 4  | 8  | 10 | 30 | 
| DetectedErrors             | 0  | 0  | -1 | -2  | -4  | -5 | 15 |
| ReworkedErrors             | 0  | 0  | 2 | 4  | 8  | 10 | 30 |
| UndetectedActiveError      | 0  | 0  | 6 | 12 | 24 | 30 | 90 |
| UndetectedPassiveError     | 0  | 0  | 6 | 6  | 12  | 6 | 60 |

### Improvement by DE 

After verifying that our implementaion was correct we integrated IPMDFC with our DE 
implementation. We observed whether DE is minimizing the two objectives for our project. To observe that we logged the baseline maximum value for the two objectives along with the objective values after DE optimization. Figure 2 presents how the baseline values for the stock UndetectedActiveErrors compare with that of the optimized candidate generated by DE.   

![scores](output/compare_with_baseline.jpg?raw=true=50x40)
Figure 2: Comparing Objective Scores with Baseline.  

As we observe in Figure 2, the optimized value of the two objectives are lesser than the baseline values. We observe that the median value of UndetectedActiveErrors
remain less than 200 for different iterations. The median value for UndetectedPassiveErrors remain less than 2 for different iterations of DE. 
### Experiments  

Before explaining the results we first provide the experiment configurations. In the first experiment configuration that we label as Exp-1, we set deRunCount for 1, 10, 100, and 1000, and set _constFlagForBaseline_ as False. Please note that _deRunCount_ refrs to number fo iterations DE eill be running. Setting deRunCount to 1 will allow DE to run on the model for one iteration. In the same manner, setting deRunCount to 1000 will allow DE to run for 1000 iterations. Setting _constFlagForBaseline_ as False that enables the four auxiliaries _MultiplierSchedPressure_, _MultiplierWorkforce_, _ActiveErrorsRetiringFraction_, and _FractionEscapingErrors_ to set between any random number 0 & 1. This experiment was run 10 times to see if there is any noticeable difference for different iterations.  

In the second experiment configuration that we label as Exp-2, we set deRunCount for 1, 10, 100, and 1000, and set _constFlagForBaseline_ as False. Setting constFlagForBaseline as False that enables the five auxiliaries MultiplierSchedPressure, MPRegen, MultiplierWorkforce, ActiveErrorsRetiringFraction, and FractionEscapingErrors to use regression equations instead of any random number between 0 & 1. 

Table III: Regression Equations Used in Exp-2  

|Auxiliary Name                 | Regression Equation Used            |  
|-------------------------------|-------------------------------------|
| MultiplierWorkforce           | y = -x + 2                          | 
| FractionEscapingErrors        | y = -1.0286x^{2} -0.2283x + 1.0719  |   
| MPRegen                       | y = 0.0007x^{2} - 0.031x + 1.3099   | 
| ActiveErrorsRetiringFraction  | y = 0.0004e^{7.2984x}               | 
| MultiplierSchedPressure       | y = 0.2128x^{2} + 0.2955x + 0.9888  | 




As we obeserve in Figure 3, with respect to normalized score, the median normalized scores are lower for Exp-1, than that for Exp-2. We do not observe a lot of variation with respect to the median of normalized values for Exp-1, and Exp-2 individually. We also observe the median of the normalized scores are different between the two experiemnts, and use of regression equations has an effect.     

![scores](output/scores.png?raw=true=100x80)
Figure 3: Median of Normalized Scores Obtained for Exp-1, and Exp-2.  



From Figure 4 we observe that the experiment duration followed the same trend for both experiemnts. For both experiemnts the time to complete each experiment increases with the increase of iterations. The highest median experiment duration was recorded for 1000 iterations as expected. We also observe that Exp-2 is not strict enough to increase computation time compared to that of Exp-1.


![time](output/time.png?raw=true=100x80)
Figure 4: Median of Experiment Duration Obtained for Exp-1, and Exp-2.  
 
## Threats to Validity

We discuss the limitations of our study as following: 

* Use of synthetic values for the used auxiliaries 
* We did not consider all auxiliaries that are part of a bigger model 
* We did not consider the complete model 
* The equations used for auxiliaries are generated from regression using a sample of values that are less than 10 in size. 
* We ran the integrated model for 365 days that is equivalent to one year. In real world software projects tend to vary in duration usually in months, or years. 
* The base of our assumption that connects the top and bottom part of the model is based on the notations of Abdel-Hamid and Madnick’s book. We have not thoroughly verified this assumption.  
* In our project we considered only one differential algorithm that is DE. We did not include other genetic algorithms such as GALE, max walk sat or NSGA II.   
 
## Future Work 
We leave the following actions as scope for future work: 

* Future work can consider all auxiliaries in the model   
* Future work can implement the complete model that includes all the sectors of interest  
* Future work can verify the equations used for auxiliaries _MultiplierWorkforce_, _FractionEscapingErrors_, _MultiplierToRegeneration_, _MultiplierSchedulePressure_, and _ActiveErrorsRetiringFractions_ for real world values. 
* Future work can run the complete model, and the optimizer for real world software project duration and contextual factors. 
* Future work can perform analysis of the complete model and compare the findings with that of Madachy’s implementation available on Internet [6]. 
* Future work can include other genetic algorithms such as simulated annealing, max walk sat or NSGA II.

## Conclusion

IPMDFC is a software model that illustrates the flow chains of different software development factors namely software development rate, bad fix generation rate, and testing rate on different types of errors. In this project we implemented IPMDFC as a domain specific language using Python. Then we applied DE to find an optimized solution that will return the a set of values for the 17 auxiliaries when we are minimizing two stocks namely Undetected Active Errors, and Undetected Passive Errors. We suggest that our implementation can be used as a starting point for implementation of the complete model, as our implementation is modular, and extensible. The organization of the project also facilitates the scope of adding other genetic algorithms namely simulated annealing, max walk sat, and NSGAII. We observe that to make our implementation applicable to real-world software projects, future work should include all necessary auxiliaries, complete implementation of all relevant models, and real world project values for the auxiliaries. 

## Acknowledgement 

We earnestly thank course instructor Dr. Tim Menzies, and teaching assistant Rahul Krishna for giving us valuable advice in implementing the project.

## References 
[1] T. Abdel-Hamid, and S. Madnick, "Software Project Dynamics: An Integrated Approach", Prentice Hall, NJ, USA, 1990 

[2] R. Becerra, R. Sagarna, and X. Yao, "An evaluation of Differential Evolution in software test data generation," in Proceedings of IEEE Congress on Evolutionary Computation (CEC), Vienna, Austria, pages 2850-2857, May, 2009

[3] C. Jones, "Software Assessments, Benchmarks, and Best Practices", 1st Edition, Addison-Wesley Professional, MA, USA, 2000

[4] T. Liao, "Two Hybrid Differential Evolution Algorithms for Engineering Design Optimization", in Applied Soft Computing, vol. 10, no. 4, pages 1188-1199, September, 2010

[5] R. Madachy, "Software Process Dynamics", Wiley Interscience, Wiley & Sons, NJ, USA, 2008

[6] R. Madachy (2010, August), Software Process Dynamics [Online]. Available: http://csse.usc.edu/softwareprocessdynamics/models/integrated%20project.itm

[7] A. Meneely, L., W. Snipes, and J. Osborne, "Predicting Failures With Developer Networks and Social Network Analysis", in Proceedings of the 16th ACM SIGSOFT International Symposium on Foundations of Software Engineering, 2008. 

[8] N. Nagappan, T. Ball, and A. Zeller, "Mining Metrics to Predict Component Failures", in Proceedings of the 28th international conference on Software engineering (ICSE '06), pages 452-461, 2006. 

[9] M. Nasar, and P. Johri, "A Differential Evolution Approach for Software Testing Effort Allocation", in Journal of Industrial and Intelligent Information vol. 1, no. 2, June, 2013 

[10] P. Rocca, G. Oliveri, and A. Massa, "Differential Evolution as Applied to Electromagnetics," in IEEE Antennas and Propagation Magazine, vol.53, no.1, pages 38-49, February, 2011

[11] R. Storn, and K. Price, "Differential Evolution: A Simple and Efficient Heuristic for Global Optimization Over Continuous Spaces", in Journal of Global Optimization, vol. 11, no. 4, pages 341-359, December, 1997 

[12] A. Talukder, M. Kirley, and R. Buyya, "Multiobjective Differential Evolution for Scheduling Workflow Applications on Global Grids", in Journal of Conncurrency & Computation, pages 1742-1756 vol. 21 no. 13, September 2009  

