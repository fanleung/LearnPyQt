# 导入工具包
from imutils import contours
import numpy as np
import argparse
import cv2
import myutils


# 设置是否为调试模式
# 调试模式：debug_mode = 1
# 非调试模式：debug_mode = 0
debug_mode = 1


# 绘图展示
def cv_show(name, img):
    if debug_mode:
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        pass


# 读取一个模板图像
# img = cv2.imread('temp.png')
img = cv2.imread('temp2.png')
cv_show('img', img)
# 灰度图
ref = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv_show('ref', ref)
# 二值图像
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1]
cv_show('ref', ref)

# 计算轮廓
# cv2.findContours()函数接受的参数为二值图，即黑白的（不是灰度图）,cv2.RETR_EXTERNAL只检测外轮廓，cv2.CHAIN_APPROX_SIMPLE只保留终点坐标
# 返回的list中每个元素都是图像中的一个轮廓

ref_, refCnts, hierarchy = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, refCnts, -1, (0, 0, 255), 3)
cv_show('img', img)
print(np.array(refCnts).shape)
refCnts = myutils.sort_contours(refCnts, method="left-to-right")[0]  # 排序，从左到右，从上到下
digits = {}

# 遍历每一个轮廓
for (i, c) in enumerate(refCnts):
    # 计算外接矩形并且resize成合适大小
    (x, y, w, h) = cv2.boundingRect(c)
    roi = ref[y:y + h, x:x + w]
    roi = cv2.resize(roi, (60, 100))
    # roi = cv2.resize(roi, (57, 88))

    # cv_show("digits_roi", roi)

    # 每一个数字对应每一个模板
    digits[i] = roi

# 初始化卷积核
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 读取输入图像，预处理
# image = cv2.imread('card.png')
image = cv2.imread('22.jpg')
cv_show('image', image)
# 这一句很重要，会影响到识别效果
image = myutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv_show('gray', gray)

# 礼帽操作，突出更明亮的区域
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
cv_show('tophat', tophat)

# 用Sobel算子边缘检测
gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0,  # ksize=-1相当于用3*3的
                  ksize=-1)
gradX = np.absolute(gradX)
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
gradX = gradX.astype("uint8")
# 这打印啥啊
print(np.array(gradX).shape)
cv_show('gradX', gradX)


# 通过闭操作（先膨胀，再腐蚀）将数字连在一起
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
cv_show('gradX', gradX)
# THRESH_OTSU会自动寻找合适的阈值，适合双峰，需把阈值参数设置为0
thresh = cv2.threshold(gradX, 0, 255,
                       cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
cv_show('thresh', thresh)

# 再来一个闭操作

thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)  # 再来一个闭操作
cv_show('thresh', thresh)

# 计算轮廓
thresh_, threshCnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                                                  cv2.CHAIN_APPROX_SIMPLE)

cnts = threshCnts
cur_img = image.copy()
cv2.drawContours(cur_img, cnts, -1, (0, 0, 255), 3)
cv_show('img', cur_img)
locs = []

## (212, 160, 77, 14)
# 遍历轮廓
for (i, c) in enumerate(cnts):
    # 计算矩形
    (x, y, w, h) = cv2.boundingRect(c)
    ar = w / float(h)
    print(x, y, w, h)
    # 选择合适的区域，根据实际任务来，这里的基本都是四个数字一组
    if ar > 3 and ar < 4:
        if (w > 70 and w < 90) and (h > 20 and h < 25):
            # 符合的留下来
            # x = x+32
            # w = w-32
            locs.append((x, y, w, h))
            print("选择合适的区域")
            print((x, y, w, h))

# 204 261 76 12
# 136 162 87 27
#     if ar > 4 and ar < 7:
#         if (w > 70 and w < 90) and (h > 5 and h < 15):
#             # 符合的留下来
#             x = x+28
#             w = w-28
#             locs.append((x, y, w, h))
#             print("选择合适的区域")
#             print((x, y, w, h))





# 将符合的轮廓从左到右排序
locs = sorted(locs, key=lambda x: x[0])
print("locs:")
print(locs)
output = []


# 遍历每一个轮廓中的数字
for (i, (gX, gY, gW, gH)) in enumerate(locs):
    print("line141")
    print(i, (gX, gY, gW, gH))
    # initialize the list of group digits
    groupOutput = []

    # 根据这个坐标，提取数字，并显示
    # 根据坐标提取每一个组
    group = gray[gY - 5:gY + gH + 5, gX - 5:gX + gW + 5]
    cv_show('group', group)

    # 预处理
    group = cv2.threshold(group, 0, 255,
                          cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv_show('预处理', group)

    # # 简单滤波
    # ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # # Otsu 滤波
    # ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # 计算每一组的轮廓
    group_, digitCnts, hierarchy = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_SIMPLE)
    digitCnts = contours.sort_contours(digitCnts,
                                       method="left-to-right")[0]

    print("length:", len(digitCnts))
    # 计算每一组中的每一个数值
    for c in digitCnts:
        # 找到当前数值的轮廓，resize成合适的的大小
        (x, y, w, h) = cv2.boundingRect(c)
        print((x, y, w, h))
        roi = group[y:y + h, x:x + w]
        roi = cv2.resize(roi, (60, 100))
        cv_show('roi', roi)
        if w > 2 and h > 2:

            # 计算匹配得分
            scores = []

            # 在模板中计算每一个得分
            for (digit, digitROI) in digits.items():
                # 模板匹配
                result = cv2.matchTemplate(roi, digitROI,
                                           cv2.TM_CCOEFF)
                (_, score, _, _) = cv2.minMaxLoc(result)
                scores.append(score)

            # 得到最合适的数字
            groupOutput.append(str(np.argmax(scores)))


    # 画出来
    cv2.rectangle(image, (gX - 5, gY - 5),
                  (gX + gW + 5, gY + gH + 5), (0, 0, 255), 1)
    cv2.putText(image, "".join(groupOutput), (gX-32, gY - 15),
                cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

    # 得到结果
    output.extend(groupOutput)

# 打印结果
# print("Credit Card Type: {}".format(FIRST_NUMBER[output[0]]))
print("Credit Card #: {}".format("".join(output)))
cv2.imshow("Image", image)
cv2.waitKey(0)
