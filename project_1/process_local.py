"""
ECE196 Face Recognition Project
Author: Will Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import cv2
import math
# TODO: Edit this function
def process_image():
  cv2.imwrite("geisel1.jpg", cv2.imread("geisel.jpg", 0))
  src = cv2.imread("geisel1.jpg", 0)
  dst = cv2.resize(src, (0,0), fx=.5, fy=.5)
  cv2.rectangle(dst, (math.floor(dst.shape[0]/2-50),math.floor(dst.shape[1]/2-50)),
       (math.floor(dst.shape[0]/2+50),math.floor(dst.shape[1]/2+50)), (255, 0, 0), 1)
  cv2.imwrite("geisel2.jpg", dst)
  return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# TODO: Call process_image function.
def main():
    hello_world()
    process_image()
    return


if(__name__ == '__main__'):
    main()
