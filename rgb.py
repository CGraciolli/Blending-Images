import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import make_lupton_rgb
from blend_matrix import process_matrix

def create_random_image_rgb(dim):
    """
    creates a square image of dimentions dim x dim pixels
    each pixel has a randomly generated rgb value
    displays the image
    and returns a list containing the three matrixes (representing red, blue and green)"""
    ##random number generator
    rng = np.random.default_rng() 
    image_r = rng.random((dim, dim)) 
    image_g = rng.random((dim, dim)) 
    image_b = rng.random((dim, dim))
    ##creates an image from 3 matrixes representing red, green and blue
    image = make_lupton_rgb(image_r, image_g, image_b, stretch = 0.1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()
    return [image_r, image_g, image_b]

def blend_image_rgb_k_times(list_matrix, k=1):
    """
    recives a list of the rgb matrixes of an image
    creates a blended image, displays it and
    return the rgb matrixes of the blended image
    """
    for _ in range(k):
        list_matrix = map(process_matrix, list_matrix)
    list_blended = list(list_matrix)
    blended_img = make_lupton_rgb(list_blended[0], list_blended[1], list_blended[2], stretch = 0.1) 
    plt.imshow(blended_img)
    plt.title(f"Image blended {k} time(s)")
    plt.axis("off")
    plt.show()
    return list_blended

##could be modified so it blends the image n times
def create_and_blend_image_rgb(dim, k=1):
    """
    creates a randomly generated image of dimentions dim x dim pixels
    using rgb matrixes and displays it,
    then blends the image k times,
    displays the blended image
    """
    list_rgb = create_random_image_rgb(dim)
    blend_image_rgb_k_times(list_rgb, k)
