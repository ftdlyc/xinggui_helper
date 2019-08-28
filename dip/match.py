# 2019.8.14
# by ftdlyc

import sys
sys.path.append('./')

import cv2
import numpy as np
import win32_helper


# 非极大值抑制
def non_maximum_suppression(img, wt, ht):
    hi = img.shape[0]
    wi = img.shape[1]
    ht_haf = int(ht / 2)
    wt_haf = int(wt / 2)
    ret = []

    j = 0
    while j < hi:
        i = 0
        while i < wi:
            maxi = i
            maxj = j
            maxval = img[j, i]
            choose = True

            for j2 in range(j, min(hi, j + ht)):
                for i2 in range(i, min(wi, i + wt)):
                    if img[j2, i2] > maxval:
                        maxi = i2
                        maxj = j2
                        maxval = img[j2, i2]
            
            for j2 in range(max(0, maxj - ht_haf), min(hi, maxj + ht_haf)):
                for i2 in range(max(0, maxi - wt_haf), min(wi, maxi + wt_haf)):
                    if img[j2, i2] > maxval:
                        choose = False
                        break
                else:
                    continue
                break

            if choose:
                ret.append((maxval, maxi, maxj))

            i = i + wt
        j = j + ht
    
    return ret


def entropy(img):
    w = img.shape[1]
    h = img.shape[0]
    hist = np.zeros(256, dtype=float)
    for j in range(h):
        for i in range(w):
            hist[img[j, i]] += 1
    p = hist / (w * h)
    return -np.sum(p * np.log(p + 1e-8))


def joint_entropy(img1, img2):
    w = img1.shape[1]
    h = img1.shape[0]
    hist = np.zeros((256, 256), dtype=float)
    for j in range(h):
        for i in range(w):
            hist[img1[j, i], img2[j, i]] += 1
    p = hist / (w * h)
    return -np.sum(p * np.log(p + 1e-8))


def template_match_mi(img, template):
    if len(img.shape) > 2 and img.shape[2] > 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if len(template.shape) > 2 and template.shape[2] > 1:
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    w = img.shape[1]
    h = img.shape[0]
    tw = template.shape[1]
    th = template.shape[0]

    max_NMI = 0
    max_i = 0
    max_j = 0

    ET = entropy(template)
    for j in range(h - th):
        for i in range(w - tw):
            patch = img[j:j + th, i:i + tw]
            ES = entropy(patch)
            EST = joint_entropy(patch, template)
            NMI = (ET + ES) / EST

            if NMI > max_NMI:
                max_i = i
                max_j = j
                max_NMI = NMI

    return max_i, max_j


# 模板匹配
# 返回 (匹配值, 横坐标, 纵坐标)
def template_match(img, template, n=1):
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    if n == 1:
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        proposal = [(max_val, max_loc[0], max_loc[1])]
    else:
        proposal = non_maximum_suppression(res, template.shape[1], template.shape[0])
        def get_first(elem):
            return elem[0]
        proposal.sort(key=get_first, reverse=True)
    return proposal[0:n]


if __name__ == "__main__":
    handle = win32_helper.find_window_handle('MuMu', None, None)
    handle = win32_helper.find_first_child_window(handle)
    img = win32_helper.screenshot(handle)
    template = cv2.imread('./pic/button_use.png')
    ret = template_match(img, template)
    i = ret[0][1]
    j = ret[0][2]
    img = cv2.rectangle(img, (i, j), (i + template.shape[1], j + template.shape[0]), (255, 0, 0), 3)
    cv2.imshow('img', img)
    cv2.waitKey(0)
