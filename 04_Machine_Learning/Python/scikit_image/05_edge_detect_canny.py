from skimage.feature import canny
from skimage import data
from matplotlib import pyplot as plt
img = data.coins()

canny_img = canny(img,sigma = 5)

plt.imshow(canny_img)
plt.show()