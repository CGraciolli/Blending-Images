import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from blend_matrix import process_matrix

def create_random_matrix(dim):
    """
    creates a random square matrix of dimentions dim x dim
    each element of the matrix is a random number between 0 and 9
    """
    return np.random.randint(0, 10, size=(dim, dim))

def create_image(dim):
    """
    creates an image of dimentions dim x dim pixels
    each pixel is assigned a random number between 0 and 9
    displays the image with matplotlib.pyplot
    returns the matrix of the image
    """
    ##creates a matrix of dimentions dim x dim
    ##each position has a randomly picked number between 0 and 9
    matrix = create_random_matrix(dim)
    x=pd.DataFrame(matrix)
    sns.heatmap(x, annot=False, vmin=0, vmax=10) ## annot show the number or not
    plt.title("Original Heatmap")
    plt.axis("off")
    plt.show()
    return matrix

def create_blended_image(matrix):
    """
    recives a matrix representing an image
    each element is a number,
    returns the blended image's matrix
    """
    blended = process_matrix(matrix)
    return blended

##adjust so it blends n times
##put titles
def k_times_blended_heatmap(dim, k=1):
    """
    creates a random matrix of dimentions dim x dim
    representing a heatmap
    displays the heatmap
    then blends the matrix twice,
    displaying the heatmap each time
    """
    image_matrix = create_image(dim)
    for _ in range(k):
        image_matrix = create_blended_image(image_matrix)
    y = pd.DataFrame(image_matrix)
    sns.heatmap(y, annot=False, vmin=0, vmax=10)
    plt.title(f"Heatmap blended {k} time(s)")
    plt.axis("off")
    plt.show()
    return image_matrix

