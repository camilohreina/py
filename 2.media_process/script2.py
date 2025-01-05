import cv2
import glob

images = glob.glob('*.jpg')
for image in images:
    img = cv2.imread(image, 0)
    resize_img = cv2.resize(img,(100,100)) # resize the image
    cv2.imshow('Hey', resize_img)
    cv2.imwrite('resized_'+image, resize_img)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite('resized_'+image, resize_img)