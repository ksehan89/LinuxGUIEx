from PIL import Image

# image open
im = Image.open('data/lena.jpg')

# Thumbnail image create
size = (64, 64)
im.thumbnail(size)
im.show()

# save image to as .JPG
im.save('data/lena-thumb.jpg')
