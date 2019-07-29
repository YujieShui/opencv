'''
@Description: 二值图像连通组件状态统计
@Author: shuiyj
@Date: 2019-07-29 17:35:59
'''
import cv2 as cv
import numpy as np

def connected_components_stats_demo(src):
    src = cv.GaussianBlur(src, (3, 3), 0)
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)

    num_labels, labels, stats, centers = cv.connectedComponentsWithStats(binary, connectivity=8, ltype=cv.CV_32S)
    colors = []
    for i in range(num_labels):
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        colors.append((b, g, r))

    colors[0] = (0, 0, 0)
    image = np.copy(src)
    for t in range(1, num_labels, 1):
        x, y, w, h, area = stats[t]
        cx, cy = centers[t]
        cv.circle(image, (np.int32(cx), np.int32(cy)), 2, (0, 255, 0), 2, 8, 0)
        cv.rectangle(image, (x, y), (x+w, y+h), colors[t], 1, 8, 0)
        cv.putText(image, "num:" + str(t), (x, y), cv.FONT_HERSHEY_SIMPLEX, .5, (0, 0, 255), 1);
        print("label index %d, area of the label : %d"%(t, area))

    cv.imshow("colored labels", image)
    cv.imwrite("D:/labels.png", image)
    print("total rice : ", num_labels - 1)


input = cv.imread("../images/rice.png")
connected_components_stats_demo(input)
cv.waitKey(0)
cv.destroyAllWindows()