from skimage import io
import matplotlib.pyplot as plt

img = io.imread('images/balloon.jpg',as_gray=True)

plt.imshow(img,cmap='gray')
plt.show()