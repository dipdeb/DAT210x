import pandas as pd
import matplotlib.pyplot as plt

#
# TODO: Load up the Seeds Dataset into a Dataframe
# It's located at 'Datasets/wheat.data'
# 
# .. your code here ..
df = pd.read_csv('/home/dipanjan/DAT210x/Module3/Datasets/wheat.data', index_col = 0)


#
# TODO: Drop the 'id' feature, if you included it as a feature
# (Hint: You shouldn't have)
# 
# .. your code here ..
s1 = df[['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry', 'groove', 'wheat_type']]

#
# TODO: Compute the correlation matrix of your dataframe
# 
# .. your code here ..
#print(s1.corr())

#
# TODO: Graph the correlation matrix using imshow or matshow
# 
# .. your code here ..
plt.imshow(df.corr(), cmap=plt.cm.Blues, interpolation='nearest')
plt.colorbar()

tick_marks = [i for i in range(len(df.columns))]
plt.xticks(tick_marks, df.columns, rotation='vertical')
plt.yticks(tick_marks, df.columns)


