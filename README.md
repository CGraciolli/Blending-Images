# Blending-Images

## Objective
We want to blend images, so their edges are smoother.

## Strategy
In order to do so, we want to be able to harmonize each pixel to the other pixels surrounding it.  
(Example with pixel images)

## Implementation
* First we define a function **process_matrix** that is given a matrix with numerical values, and returns a new matrix.
The new matrix has in the position (i, j) the average of the element (i, j) of the original matrix and it's neighbors.  
(image illustrating it)  
  
* Now we use this matrix to harmozine pixels in images to the surrounding pixels.  We implement it in three different ways:

1. We create a randomly generated matrix and use it to generate a heatmap using **Seaborn**. 
Then we use **process_matrix** in the randomly generated matrix and create a smoother heatmap using the resulting matrix.
![original_heatmp](https://user-images.githubusercontent.com/112963325/197737190-a1461a5e-7037-4d91-b1e1-92f088eeec45.png) 
![heatmap_blended](https://user-images.githubusercontent.com/112963325/197737224-6df77891-a2cc-4efc-8b1e-292ea163347f.png)
(images should be side by side)

2. We create a imagem by randomly generating three matrixes, each representing one color in the RGB representation. 
Then we use **Astropy** to create an image using this three matrixes. 
Using the same strategy as before, we harmonize each RGB matrix using **process_matrix** and create a blended image with this new matrixes.  
![original_rgb](https://user-images.githubusercontent.com/112963325/197739663-c7301feb-7941-45e4-9bc2-ccf9afb3e800.png)
![rgb_blended](https://user-images.githubusercontent.com/112963325/197739679-a383dbc3-bf7f-4c89-8e62-26eb1fe5ad01.png)

3.Now we are prepared to smooth an image given to us. We use **Pillow** to open an image and extract its RGBA matrix. 
Now we divide the RGBA matrix in four separated matrixes and use **process_matrix** in each. 
After we combine this matrix in a RGBA matrix that **Pillow** can use to generate a new image.  
![dog](https://user-images.githubusercontent.com/112963325/197740607-0e67a066-93bf-4c11-bcd6-f96b9ed27831.png)
![dog_blended](https://user-images.githubusercontent.com/112963325/197740608-8d2c1484-ef52-45dc-a323-bac811a81d8f.png)


