# -*- coding: UTF-8 -*-
import time

import cv2


def template_macth(src, template, method):
    result = cv2.matchTemplate(src, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        loc = min_loc
    else:
        loc = max_loc
    return loc


def main():
    template = cv2.imread('img01.png', 1)
    src = cv2.imread('img02.png', 1)
    methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED]
    locations = []
    for method in methods:
        locations.append(template_macth(src, template, method))
    print(locations)


main()
