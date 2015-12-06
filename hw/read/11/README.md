#Reading Assignment # 11 
 
### Summary of *Method-Level Bug Prediction* [1]

#### Download Link 
http://dl.acm.org/citation.cfm?id=2372285

#### Keywords	 
* ii1: Bug Prediction : This term refers to the ability to predict a future bug by building a model using the historical metrics, which are mined from version histories of software modules.
* ii2: Fine-grained Prediction: This term refers to the use of method-level details. Here, the author computes source code metrics at the method level along with change metrics to do fine-grained prediction
* ii3: Fine-grained source code changes: It refers to the code changes happening in the source code at the fine-grained level of methods as compared to changes observed at the file-level or the package-level.
* ii4: Code Metrics:They are metrics which are directly computed from the source code itself. There are two traditional suites of code metrics : CK metrics and a SCM, which is a set of metrics directly computed at the method level. They are used by author to generate bug prediction models.

#### Key Points
* iii1: Related Work: The paper says that bug prediction has been widely studied and bug prediction models  have been built using bug-fix information. Bug prediction has been done using file-level and package-level and researchers have been successful in locating files containing bugs. However, there has been no work on predicting bugs at the method level.  
* iii2: Motivational Statements: Although a lot of previous work has been done on bug prediction using file-level and package-level historical metrics, there is a need to do bug prediction at a fine-grained level such as method level. The authors observe that although it is helpful to locate the file containing the bugs, most of the times such files are huge and complex in size and hence are easily classifed as bug-containing file. However, it takes a lot of manual effort for the developer to identify the exact area containing the bug and thus becomes time consuming and cumbersome. Also, there is a risk of inferential fallacy when transferring empirical findings from an aggregated level. This paper hopes to save manual inspection steps and significantly improve testing effort allocation.
* iii3: Study Instruments: The authors collected the dataset consisting of code, change and bug metrics for 21 software sub-systems. They used source code metrics and change metrics to build bug prediction models.The bug data was obtained from bug tracking systems such as Bugzilla and the code change is linked to bugs through the bug ids found in the commit message of each bug fix.
* iii4: New Results: The experiments performed on 21 Java open-source systems show that the prediction models reach a precision and recall of 84% and 88%, respectively. Furthermore, results indicate that change metrics significantly outperfom source code metrics.

#### Suggestions for Improvement 
* iv1: The authors used 21 software projects , all of which are java-based. Although the methodology seems to be generic and reproducible, it would further strengthen the case if instead of doing 21 projects, author had chosen say 10 java projects and 10 projects from any other language.
* iv2: Random forest being an ensemble prediction algorithm , works well for bug prediction as observed in previous studies on bug prediction. It would be great if authors could also try other models and confirm that random forest indeed works better in method-level prediction as well. This would further strengthen the case for future researchers.
* iv3: The author assumes that method bodies are not large and complex and it would still not take significant amount of time to localize the area containing the bug. Future research may be possible to identify blocks of code that contain bug within a method.
* iv4: Although random forest modelling is quite robust, they could have used other models and compared the results. 

#### Connection to the Initial Paper
Our selected initial paper titled *Ecological Inference in Empirical Software Engineering [2]* provided a conceptual framework on how prediction models can vary if metrics that are collected at aggregated with that of metrics collected at non-aggregated level. The "Ecological Inference in Empirical Software Engineering" paper makes use of the conclusion from "Benchmarking Classification Models.." paper - that simple statistic measures like TPR, FPR do not work well in a software defect prediction context as it is possible for two groups to use the same model on same data set and yet come with different results just because they had different threshold values. So the authors use ROC and statistical testing methods in their experiment to model defects. The authors of this paper use this information and argue that method-level fine-grained changed metrics give interesting bug-prediction models which yield better results as compared to file-level or package-level metrics or method-level source code metrics. 

####Reference
[1] Emanuel Giger, Marco D'Ambros, Martin Pinzger and Herald C. Gall. Method-Level Bug Prediction. In Proceeding ESEM '12 Proceedings of the ACM-IEEE international symposium on Empirical software engineering and measurement Pages 171-180 
[2] D. Posnett, V. Filkov, and P. Devanbu. Ecological inference in empirical software engineering. In Proceedings of the 2011 26th IEEE/ACM Inter- national Conference on Automated Software Engineering, pages 362–371. IEEE Computer Society, 2011. 

