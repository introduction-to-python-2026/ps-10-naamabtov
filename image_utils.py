import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_image(path):
    image = Image.open(path)
    return np.array(image)

def edge_detection(image):
    gray = image.mean(axis=2)

    vertical_filter = np.array([
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ])

    horizontal_filter = np.array([
        [1,   0, -1],
        [ 1,  0,  -1],
        [ 1,  0,  -1]
    ])

    edgeX = convolve2d(gray, horizontal_filter,
                       mode="same", boundary="fill", fillvalue=0)

    edgeY = convolve2d(gray, vertical_filter,
                       mode="same", boundary="fill", fillvalue=0)

    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)
    return edgeMAG
