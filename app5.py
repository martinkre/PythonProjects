# Importing the OpenCV library
import cv2
# Reading the image using imread() function
image = cv2.imread('road.jpg')
var = 200
# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))
text = cv2.putText(image, 'Air speed: '+ str(var), (200, 200), 
                   cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
cv2.imshow("Display window",image)

k= cv2.waitKey(0)
    