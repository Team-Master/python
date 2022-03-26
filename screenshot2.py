# screenshot2.py

# pip install pyautogui
from pyautogui import screenshot
# pip install opencv-python
import cv2

import datetime
import time

def getFilename():
  now = datetime.datetime.now()
  filename = now.strftime('%Y%m%d_%H%M%S') + '.png'
  return 'SRF' + filename

# screenshot('SRF' + filename)
# screenshot('SRR' + filename, region=(240, 140, 1427, 808))  # fullsize
# screenshot('SRR' + filename, region=(275, 134, 1628, 905))
region = (275, 134, 1628, 905)
filename1 = getFilename()
screenshot('tmp/' + filename1, region)

while (True):
  time.sleep(1)

  filename2 = getFilename()
  screenshot('tmp/' + filename2, region)
  # image2 = screenshot('tmp/' + filename2, region)
  # image2.save(getFilename())

  # load images
  image1 = cv2.imread('tmp/' + filename1)
  image2 = cv2.imread('tmp/' + filename2)

  # compute difference
  difference = cv2.subtract(image1, image2)
  # print(difference)

  if (difference.sum() > 0):
    print('image changed!!')
    # color the mask red
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
    difference[mask != 255] = [0, 0, 255]

    # add the red mask to the images to make the differences obvious
    # image1[mask != 255] = [0, 0, 255]
    image2[mask != 255] = [0, 0, 255]

    # store images
    cv2.imwrite('out/' + filename2, image2)
    cv2.imwrite('out/diff-' + filename2, difference)

    filename1 = filename2
