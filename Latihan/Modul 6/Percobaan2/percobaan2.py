import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image, ImageDraw, ImageFont

gambar_latar_belakang = Image.open('Percobaan2/gambar/bg.png')

gambar_objek = Image.open('Percobaan2/gambar/logo.png')

gambar_objek = gambar_objek.convert('RGB')

gambar_objek = gambar_objek.resize((333, 188))

posisi_x = 200
posisi_y = 200

# Sisipkan gambar overlay ke dalam gambar latar belakang
gambar_latar_belakang.paste(gambar_objek, (posisi_x, posisi_y))

gambar_latar_belakang.save('Percobaan2/gambarhasiledit/hasil_edit.png')

plt.imshow(gambar_latar_belakang)
plt.axis('off')
plt.show()