# Copyright © 2019 by Spectrico

import classifier
import MTCNN
import cv2
import numpy as np

race_classifier = classifier.Classifier()
mtcnn = MTCNN.MTCNN()

# Load an color image
img = cv2.imread('image.jpg', cv2.IMREAD_COLOR)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
boxes = mtcnn.detect(img[:,:,::-1])
for box in boxes:
    score = box[4]
    box = box[:4] + 0.5
    box = box.astype(np.int32)
    x = box[0]
    y = box[1]
    w = box[2] - x
    h = box[3] - y
    l = max(w, h)
    x1 = int(x - (l - w) / 2)
    y1 = int(y - (l - h) / 2)
    x2 = x1 + l
    y2 = y1 + l
    x1 = max(0, x1)
    y1 = max(0, y1)
    x2 = min(img.shape[1], x2)
    y2 = min(img.shape[0], y2)
    result = race_classifier.predict(img[y1:y2, x1:x2])
    cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]), (0, 0, 255))
    text = "{}".format(result[0]['race'])
    # Print race on the output image
    cv2.putText(img, text, (box[0], box[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))


cv2.imshow('image',img)
cv2.imwrite('out.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
