from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    import numpy as np
from PIL import Image

def load_image(path):
    image = Image.open(path).convert("RGB")
    return np.array(image)

def edge_detection(image):
    import numpy as np
from scipy.signal import convolve2d

def edge_detection(image):
    """
    Perform edge detection on a color image.
    """
    # Convert RGB → grayscale
    gray = image.mean(axis=2)

    # Sobel filters
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
