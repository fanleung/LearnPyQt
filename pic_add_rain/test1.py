import cv2
import numpy as np

img = cv2.imread("1.jpg")

b_channel, g_channel, r_channel = cv2.split(img)

alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255

# 最小值为0-255
alpha_channel[:, :int(b_channel.shape[0])] = 10

img_BGRA = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))

cv2.imwrite("11.png", img_BGRA)
