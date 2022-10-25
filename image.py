from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from blend_matrix import process_matrix

##should be a function that recives an image
##divided in various small functions
##trabalho para a carolina do futuro

def get_pixel_matrix(im):
    """
    recives an image as a PIL file
    returns a matrix with its RGBA representation
    """
    w, h = im.size
    pix = list(im.getdata()) ##list of pixels
    pix_matrix = [pix[n:n+w] for n in range(0, w*h, w)]
    return pix_matrix

def separate_rgba_matrix(pix_matrix):
    """
    recives a matrix with the RGBA representation of an image
    returns a list of matrixes, each representing red, green, blue or the trasnparency
    """
    list_matrixes_rgba = []
    ##the first matrix in the list represents red, the second green, 
    ## the third blue and the fourth the transparency
    for _ in range(4):
        list_matrixes_rgba.append([])
    for row in pix_matrix:
        row_list = []
        for _ in range(4):
            row_list.append([])
        for elem in row:
            for i in range(4):
                row_list[i].append(elem[i])
        for i in range(4):
            list_matrixes_rgba[i].append(row_list[i])
    return list_matrixes_rgba

def blend_matrixes_rgba(list_matrixes, k=1):
    """
    recives a list of matrixes representing RGBA
    returns the list of the matrixes representing the RGBA of the image blended k times
    """
    for _ in range(k):
        list_matrixes = map(process_matrix, list_matrixes)
    return list(list_matrixes)

def construct_matrix_rgba(list_matrixes):
    """
    recives a list of matrixes, each representing R, G, B or A
    returns one matrix that combines all four matrixes
    """
    blended_matrix = []
    dim_rows = len(list_matrixes[0]) ##how many rows each matrix has
    dim_columns = len(list_matrixes[0][0]) ##how many columns each matrix has
    for row_index in range(dim_rows):
        blended_row = []
        for column_index in range(dim_columns):
            blended_pixel = []
            for color in range(4):
                blended_pixel.append(list_matrixes[color][row_index][column_index])
            blended_row.append(blended_pixel)
        blended_matrix.append(blended_row)
    return blended_matrix

def display_image_rgba(matrix, k):
    """
    recives one matrix with the RGBA representation of an image
    displays the image
    """
    blended_image = Image.fromarray(np.array(matrix, dtype=np.uint8), 'RGBA')
    plt.imshow(blended_image)
    plt.title(f"Image blended {k} time(s)")
    plt.axis("off")
    plt.show()

##the images should have titles
def blend_image_k_times(img, k):
    """
    recives an image in a PIL format,
    displays it,
    blends it k times and
    displays the blended image
    """
    ##displays the image
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")
    plt.show()
    pixel_matrix = get_pixel_matrix(img)
    list_rgba = separate_rgba_matrix(pixel_matrix)
    list_rgba_blended = blend_matrixes_rgba(list_rgba, k)
    blended_rgba_matrix = construct_matrix_rgba(list_rgba_blended)
    display_image_rgba(blended_rgba_matrix, k)