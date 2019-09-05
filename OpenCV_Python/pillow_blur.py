from PIL import Image, ImageFilter

# image open
im = Image.open('data/lena.jpg')

blurImage = im.filter(ImageFilter.BLUR)
blurImage.show()
blurImage.save('lena-blur.jpg')
