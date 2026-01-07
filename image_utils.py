from PIL import Image
import numpy as np
from scipy.signal import convolve2d


def load_image(path):
    image = Image.open(path)
    return np.array(image)


    import numpy as np
from scipy.signal import convolve2d

def edge_detection(image):
    gray = image.mean(ןimage,axis=2)
    filter_vertical = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    filter_horizontal = np.array([
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ])
    edgeX = convolve2d(gray, horizontal_filter,
                       mode="same", boundary="fill", fillvalue=0)

    edgeY = convolve2d(gray, vertical_filter,
                       mode="same", boundary="fill", fillvalue=0)

    # Edge magnitude
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeM
