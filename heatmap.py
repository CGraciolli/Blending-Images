import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from blend_matrix import process_matrix


max_val = 15
##creates a matrix of dimentions max_val x max_val
##each position has a randomly picked number between 0 and 9
matrix = np.random.randint(0, 10, size=(max_val, max_val)) 
x=pd.DataFrame(matrix)
sns.heatmap(x, annot=False) ## annot show the number or not
plt.show()

blended = process_matrix(matrix)
y = pd.DataFrame(blended)
sns.heatmap(y, annot=False)
plt.show()

twice_blended = process_matrix(blended)
z = pd.DataFrame(twice_blended)
sns.heatmap(z, annot=False)
plt.show()


