import cv2

img = cv2.imread('galaxy.jpg', 0)
print(type(img))
print(img)
print(img.shape)   # resolution of the image
print(img.ndim)    # number of dimensions

resize_img = cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2))) # resize the image
cv2.imshow('Galaxy', resize_img)
cv2.imwrite('galaxy_resized.jpg', resize_img)
cv2.waitKey(0)  
cv2.destroyAllWindows()