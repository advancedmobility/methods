import cv2
import os
import os.path as osp
import numpy as np

COLORS = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 255, 0),
    (255, 128, 0),
    (128, 0, 255),
    (255, 0, 128),
    (0, 128, 255),
    (0, 255, 128),
    (128, 255, 255),
    (255, 128, 255),
    (255, 255, 128),
    (60, 180, 0),
    (180, 60, 0),
    (0, 60, 180),
    (0, 180, 60),
    (60, 0, 180),
    (180, 0, 60),
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 0, 255),
    (0, 255, 255),
    (128, 255, 0),
    (255, 128, 0),
    (128, 0, 255),
]


def imshow_lanes(img, lanes,confidences, show=False, out_file=None, width=4):
    lanes_xys = []
    for _, lane in enumerate(lanes):
        xys = []
        for x, y in lane:
            if x <= 0 or y <= 0:
                continue
            x, y = int(x), int(y)
            xys.append((x, y))
        if len(xys)==0:
            xys.append((0,0))
            xys.append((0,0))
        lanes_xys.append(xys)

        lanes_xys.sort(key=lambda xys : xys[0][0])
        
        

    for idx, xys in enumerate(lanes_xys):
        x_label = int(np.mean([xys[1][0], xys[0][0]]))
        y_label = int(np.mean([xys[1][1], xys[0][1]]))
        cv2.putText(img,str(confidences[idx]),(x_label,y_label),fontFace = cv2.FONT_HERSHEY_COMPLEX, fontScale = 1.5,color=COLORS[idx])

        for i in range(1, len(xys)):
            cv2.line(img, xys[i - 1], xys[i], COLORS[idx], thickness=width)
        


    if show:
        cv2.imshow('view', img)
        cv2.waitKey(0)

    if out_file:
        if not osp.exists(osp.dirname(out_file)):
            os.makedirs(osp.dirname(out_file))
        cv2.imwrite(out_file, img)