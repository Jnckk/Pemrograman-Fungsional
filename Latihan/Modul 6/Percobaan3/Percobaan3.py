import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageEnhance

gambar = Image.open('Percobaan3/gambar/bg.png')

enhancer = ImageEnhance.Brightness(gambar)
gambar = enhancer.enhance(1.5)

enhancer = ImageEnhance.Contrast(gambar)
gambar = enhancer.enhance(1.2)

gambar = gambar.convert('RGB')

gambar.save('Percobaan3/gambarhasiledit/brightness_contrast_image.png')

plt.imshow(gambar)
plt.axis('off')
plt.show()