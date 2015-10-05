#Reading Assignment # 5 
 
### Summary of *Benchmarking Classification Models for Software Defect Prediction: A Proposed Framework and Novel Findings* [1]

#### Download Link 
http://ieeexplore.ieee.org.prox.lib.ncsu.edu/stamp/stamp.jsp?tp=&arnumber=4527256

#### Keywords	 
* ii1: Classification : This term refers to the categorization of data values into discrete classes. For example, a binary classification will have two categories or classes - "YES" and "NO"
* ii2: Software Defect Prediction: This term refers to the process of identifying error prone software modules by means of data mining techniques. This helps in efficient allocation of resources to high-risk software segments. 
* ii3: Data Mining: It is a process of analyzing data from various sources and analyzing and deriving useful insights and patterns from the data , that can be used to make better decision in future.
* ii4: Statistical Methods: Statistics deals with the collection, interpretation, presentation and analysis of data. It offers various methods to estimate and correct for any bias within a sample and data collection procedures.

#### Key Points
* iii1: Related Work: The paper discusses about the previous works which have used various models for software defect prediction. Classification has been a popular approach and various types of classifiers have been applied to predict defects, including statistical procedures, tree-based methods, neural networks and analogy-based approaches.
* iii2: Motivational Statements: Although a lot of previous work exists where numerous classification models have been used, the results about the superiority of one model or method over another or the usefulness of metric-based classification are not always consistent across different studies. There are various potential sources of bias : comparing classifiers over one or a small number of proprietary data sets, depending on accuracy indicators that are inappropriate for software defect prediction and cross-study comparisons and limited use of statistical testing procedures to secure empirical findings. Thus, there is a need for more reliable research procedures before we conclude the results of the comparative studies of software prediction models.
* iii3: Study Instruments: The paper proposes a framework for organizing comparative classification experiments in software defect prediction. The authors conduct a large-scale benchmark of 22 different classification models over 10 public-domain data sets from NASA Metrics Data (MDP) repository and the PROMISE repository. Comparisons are based on the area under the receiver operating characteristic curve (AUC). The authors argue that AUC represents the most informative and objective indicator of predictive accuracy within a benchmarking context. The authors then use statistical methods to measure statistical significance of the difference between the performance of the various classification models.
* iii4: New Results: The authors have established that AUC is the primary accuracy indicator for comparative studies in software defect prediction as it separates predictive performance from class and cost distributions, which are project-specific characteristics that may be unknown or subject to change. Another contribution was the usage of statistical testing procedures for comparing and contrasting classification models. Further, as per the results obtained, the predictive accuracy of the models did not differ significantly. Thus, the assessment and selection of a classification model should not be based on the predictive accuracy. Instead it should be based on other factors such as computation costs, efficiency, ease of use and comprehensibility.

#### Suggestions for Improvement 
* iv1: Although the authors mention that same studies using the same models can conclude different results based on the selection of threshold criteria, the authors themselves are using threshold criteria for AUC which can be debatable.
* iv2: The data set from NASA need not be representative enough unless someone runs similar experiment on other data sets and verifies the results.
* iv3: There are more than 22 classifier algorithms available and the authors have not covered all of them. Further, the author does not do any statistical proof that these 22 classifiers are representative of the entire domain of classifier algorithms available.
* iv4: The authors have specifically focused on classification problem in the data mining domain. The data mining problem involves several steps and stages. So, it is possible that if we do some previous step such as data preprocessing properly, it can improve the performance or prediction accuracy of a classification model and the results of two different models will no longer be "not statistically significant" - that is, there will be significant difference in the software defect prediction accuracy and the framework demonstrated by this paper would fail to hold ground.

#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [2]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. The "Ecological Inference in Empirical Software Engineering" paper makes use of the conclusion from "Benchmarking Classification Models.." paper - that simple statistic measures like TPR, FPR do not work well in a software defect prediction context as it is possible for two groups to use the same model on same data set and yet come with different results just because they had different threshold values. So the authors use ROC and statistical testing methods in their experiment to model defects. 

####Reference
[1] Stefan Lessmann, Bart Baesens, Christophe Mues, and Swantje Pietsch. Benchmarking Classification Models for Software Defect Prediction: A Proposed Framework and Novel Findings in *IEEE TRANSACTIONS ON SOFTWARE ENGINEERING, VOL.34, NO.4, JULY/AUGUST 2008*
[2] D. Posnett, V. Filkov, and P. Devanbu. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM Inter- national Conference on Automated Software Engineering, pages 362–371. IEEE Computer Society, 2011. 

