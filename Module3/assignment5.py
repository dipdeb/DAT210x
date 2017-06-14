#
# This code is intentionally missing!
# Read the directions on the course lab page!
#
from pandas.tools.plotting import andrews_curves
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

wheat = pd.read_csv('/home/dipanjan/DAT210x/Module3/Datasets/wheat.data', index_col=0)

s1 = wheat[['compactness', 'length', 'width', 'asymmetry', 'groove', 'wheat_type']]

plt.figure()
andrews_curves(s1, 'wheat_type')

s2 = wheat[['area', 'perimeter', 'compactness', 'length', 'width', 'asymmetry', 'groove', 'wheat_type']]
plt.figure()
andrews_curves(s2, 'wheat_type')
plt.show()