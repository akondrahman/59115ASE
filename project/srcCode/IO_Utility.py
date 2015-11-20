# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:25:44 2015

@author: akond
"""



def writeDictToFile(dirParam, fileParam, dictP):
  import os   
  completeStrToWrite=""
  if not os.path.exists(dirParam):
    os.makedirs(dirParam)  
  fileParam = dirParam + "/" + fileParam + ".csv"
  fileToWrite = open( fileParam, 'w');
  lineStr =  "Index|Stock>" +","  + "Undetected Active Errors" + ","  + "Undetected Passive Errors" +","  
  fileToWrite.write(lineStr + "\n") 
  for key, values in dictP.items():
    lineStr = str(key) + ","  
    for item in values:    
        lineStr = lineStr + str(item) + ","
    lineStr = lineStr + "\n"  
    completeStrToWrite = completeStrToWrite + lineStr  
    lineStr="";
  fileToWrite.write(completeStrToWrite );
  fileToWrite.close()
  return "DONE !"

def getConstraintFromCSV(fileNameParam): 
    import csv   
    _vector_Lower_Range = [] 
    _vector_Upper_Range = []   

    fileToRead = open(fileNameParam, "rU") 
    try:
        fileReader = csv.reader(fileToRead, delimiter =',', dialect=csv.excel_tab)
        next(fileReader, None)
        for rowVar in fileReader: 
           _vector_Lower_Range.append(float(rowVar[1]))
           _vector_Upper_Range.append(float(rowVar[2]))
    finally: 
        fileToRead.close()
        
    return _vector_Lower_Range, _vector_Upper_Range
    
    
    
    
def createConstraintFiles(dirParam, fileParam, auxParam, lowListParam, highListParam):
  import os   
  completeStrToWrite = ""
  if not os.path.exists(dirParam):
    os.makedirs(dirParam)  
  fileParam = dirParam + "/" + fileParam + ".csv"
  fileToWrite = open( fileParam, 'w')
  lineStr =  "AuxNames>" +","  + "Low" + ","  + "High" +","  
  fileToWrite.write(lineStr + "\n")  
  if(len(lowListParam)==len(auxParam)) and (len(lowListParam)==len(highListParam)):
      for cnt in xrange(len(auxParam)):
          lineStr = lineStr + str(auxParam[cnt]) + "," + str(lowListParam[cnt]) + "," + str(highListParam[cnt]) + ","
          lineStr = lineStr + "\n"  
          completeStrToWrite = completeStrToWrite + lineStr  
          lineStr="";
      fileToWrite.write(completeStrToWrite )
      fileToWrite.close()
  return "DONE !"      
        