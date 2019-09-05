from PIL import Image

# image open
im = Image.open('data/lena.jpg')

# size 600x600
img2 = im.resize((600, 600))
img2.save('lena-1000.jpg')
