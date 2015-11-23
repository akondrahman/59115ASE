#Project - Integrated Defect Model

## Starting Date: October 30, 2015

#### Execution 
    output and tests: run *python main.py* 


#### Updates (Nov 05, 2015)
 * Implemented and tested _Potentially Detetable Errors_ with synthetic test values 
 * Implemented and tested _Escaped Errors_ with synthetic test values 
 * Implemented and tested _Detected Errors_ with synthetic test values 
 * Implemented and tested _Reworked Errors_ with synthetic test values
 * The relevant, four flows, and nine auxiliaries were also implemented  
 * Implemented test cases for the above four stocks 
 * Implemented and tested _Undetected Active Errors_ with synthetic test values 
 * The relevant, four flows, and seven auxiliaries were also implemented  
 * Implemented test cases for _Undetected Active Errors_
 * Refactored and re-arranged to facilitate top and bottom parts of the model to
 run them at the same time automatically  
 
#### Updates (Nov 20, 2015)
 * Refactored and re-arranged code to facilitate model integration with D.E. 
 * Finished setting up code for baseline 
 * Got baseline for the model for different runs: 1000, 10000, 100000, and 1000000 
 * Coded up model.py , now the model can be run as an object  
 * Ran D.E. for model with minimizing and maximizing goals. 
   
#### Output
* Model Output for Dummy Values 

![output](output/update_nov_17.png?raw=true=100x80)

* Baseline Output 

![output](output/baseline_nov_17.png?raw=true=100x80)

* Output : D.E min (all auxiliaries are between 0 & 1 )

![output](output/de_min.png?raw=true=100x80)

* Output : D.E max (all auxiliaries are between 0 & 1 )

![output](output/de_max.png?raw=true=100x80)


* Output : D.E min (11 auxiliairies are between 0 & 1, five use equations with three heuristics to handle infinite loop )

**For output, see `output/0_1_heuristic_de_min_output.txt`** 

* Output : D.E min (11 auxiliairies are between 0 & 2, five use equations with four heuristics to handle infinite loop )
_When we increase upper range from 0 to 2, we might get stuck in an infntie loop to satisfy all constraints. For example, the following text file shows how D.E. got stuck while running 100 times. An impossible to satisfy constraint was generated_

**For output, see `output/0_2_heuristic_de_min_output.txt`** 

**For corresponding constraints see `supplementary/0_2_mod_equ_constraints.csv`**

#### References
[1] Raymond J. Madachy. "Software Process Dynamics",  Wiley Interscience, 2007	

