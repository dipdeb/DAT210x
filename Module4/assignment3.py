#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import assignment2_helper as helper

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


# Do * NOT * alter this line, until instructed!
#scaleFeatures = False
scaleFeatures = True


# TODO: Load up the dataset and remove any and all
# Rows that have a nan. You should be a pro at this
# by now ;-)
#
# QUESTION: Should the id column be included as a
# feature?
#
# .. your code here ..
df = pd.read_csv('/home/dipanjan/DAT210x/Module4/Datasets/kidney_disease.csv');
df = df.dropna()                       

labels = ['red' if i=='ckd' else 'green' for i in df.classification]

#df = df.drop(labels=['id', 'classification', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'], axis=1)
df = df.drop(labels=['id', 'classification'], axis=1)
df.dtypes

df['pcv'] = pd.to_numeric(df['pcv'], errors='coerce')
df['rc'] = pd.to_numeric(df['rc'], errors='coerce')
df['wc'] = pd.to_numeric(df['wc'], errors='coerce')
df['rbc'] = pd.to_numeric(df['rbc'], errors='coerce')
df['pc'] = pd.to_numeric(df['pc'], errors='coerce')
df['pcc'] = pd.to_numeric(df['pcc'], errors='coerce')
df['ba'] = pd.to_numeric(df['ba'], errors='coerce')
df['rc'] = pd.to_numeric(df['rc'], errors='coerce')
df['htn'] = pd.to_numeric(df['htn'], errors='coerce')
df['dm'] = pd.to_numeric(df['dm'], errors='coerce')
df['cad'] = pd.to_numeric(df['cad'], errors='coerce')
df['appet'] = pd.to_numeric(df['appet'], errors='coerce')
df['pe'] = pd.to_numeric(df['pe'], errors='coerce')
df['ane'] = pd.to_numeric(df['ane'], errors='coerce')


df = pd.get_dummies(df, columns=['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane'])

if scaleFeatures: df = helper.scaleFeatures(df)



# TODO: Run PCA on your dataset and reduce it to 2 components
# Ensure your PCA instance is saved in a variable called 'pca',
# and that the results of your transformation are saved in 'T'.
#
# .. your code here ..
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(df)
T = pca.transform(df)

# Plot the transformed data as a scatter plot. Recall that transforming
# the data will result in a NumPy NDArray. You can either use MatPlotLib
# to graph it directly, or you can convert it to DataFrame and have pandas
# do it for you.
#
# Since we've already demonstrated how to plot directly with MatPlotLib in
# Module4/assignment1.py, this time we'll convert to a Pandas Dataframe.
#
# Since we transformed via PCA, we no longer have column names. We know we
# are in P.C. space, so we'll just define the coordinates accordingly:
ax = helper.drawVectors(T, pca.components_, df.columns.values, plt, scaleFeatures)
T = pd.DataFrame(T)
T.columns = ['component1', 'component2']
T.plot.scatter(x='component1', y='component2', marker='o', c=labels, alpha=0.75, ax=ax)
plt.show()
