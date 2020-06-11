from PIL import Image
from PIL import ImageGrab
from PIL import ImageChops
import time

def PixelCheck(x1, y1, x2, y2):
  im1 = ImageGrab.grab((x1, y1, x2, y2))
  im1.save('img1.png')

  while 1:
    time.sleep(0.1)
    im2 = ImageGrab.grab((x1, y1, x2, y2))
    im2.save('img2.png')
    im = ImageChops.difference(im1, im2)

    px = im.load()
    for y in range(im.height):
      for x in range(im.width):
        # if im.getpixel((x, y)) != (0, 0, 0):
        if px[x, y] != (0, 0, 0):
          return x, y

# x1, y1, x2, y2 = map(int, input('Enter x1, y1, x2, y2 values: ').split())
x1, y1, x2, y2 = map(int, ('0 100 100 200').split())

coord = PixelCheck(x1, y1, x2, y2)
print(x1 + coord[0], y1 + coord[1])
