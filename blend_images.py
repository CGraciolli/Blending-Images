from PIL import Image
from heatmap_functions import k_times_blended_heatmap
from image import blend_image_k_times
from rgb import create_and_blend_image_rgb

k_times_blended_heatmap(15, 2)

create_and_blend_image_rgb(50, 1)

im = Image.open("dog.png")

blend_image_k_times(im, 5)
im.close()

