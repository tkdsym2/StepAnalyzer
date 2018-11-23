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
    # TODO: 検出された数だけ回すようにする
    for detection in result:
        print detection

    plt.axis('off')
    plt.clm(im1.get_clim())

    if not os.path.exists('./detected'):
        os.makedirs('./detected')

    # TODO: GCSにアップロードして，外から見れるかどうか確認する
    detected_image = 'detected_' + filename + '.jpg'
    plt.savefig('./detected/' + detected_image)
