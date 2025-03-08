from chrplotlib import img
import cv2
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(CURRENT_DIR, 'data')

# img_path = os.path.join(IMAGE_DIR, 'd.jpeg')
img_path = os.path.join(IMAGE_DIR, 'img1.jpeg')
img_path = os.path.join(IMAGE_DIR, 'long.jpg')

img_data = cv2.imread(img_path)

print(img.plot_from_img(img_data, max_width=80))

with open("output.txt", "w") as f:
    f.write(img.plot_from_img(img_data, max_width=150))
