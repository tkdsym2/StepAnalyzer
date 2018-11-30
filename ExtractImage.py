import os
import cv2


def MovieToFrame(filepath, filename):
    if not os.path.exists('./frames'):
        os.makedirs('./frames')

    # movie to frame
    count = 0
    cap = cv2.VideoCapture(filepath)
    while(cap.isOpened()):
        flag, frame = cap.read()
        if flag == False:
            break
        cv2.imwrite('./frames/{}.jpg'.format(filename), frame)
        print('save', './frames/{}.jpg'.format(filename))
        count += 1
        if count == 1:
            break
        cap.release()
    return './frames/{}.jpg'.format(filename)
