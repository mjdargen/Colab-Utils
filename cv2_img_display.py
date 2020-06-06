import cv2
import numpy as np
import requests
from google.colab.patches import cv2_imshow


def show_url_image(url, width):
  # request image file from url
  url_response = requests.get(url)
  # convert to image that can be shown using openCV
  img_array = np.asarray(bytearray(url_response.content), dtype=np.uint8)
  img = cv2.imdecode(img_array, -1)
  # get current image size and resize to width
  (h, w) = img.shape[:2]
  img = cv2.resize(img, (width, int(h * width/w)))
  # show imagre
  cv2_imshow(img)

def show_local_image(img_path, width):
  # load local image
  img = cv2.imread(img_path)
  # get current image size and resize to width
  (h, w) = img.shape[:2]
  img = cv2.resize(img, (width, int(h * width/w)))
  # show image
  cv2_imshow(img)
