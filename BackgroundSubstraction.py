from skimage.measure import compare_ssim
import argparse
import imutils
import cv2


def GetDiffPoint(filepath):
    default = cv2.imread('./default.jpg')
    input_image = cv2.imread(filepath)

    # convert grayscale
    gray_default = cv2.cvtColor(default, cv2.COLOR_BGR2GRAY)
    gray_input = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

    # calcurate Structural Similarity Index (SSIM) between the two images
    (score, diff) = compare_ssim(gray_default, gray_input, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    # threshold the difference image,
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]

    diff_list = []
    for i, c in enumerate(cnts):
        (x, y, w, h) = cv2.boundingRect(c)
        if w <= 80 or h <= 80:
            continue
        point_object = {
            'x': x,
            'y': y,
            'w': w,
            'h': h
        }
        diff_list.append(point_object)

    return diff_list


'''
表示したいならこれ
Aheight = imageA.shape[0]
Awidth = imageA.shape[1]
Bheight = imageB.shape[0]
Bwidth = imageB.shape[1]
diffheight = diff.shape[0]
diffwidth = diff.shape[1]
threshheight = thresh.shape[0]
threshwidth = thresh.shape[1]

resizedA = cv2.resize(imageA, (int(Awidth/4), int(Aheight/4)))
resizedB = cv2.resize(imageB, (int(Bwidth/4), int(Bheight/4)))
resizedDiff = cv2.resize(diff, (int(diffwidth/4), int(diffheight/4)))
resizedThresh = cv2.resize(thresh, (int(threshwidth/4), int(threshheight/4)))

# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
