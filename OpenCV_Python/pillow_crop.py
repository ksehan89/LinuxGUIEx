from PIL import Image

# image open
im = Image.open('data/lena.jpg')

cropImage = im.crop((100, 100, 350, 350))
cropImage.show()

# save image to as .JPG
cropImage.save('data/lena-crop.jpg')
