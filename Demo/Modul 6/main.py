from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

# meload gambar
background = Image.open("image\\backgorund.jpg")
overlay = Image.open("image\\logo.jpg")

# mengilangkan aplha channel jika ada 
background = background.convert("RGBA")
overlay = overlay.convert("RGBA")

# bw,rotasi,blur
backgroundBw = background.convert("L")
backgroundRotation = backgroundBw.rotate(30)
backgroundBlur = backgroundRotation.filter(ImageFilter.GaussianBlur(5)).convert("RGB")

enhancer = ImageEnhance.Brightness(overlay)
overlay = enhancer.enhance(1.7)

enhancer = ImageEnhance.Contrast(overlay)
overlay = enhancer.enhance(1.9)

# menggambar text
draw = ImageDraw.Draw(overlay)
font_path = "font\\arial.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)
text = "Informatika JOSSS!"

# posisi text
text_width, text_height = 200, 100
text_x = (overlay.width - text_width) // 2
text_y = (overlay.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill=255)

# posisi overlay
x_center = (backgroundBlur.width - overlay.width) // 2
y_center = (backgroundBlur.height - overlay.height) // 2

# proses penempelan
backgroundBlur.paste(overlay, (x_center, y_center), overlay)

# simpan
backgroundBlur.save("Hasil\\tugas_praktikum_enam.jpg")
backgroundBlur.show()