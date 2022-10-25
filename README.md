# Blending Images

## Objective
We want to blend a image, so its edges are smoother.

## Strategy
In order to do so, we want to be able to harmonize each pixel to the other pixels surrounding it.  
![pixel_comp](https://user-images.githubusercontent.com/112963325/197756584-1d3dd28e-5365-4c41-a0a4-d47e32042b0c.png)


## Implementation
* First we define a function **process_matrix** that is given a matrix with numerical values, and returns a new matrix.
The new matrix has in the position (i, j) the average of the element (i, j) of the original matrix and it's neighbors.  
Like in the image above, the original matrix has 5 in the position (1, 1) and its neighbors have values 2 and 2.   
So the new value will be (5+2+2)/3 = 3
  
* Now we use this matrix to harmozine pixels to the ones surrounding it.  We implement it in three different ways:

1. We create a randomly generated matrix and use it to generate a heatmap using **Seaborn**. 
Then we use **process_matrix** in the randomly generated matrix and create a smoother heatmap using the resulting matrix.
![heatmap](https://user-images.githubusercontent.com/112963325/197753937-26d81c0c-57a4-4b35-bb9a-cefd17866294.png)

2. We create a image by randomly generating three matrixes, each representing one color in the RGB representation. 
Then we use **Astropy** to create an image using this three matrixes. 
Using the same strategy as before, we harmonize each RGB matrix using **process_matrix** and create a smoother image with this new matrixes.  
![rgb](https://user-images.githubusercontent.com/112963325/197754402-260603e0-77c2-4eb7-8995-512cb4f73675.png)


3. Now we are ready to smooth any given image. We use **Pillow** to open the image and extract its RGBA matrix. 
We divide the RGBA matrix in four separated matrixes and use **process_matrix** in each. 
Then we combine this matrix in a RGBA matrix that **Pillow** can use to generate a new image.  
![dog_comp](https://user-images.githubusercontent.com/112963325/197754602-3b284bff-f849-4281-84c5-4db0196aaf2e.png)


