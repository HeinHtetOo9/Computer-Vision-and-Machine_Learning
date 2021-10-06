from skimage import io
from skimage.filters import roberts ,sobel ,scharr ,prewitt
from matplotlib import pyplot as plt
from skimage import data

img = data.coins()

robert_img = roberts(img)
sobel_img = sobel(img)
scharr_img = scharr(img)
prewitt_img = prewitt(img)

_,axes = plt.subplots(nrows = 2 , ncols = 2 )
ax = axes.ravel()

ax[0].imshow(robert_img, cmap='gray')
ax[0].set_title('Original image')

ax[1].imshow(sobel_img, cmap='gray')
ax[1].set_title('Sobel')

ax[2].imshow(scharr_img, cmap='gray')
ax[2].set_title('scharr')

ax[3].imshow(prewitt_img, cmap='gray')
ax[3].set_title('prewitt')

for a in ax:
    a.axis('off')
    
plt.tight_layout()
plt.show()