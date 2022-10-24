from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from blend_matrix import process_matrix

##should be a function that recives an image
##divided in various small functions
##trabalho para a carolina do futuro
im = Image.open("dog.png")
w, h = im.size
plt.imshow(im)
plt.show()

##should be one function
pix = list(im.getdata()) ##list of pixels
pix_matrix = [pix[n:n+w] for n in range(0, w*h, w)]


matrix_r = [] 
matrix_g = [] 
matrix_b = [] 
matrix_a = []

for row in pix_matrix:
    row_r = []
    row_g = []
    row_b = []
    row_a = []
    for elem in row:
        row_r.append(elem[0])
        row_g.append(elem[1])
        row_b.append(elem[2])
        row_a.append(elem[3])
    matrix_r.append(row_r)
    matrix_g.append(row_g)
    matrix_b.append(row_b)
    matrix_a.append(row_a)


##should be a map
blended_r = process_matrix(matrix_r)
blended_g = process_matrix(matrix_g)
blended_b = process_matrix(matrix_b)
blended_a = process_matrix(matrix_a)

for _ in range(20):
    blended_r = process_matrix(blended_r)
    blended_g = process_matrix(blended_g)
    blended_b = process_matrix(blended_b)
    blended_a = process_matrix(blended_a)
    
##another function
blended_matrix = []
for row_index, row in enumerate(blended_r):
    blended_row = []
    for column_index, elem in enumerate(row):
        ##could be better written
        blended_elem = []
        blended_elem.append(blended_r[row_index][column_index])
        blended_elem.append(blended_g[row_index][column_index])
        blended_elem.append(blended_b[row_index][column_index])
        blended_elem.append(blended_a[row_index][column_index])
        blended_row.append(blended_elem)
    blended_matrix.append(blended_row)


##we should have the rgba matrix of the blended image at this point
blended_image = Image.fromarray(np.array(blended_matrix, dtype=np.uint8), 'RGBA')

plt.imshow(blended_image)
plt.show()

