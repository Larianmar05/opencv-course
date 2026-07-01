#pylint:disable=no-member

import cv2 as cv
import numpy as np

image_names = ['ME.jpg', 'me1.jpg', 'mywife.jpg', 'pancho.jpg']

for name in image_names:
    img = cv.imread(f'../Resources/Photos/{name}')
    if img is None:
        raise FileNotFoundError(f'Could not load image: ../Resources/Photos/{name}')

    cv.imshow(name, img)

    blank = np.zeros(img.shape, dtype='uint8')
    cv.imshow(f'{name} Blank', blank)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow(f'{name} Gray', gray)

    blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
    cv.imshow(f'{name} Blur', blur)

    canny = cv.Canny(blur, 125, 175)
    cv.imshow(f'{name} Canny Edges', canny)

    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    print(f'{name}: {len(contours)} contour(s) found!')

    cv.drawContours(blank, contours, -1, (0,0,255), 1)
    cv.imshow(f'{name} Contours Drawn', blank)

cv.waitKey(0)
cv.destroyAllWindows()