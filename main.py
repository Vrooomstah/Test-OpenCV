import cv2 as cv
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap = WindowCapture('RuneLite - Vrooomstah')
vision_leaf = Vision('osrs_banner.jpg')

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.getScreenshot()

    # display the processed image
    points = vision_leaf.find(screenshot, 0.2, 'rectangles')

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')