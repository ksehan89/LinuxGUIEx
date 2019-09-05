from PIL import Image

# image open
im = Image.open('data/lena.jpg')

# image size & output
print(im.size)
im.show()

# save image to as .JPG
im.save('data/pillow_Lena.jpg')
