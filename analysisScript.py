# import requisite libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset
df = pd.read_csv('../datasets/911.csv')

# Que 01: Top 5 zip codes called in
zip = df['zip'].value_counts().head(5)

# Que 02: Top 5 townships called in
twp = df['twp'].value_counts().head(5)

# Que 03: Number of unique reasins called in
unique = df['title'].nunique()

# Que 04: Top specific reasons called in
df['specificReason'] = df['title'].apply(lambda title: title.split(':')[0])
reasons = df['specificReason'].value_counts()

#plot the count chart
#plt.hist(reasons, bins=5)
sns.countplot(x=specificReason, data=df)
