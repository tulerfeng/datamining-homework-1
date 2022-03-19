import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt

def loader():  
    filepath = "dataset/winemag-data_first150k.csv" 
    df = pd.read_csv(filepath, header=0)
    return df

def cnt(str1,data1):
    print(data1[str1].value_cnts()[:10])

def find(str2,data2): 
    nullnum = nums.isnull().sum()
    print("null:%d"%(nullnum))
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
cnt("cntry",df)
cnt("points",df)
cnt("province",df)
cnt("region_1",df)
cnt("region_2",df)
cnt("variety",df)
cnt("winery",df)
find("points",df)
find("price",df)


'''
wine_dffs_province.value_counts().head(10).plot.bar()
plt.title('wine_dffs_province')
plt.show()
wine_dffs_region_1.value_counts().head(10).plot.bar()
plt.title('wine_dffs_region_1')
plt.show()
wine_dffs_region_2.value_counts().head(10).plot.bar()
plt.title('wine_dffs_region_2')
plt.show()
wine_dffs_taster_name.value_counts().head(10).plot.bar()
plt.title('wine_dffs_taster_name')
plt.show()
wine_dffs_variety.value_counts().head(10).plot.bar()
plt.title('wine_dffs_variety')
plt.show()
wine_dffs_winery.value_counts().head(10).plot.bar()
plt.title('wine_dffs_winery')
plt.show()
hist = dt1[str1].hist(bins=100)
plt.show()
dt2[str2].plot.box()
plt.show()
'''
