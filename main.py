from PIL import Image

img = Image.open("images/𝟵𝗔𝗗 __ صَاد.jpg")
img.show()
img_RGP = img.convert("RGB")
img_RGP.show()
img_resized = img.resize((800,600))
img_resized.show()
img.save("C:/Users/ahmed.mostafa/PycharmProjects/Pillow/S@D.jpg")

print(f"image size: {img.size},",f"image format: {img.format},",f"image mode: {img.mode}")