#pylint:disable=no-member

import cv2 as cv
import matplotlib.pyplot as plt

image_names = ['ME.jpg', 'me1.jpg', 'mywife.jpg', 'pancho.jpg']

for name in image_names:
    img = cv.imread(f'../Resources/Photos/{name}')
    if img is None:
        raise FileNotFoundError(f'Could not load image: ../Resources/Photos/{name}')

    cv.imshow(name, img)

    # BGR to Grayscale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow(f'{name} Gray', gray)

    # BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    cv.imshow(f'{name} HSV', hsv)

    # BGR to L*a*b
    lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
    cv.imshow(f'{name} LAB', lab)

    # BGR to RGB
    rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    cv.imshow(f'{name} RGB', rgb)

    # LAB to BGR
    lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
    cv.imshow(f'{name} LAB --> BGR', lab_bgr)

cv.waitKey(0)
cv.destroyAllWindows()