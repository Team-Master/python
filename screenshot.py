# screenshot.py

import datetime
# pip install pyautogui
from pyautogui import screenshot

now = datetime.datetime.now()

filename = now.strftime('%Y%m%d_%H%M%S') + '.png'
# screenshot('SRF' + filename)
screenshot('SRR' + filename, region=(6, 38, 1277, 752))
