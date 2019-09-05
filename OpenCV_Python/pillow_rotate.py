from PIL import Image

# image open
im = Image.open('data/lena.jpg')

# size 600x600
#img2 = im.resize((600, 600))
#img2.save('lena-1000.jpg')

# 90 degree rotate
img3 = im.rotate(90)
img3.save('lena-rotate.jpg')
