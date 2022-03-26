from pynput.mouse import Controller
import time

while(True):
    print("Current position: " + str(Controller().position))
    time.sleep(1)