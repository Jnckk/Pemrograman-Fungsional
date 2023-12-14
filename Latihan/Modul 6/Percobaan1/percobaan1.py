import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont

image = PIL.Image.open("Percobaan1/gambar/1.png")

image = image.convert("L") #hitam-putih

font = PIL.ImageFont.truetype("Percobaan1/font/arial.ttf", 24)
draw = PIL.ImageDraw.Draw(image)
draw.text((image.width // 2, image.height // 2), "Nama: [Riski Cahyadi] | NIM: [202110370311279]", font=font, fill="white")

# Simpan gambar
image.save("Percobaan1/gambarsave/percobaan.jpg")

# Tampilkan gambar
image.show()