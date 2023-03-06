from PIL import Image,ImageChops
img1 = Image.open('dif1.jpeg')
img2 = Image.open('dif2.jpeg')
diff = ImageChops.difference(img1,img2)
if diff.getbbox():
   diff.show()

