from pandas import read csv
from numpy import set printoptions
from sklearn.preprocessing import Binarizer
names=[’preg’,’plas’,’pres’,’skin’,’test’,’mass’,’pedi’,’age’,’class’]
dataframe= read csv(”D:/SEM 6/IoT Domain Analyst/pima-indians-diabetes.csv”)
dataframe.head()
array=dataframe.values
data binarizer=Binarizer(threshold=0.5).fit(array)
data binarized=data binarizer.transform(array)
set printoptions(precision=2)
print(” \nBinarized Data: \n”,data binarized[0:3])

from pandas import read csv
from numpy import set printoptions
from sklearn import preprocessing
names=[’preg’,’plas’,’pres’,’skin’,’test’,’mass’,’pedi’,’age’,’class’]
dataframe= read csv(”D:/SEM 6/IoT Domain Analyst/pima-indians-diabetes.csv”)
dataframe.head()
dataframe.info()
array=dataframe.values
data scaler=preprocessing.MinMaxScaler(feature range=(0,1))
data rescaled=data scaler.fit transform(array)
set printoptions(precision=2)
print(”\nScaledData: \n”,data rescaled[0:8])

from pandas import read csv
from numpy import set printoptions
from sklearn.preprocessing import Normalizer
names=[’preg’,’plas’,’pres’,’skin’,’test’,’mass’,’pedi’,’age’,’class’]
dataframe= read csv(”D:/SEM 6/IoT DomainAnalyst/pima-indians-diabetes.csv”)
dataframe.head()
array=dataframe.values
data normalizer=Normalizer(norm=’l2’).fit(array)
data normalized=data normalizer.transform(array)
set printoptions(precision=2)
print(”\nNormalizedData: \n”,data normalized[0:4])

from pandas import read csv
from numpy import set printoptions
from sklearn.preprocessing import StandardScaler
names=[’preg’,’plas’,’pres’,’skin’,’test’,’mass’,’pedi’,’age’,’class’]
dataframe= read csv(”D:/SEM 6/IoT Domain Analyst/pima-indians-diabetes.csv”)
dataframe.head()
array=dataframe.values
data scaler=StandardScaler().fit(array)
data rescaled=data scaler.transform(array)
set printoptions(precision=2) print(”\nStandardized Data: \n”,data rescaled[0:3])
