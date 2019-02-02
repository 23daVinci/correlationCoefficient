
import pandas as pd
import math

dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 1].values

X_sq = X*X
dat1 = pd.DataFrame({'X^2': X_sq})
dataset = dataset.join(dat1)

y_sq = y*y
dat2 = pd.DataFrame({'y^2': y_sq})
dataset = dataset.join(dat2)

Xy = X * y
dat3 = pd.DataFrame({'Xy': Xy})
dataset = dataset.join(dat3)

n = dataset['Salary'].count()
total = dataset.sum()

r1 = n * total['Xy'] -  total['YearsExperience'] * total['Salary']
r2 = (n * total['X^2'] - total['YearsExperience'])*(n * total['y^2'] - total['Salary'])

r3 = math.sqrt(r2)

r = r1/r3
    