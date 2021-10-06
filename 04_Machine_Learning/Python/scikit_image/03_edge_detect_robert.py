from skimage import io
from skimage.filters import roberts
from matplotlib import pyplot as plt
from skimage import data

img = data.coins()

robert_img = roberts(img,)
plt.imshow(robert_img,cmap='gray')
plt.show()
