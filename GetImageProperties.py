import cv2

img = cv2.imread("nature.jpg")

#Image Shape
print(img.shape)
#Image Size
print(img.size)
#Image Value Data Type
print(img.dtype)
#Image Dimension Ex- 2d or 3d Array
print(img.ndim)