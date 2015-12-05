#Reading Assignment # 5 
 
### Summary of *Bug Prediction Based on Fine-Grained Module Histories* [1]

#### Download Link 
http://dl.acm.org/citation.cfm?id=2337247

#### Keywords	 
* ii1: Bug Prediction : This term refers to the ability to predict a future bug by building a model using the historical metrics, which are mined from version histories of software modules.
* ii2: Fine-grained Prediction: This term refers to the use of method-level details while using historical metrics, mined from version histories of software modules, to build a model for predicting bugs.
* ii3: Fine-grained Histories: It refers to the use of fine-grained metrics, by creating metadata or a structure which will store the history or change information at very fine grained level , for example, capturing details of a method level change instead of package level or file level change alone.
* ii4: Historical Metrics:They are metrics coming from various categories such as code-related metrics, process-related metrics, organizational metrics and geographical metrics for capturing version history in different categories.


#### Key Points
* iii1: Related Work: The paper says that bug prediction has been widely studied and recent findings show the usefulness of collecting historical metrics from software repositories for bug prediction models. Prediction models have been build using bug-fix information. Bug prediction has been done using file-level and package-level historical metrics and it has been observed that results from file-level metrics are more interesting. Fine-grained prediction has been a challenge because obtaining method histories from existing version control systems is a difficult problem.
* iii2: Motivational Statements: Although a lot of previous work has been done on bug prediction using file-level and package-level historical metrics, there is a need to do bug prediction at a fine-grained level such as method level. In ESEC/FSE 2011 conference, fine-grained prediction was selected as one of the future directions. Studies of fine-grained prediction are necessary because desirable results may be obtained when compared to coarse-grained prediction.
* iii3: Study Instruments: 
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

