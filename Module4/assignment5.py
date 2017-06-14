import pandas as pd

from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import os


# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')

def Plot2D(T, title, x, y):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111)
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  
  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y], marker='.', c=colors, alpha=0.7)

def Plot3D(T, title, x, y, z):
  # This method picks a bunch of random samples (images in your case)
  # to plot onto the chart:
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.set_title(title)
  ax.set_xlabel('Component: {0}'.format(x))
  ax.set_ylabel('Component: {0}'.format(y))
  ax.set_zlabel('Component: {0}'.format(z))
  
  # It also plots the full scatter:
  ax.scatter(T[:,x],T[:,y],T[:,z], marker='.', c=colors, alpha=0.7)
  
#
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []
colors = []

#
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
path='Datasets/ALOI/32'
files = os.listdir(path)
    
for fname in files: 
   img = misc.imread(path+'/'+fname)
   samples.append((img[::2,::2]/255.0).reshape(-1))
   colors.append('b')
   #samples.append(img.reshape(-1))
df = pd.DataFrame(samples)   
   
#print(df)

from sklearn import manifold
iso = manifold.Isomap(n_components=3, n_neighbors=6)
T = iso.fit_transform(df)
Plot2D(T, 'Isomap 32 2D (n_neighbors=6)', 0, 1)
Plot3D(T, 'Isomap 32 3D (n_neighbors=6)', 0, 1, 2)

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
path='Datasets/ALOI/32i'
files = os.listdir(path)
for fname in files: 
   img = misc.imread(path+'/'+fname)
   samples.append((img[::2,::2]/255.0).reshape(-1))
   colors.append('r')
   
df_i = pd.DataFrame(samples)


#
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)


#
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
from sklearn import manifold
iso = manifold.Isomap(n_components=3, n_neighbors=6)
T = iso.fit_transform(df)



#
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
Plot2D(T, 'Isomap 32i 2D (n_neighbors=6)', 0, 1)



#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
Plot3D(T, 'Isomap 32i 3D (n_neighbors=6)', 0, 1, 2)


plt.show()

