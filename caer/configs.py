# Copyright 2020 The Caer Authors. All Rights Reserved.
#
# Licensed under the MIT License (see LICENSE);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at <https://opensource.org/licenses/MIT>
#
# ==============================================================================


# Configuration Variables used in Caer
CROP_CENTRE = 1
CROP_TOP = 2
CROP_LEFT = 3
CROP_RIGHT = 4
CROP_BOTTOM = 5

VALID_URL_NO_EXIST = 0
INVALID_URL_STRING = -1

#  OpenCV 

## Interpolations
INTER_NEAREST = 0  # cv.INTER_NEAREST
INTER_LINEAR = 1  # cv.INTER_LINEAR
INTER_CUBIC = 2  # cv.INTER_CUBIC
INTER_AREA = 3  # cv.INTER_AREA

## Color Spaces
IMREAD_COLOR = 1 # cv.IMREAD_COLOR
BGR2RGB = 4  # cv.COLOR_BGR2RGB
BGR2GRAY = 6  # cv.COLOR_BGR2GRAY
RGB2GRAY = 7  # cv.COLOR_RGB2GRAY
BGR2HSV = 40  # cv.COLOR_BGR2HSV
RGB2HSV = 41  # cv.COLOR_RGB2HSV
BGR2LAB = 44  # cv.COLOR_BGR2LAB
RGB2LAB = 45  # cv.COLOR_RGB2LAB

## Video
FPS = 5  # cv.CAP_PROP_FPS
FRAME_COUNT = 7  # cv.CAP_PROP_FRAME_COUNT



__all__ = [
    'CROP_CENTRE',
    'CROP_TOP',
    'CROP_LEFT',
    'CROP_RIGHT',
    'CROP_BOTTOM',
    'VALID_URL_NO_EXIST',
    'INVALID_URL_STRING',
    'BGR2GRAY',
    'BGR2RGB',
    'BGR2HSV',
    'BGR2LAB',
    'RGB2GRAY',
    'RGB2HSV',
    'RGB2LAB',
    'IMREAD_COLOR',
    'INTER_NEAREST',
    'INTER_LINEAR',
    'INTER_AREA',
    'INTER_CUBIC',
    'FRAME_COUNT',
    'FPS'
]