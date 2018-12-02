import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def DrawingDetectonRect(imagepath, filename, result):
    original = imagepath
    image = Image.open(original)
    image = np.asarray(image)  # convert image to numpy.ndarray

    # plot
    plt.close('all')
    plt.figure(figsize=(16, 9))

    # drawing image
    im1 = plt.imshow(image, cmap='gray')

    # detected objects
    lns = []
    for detection in result:
        x1 = detection['x']
        x2 = detection['x'] + detection['w']
        y1 = detection['y']
        y2 = detection['y'] + detection['h']
        rect_points = [[[x1, x2], [y1, y1]],
                       [[x2, x2], [y1, y2]],
                       [[x1, x2], [y2, y2]],
                       [[x1, x1], [y1, y2]]]
        for rect in rect_points:
            ln, = plt.plot(rect[0], rect[1], color='r', lw=2)
            lns.append(ln)

    plt.axis('off')
    plt.clim(im1.get_clim())

    if not os.path.exists('./detected'):
        os.makedirs('./detected')

    # TODO: GCSにアップロードして，外から見れるかどうか確認する
    detected_image = 'detected_' + filename + '.jpg'
    plt.savefig('./detected/' + detected_image, bbox_inches='tight')
