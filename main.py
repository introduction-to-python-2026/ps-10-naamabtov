 from image_utils import load_image, edge_detection
import matplotlib.pyplot as plt
import numpy as np

image = load_image("/content/dog.png")

from skimage.filters import median
from skimage.morphology import ball

clean_image = median(image, ball(3))

edges = edge_detection(clean_image)

threshold = 50  # adjust based on histogram
edge_binary = edges > threshold


from PIL import Image

edge_image = Image.fromarray((edge_binary * 255).astype(np.uint8))
edge_image.save("my_edges.png")
