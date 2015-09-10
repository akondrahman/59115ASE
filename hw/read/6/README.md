#Reading Assignment # 6 
##Date September 10, 2015 
### Summary of *Think Locally, Act Globally: Improving Defect and Effort Prediction Models* [1] 

#### Keywords	 
* ii1: Global Model: A prediction model that is created by using all the features available in the dataset. 
* ii2: Local Model: A prediction model that is created by using a subset of the features available in the dataset. The other subsets are used in testing the predictive performance of the prediction model
* ii3: Goodness of Fit: A statistical testing mechanism that is used to test the predictive performance of any prediction model. Example of some popular *goodness of fit* tests include Pearson's test, chi-squared test, R-square measure (used in this paper) etc.
* ii4: Connecting Global and Local Models: The concept of using results from a local model and use it to build a better predictor at the Global level. Posnett et al. in their work [2] stated that the same prediction model can behave differently at different levels of the same software. Menzies et al. [3] stated that smaller subsets of a typical software engineering dataset can provide better insight with respect to prediction. In this paper, Bettenburg et al. uses these findings to build better global models.     

#### Key Points
* iii1: Motivational Statements: Empirical software engineering research has shown evidence that prediction models that work at aggregated and dis-aggregated levels differ in prediction performance. Similar studies have also shown the benefits of using prediction models applied at dis-aggregated levels. Te goal of replicate these findings and use them to create better prediction models that will help software engineering practitioners.    
* iii2: Study Instruments: 
  * PROMISE repository datasets:
    * Xalan 2.6
    * Luecene 2.4 
    * CHINA 
    * NasaCoc
  * Correlational Analysis, VIF Analysis, Cross Validation   
* iii3: Scripts: The complete set of tools, code are available at *http://sailhome.cs.queensu.ca/replication/local-vs-global/*
* iii4: Informative Visualizations
  * Which metrics show higher correlations 
  ![output](a.png?raw=true=150x100)  
  * Methodology picture that shows different steps of the study 
  ![output](b.png?raw=true=150x100)    

#### Suggestions for Improvement 
* iv1: The paper could have benefitted from an *informed* clustering technique such that *similar* dataset features are used to build *similar* local models     
* iv2: The selection criteria of independent and dependent variables for automated model selection are not mentioned clearly in the paper. An *informed* selection criteria that discovers the best set of independent variables could have fine-tuned the automated model selection process.      
* iv3: The paper uses *Multi-variate Adaptive Regression Splines (MARS)* models that are global models which take local prediction models in estimation. Use and comparison of other global models that take local models into consideration, could have made the paper stronger.  

#### Connection to the Initial Paper
The initial paper titled *Ecological Inference in Empirical Software Engineering [2]* provided evidence of varying prediction outcome when the same prediction model is applied on aggregated and dis-aggregated level. This paper uses the findings of our selected initial paper as a motivational aspect and tries to discover if the prediction results obtained at a dis-aggregated level, can be applied to get better prediction results at the aggregated level.  

####Reference
[1] N. Bettenburg, M. Nagappan, and A. E. Hassan. Think Locally, Act Globally: Improving Defect and Effort Prediction Models. in *Proceedings of the 9th IEEE Working Conference on Mining Software Repositories (MSR '12)*, IEEE Press, 2012. 

[2] D. Posnett, V. Filkov, and P. Devanbu. Ecological Inference in Empirical Software Engineering. in *Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering*, IEEE Computer Society, 2011. 

[3] T. Menzies, A. Butcher, A. Marcus, T. Zimmermann, and D. Cok. Local vs. global models for effort estimation and defect prediction. in *Proceedings of the 2011 26th IEEE/ACM International Conference on Automated Software Engineering (ASE '11)*, IEEE Computer Society, 2011.  