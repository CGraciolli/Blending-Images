import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
from blend_matrix import process_matrix

rng = np.random.default_rng() ##random number generator
image_r = rng.random((50, 50)) ##matrix 50x50
image_g = rng.random((50, 50)) ##matrix 50x50
image_b = rng.random((50, 50)) ##matrix 50x50

##creates an image from 3 matrixes representing red, green and blue
image = make_lupton_rgb(image_r, image_g, image_b, stretch = 0.1) 


plt.imshow(image)
plt.show()

blended_r = process_matrix(image_r)
blended_g = process_matrix(image_g)
blended_b = process_matrix(image_b)
blended_img = make_lupton_rgb(blended_r, blended_g, blended_b, stretch = 0.1) 

plt.imshow(blended_img)
plt.show()

