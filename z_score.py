import numpy as np
import matplotlib.pyplot as plt 

import statistics

dataset = [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]

def Det_outliers(data):
    outliers = []
    threshold = 3 #3rd standard deviation
    mean = np.mean(data)
    std = np.std(data)

    for i in data:
     z_score = (i-mean)/std
     if np.abs(z_score)> threshold:
        outliers.append(i)
    
    return outliers

out = Det_outliers(dataset)
print(out)

#IQR
def IQR(data):
   np.sort(data)
   Q3 = np.percentile(data,75)
   Q1 = np.percentile(data,25)
   iqr = Q3 - Q1
   return iqr

iqr2 = IQR(dataset)

#lowerfence
def lowerfence(data,iqr2):
   Q1 = np.percentile(data,25)
   lf = Q1 - float(1.5* iqr2) 
   return lf
#upperfence
def upperfence(data,iqr2):
   Q3 = np.percentile(data,75)
   rf = Q3 + float(1.5* iqr2)
   return rf

lff = lowerfence(dataset,iqr2)
print(lff)

rff = upperfence(dataset,iqr2)
print(rff)

#dataset=sorted(dataset)
#q1,q3=np.percentile(dataset,[25,75])
#print(q1,q3)
### Find the lower fence and higher fence
#lower_fence=q1-(1.5*iqr)
#higher_fence=q3+(1.5* iqr)
#print(lower_fence,higher_fence)