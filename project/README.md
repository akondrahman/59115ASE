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

* Output : D.E min (all auxilairies are between 0 & 1 )

![output](output/de_min.png?raw=true=100x80)

* Output : D.E max (all auxilairies are between 0 & 1 )

![output](output/de_max.png?raw=true=100x80)


#### References
[1] Raymond J. Madachy. "Software Process Dynamics",  Wiley Interscience, 2007	

