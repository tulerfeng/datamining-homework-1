import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


def loader():   
    filepath = "crime/records-for-2011.csv" 
    df = pd.read_csv(filepath, header=0)
    return df

def cnt(str1,data1):
    print(data1[str1].value_cnts()[:10])

def find(str2,data2): 
    nums = data2[str2]
    nullnum = nums.isnull().sum()
    nums = nums.dropna(axis = 0)
    Minimum = min(nums)
    Maximum = max(nums)
    Q1 = np.percentile(nums, 25)
    Median = np.median(nums)
    Q3 = np.percentile(nums, 75)
    print("Minimum:%d; Q1:%d; Median:%d; Q3:%d; Maximum:%d;"%(Minimum , Q1 , Median , Q3 , Maximum)) 

def f1(data1):    
    Data1 = data1.dropna(axis = 0)
    hist = Data1.hist(bins=100)  
    Data1.plot.box()
    plt.show()

def f2(data2):    
    Data2 = data2.fillna(data2.mode())
    hist2 = Data2.hist(bins=100) 
    Data2.plot.box()
    plt.show()

df = loader()

cnt("Agency",df)
cnt("Create Time",df)
cnt("Location",df)
cnt("Area Id",df)
cnt("Beat",df)
cnt("Priority",df)
cnt("Closed Time",df)
find("Area Id",df)
find("Area Id",df)


"""
dfff_Area_Id.value_counts().head(10).plot.bar()
plt.title('dfff_Area_Id')
plt.show()
dfff_Priority.value_counts().head(10).plot.bar()
plt.title('dfff_Priority')
plt.show()
dfff_Incident_Type_Id.value_counts().head(10).plot.bar()
plt.title('dfff_Incident_Type_Id')
plt.show()
"""