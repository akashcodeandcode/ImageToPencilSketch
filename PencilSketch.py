import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "rdj.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def dodge(front, back):
    final_sketch = front * 255 / (255 - back)

    # if any image is greater than 255 then it will convert it to 255
    final_sketch[final_sketch > 255] = 255
    final_sketch[back == 255] = 255

    # to convert any existing column to categorical type we will use aspect function
    # and uint8 is for 8-bit signed integer
    return final_sketch.astype('uint8')


ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 255 - gray

# to covert into blur image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=15)
# Sigma is the intensity of the blurness

r = dodge(blur, gray) # covert image to sketch

cv2.imwrite('rdj-sketch.png', r)

