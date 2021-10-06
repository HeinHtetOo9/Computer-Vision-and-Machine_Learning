from skimage import io
from skimage.transform import resize,rescale,downscale_local_mean
from matplotlib import pyplot as plt

img = io.imread('images/balloon.jpg',as_gray=True)

resize_img = resize(img,(200,200),anti_aliasing = True)
rescale_img = rescale(img,1.0/1.0,anti_aliasing = True)
downscale_img = downscale_local_mean(img,(1,1))

plt.imshow(resize_img,cmap='gray')
plt.show()
