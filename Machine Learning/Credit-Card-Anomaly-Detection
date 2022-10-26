import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Bar plot for Transaction Class (Normal or Fraud) distribution based on
transaction frequency
RANDOM SEED = 42 #10% of entire Dataset
LABELS = [”Normal”, ”Fraud”]

data = pd.read csv(”C:/Users/ANSHUMAN PRATIK/Desktop/creditcard.csv”)
data.head()
data.info()
data.isnull().values.any()
count classes=pd.value counts(data[’Class’],sort=True) #Unique value
count classes.plot(kind=’bar’,rot=0)
plt.title(”Transaction Class distribution”)
plt.xticks(range(2),LABELS)
plt.xlabel(”Class”)
plt.ylabel(”Frequency”)
plt.show()
fraud = data[data[’Class’]==1]
normal = data[data[’Class’]==0]
fraud.Amount.describe()
normal.Amount.describe()
#Number of transaction Vs Amount and
Transaction amount Vs Time of transaction
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
f.suptitle(’Amount per transaction by Class’)
bins=50 #Transaction Interval
ax1.hist(fraud.Amount, bins = bins)
ax1.set title(’Fraud’)
ax2.hist(normal.Amount, bins = bins)
ax2.set title(’Normal’)
plt.xlabel(’Amount($)’)
plt.ylabel(’Number of Transactions’)
plt.xlim((0,20000))
plt.yscale(’log’)
plt.show();
f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
f.suptitle(’Time of transaction vs Amount by Class’)
ax1.scatter(fraud.Time, fraud.Amount)
ax1.set title(’Fraud’)
ax2.scatter(normal.Time, normal.Amount)
ax2.set title(’Normal’)

plt.xlabel(’Time (in Seconds)’)
plt.ylabel(’Amount’)
plt.show()
#Outlier fraction
data1 = data.sample(frac=0.1, random state=1)
data1.shape
data.shape
Fraud = data1[data1[’Class’] == 1]
Valid = data1[data1[’Class’] == 0]
#Ratio of fraudulent transaction to all valid Transaction
outlier fraction = len(Fraud) / float(len(Valid))
print(”Outlier Fraction:”,outlier fraction)
print(”Fraud Cases : ”.format(len(Fraud)))
print(”Valid Cases : ”.format(len(Valid)))
columns = data1.columns.tolist()
columns = [c for c in columns if c not in [”Class”]]
target = ”Class”
state = np.random.RandomState(42)
X = data1[columns]
Y = data1[target]
X outliers = state.uniform(low=0, high=1, size=(X.shape[0], X.shape[1]))
print(X.shape)
print(Y.shape)
