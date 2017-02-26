#! /usr/bin/python
# coding = utf-8

# Calculate WSI image contour
#
# Usage:
# ------
# BW = WSIcontour(Image0);
#
# Input arguments:
# ----------------
# Image0: input WSI image.
#
# Output arguments:
# -----------------
# BW: image contour/mask.
#
# ---------------------------------------------------------------------
# Written by Jean Hu from Knowledge Vision Ltd., 02-16-2017

# -------------------------------------------


import cv2
import numpy as np

import os
import os.path

import re

from cytomine import Cytomine
from cytomine.models import *
import cytomine.models
import cytomine.models
import time

import urllib


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# Split original image to patch block which size determine by variable patchSize
#
# Usage:
# ------
# getmask(src)
#
# Input arguments
# ----------------
# src:      source image
#
# Output arguments
# -----------------
# mask:     mask image
#
# ---------------------------------------------------------------------
# Written by Jean Hu from Knowledge Vision Ltd., 02-23-2017


def getmask(src):

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)  # convert to HSV

    h = cv2.split(hsv)[0]

    thresh_val, max_val = 0, 255

    # two-value by OTSU
    ret, binary = cv2.threshold(h, thresh_val, max_val, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # find contours
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    thresh_area = 100  # area threshold

    # remove small area
    smallregion = np.ones(binary.shape, np.uint8)

    for i in range(len(contours)):

        cnt = contours[i]

        area = cv2.contourArea(cnt)  # area of contours

        if area < thresh_area:

            cv2.drawContours(smallregion, [cnt], 0, 0, -1)

    mask = smallregion * binary

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))    # close

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))    # open

    ret, mask = cv2.threshold(mask, 0, 1, cv2.THRESH_BINARY)

    return mask


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# Split original image to patch block which size determine by variable patchSize
#
# Usage:
# ------
# split2patch(src, mask, size, thresh, path)
#
# Input arguments
# ----------------
# src:      source image
# mask:     mask image
# size:     patch size
# thresh:   threshold of nonzero pixel ratio
# path:     save path
#
# Output arguments
# -----------------
# No
#
# ---------------------------------------------------------------------
# Written by Jean Hu from Knowledge Vision Ltd., 02-23-2017


def split2patch(src, mask, size=32, thresh=0.8, mode=True, path=''):

    height, width = mask.shape

    for i in range(height / size):

        for j in range(width / size):

            ox, oy = i * size, j * size

            patch_mask = mask[ox: ox + size, oy: oy + size]

            if float(patch_mask.sum()) / (size * size) > thresh:

                filename = 'patch(' + str(ox) + ',' + str(oy) + ').bmp'

                patch_src = src[ox: ox + size, oy: oy + size]

                cv2.imwrite(path + filename, patch_src)


# ---------------------------------------------------------------------
# ---------------------------------------------------------------------
# Merge the patch block image into a large image
#
# Usage:
# ------
# merge2image(path, size)
#
# Input arguments
# ----------------
# path:     directory of patch block image
# size:     size of result image
#
# Output arguments
# -----------------
# image:    result image
#
# ---------------------------------------------------------------------
# Written by Jean Hu from Knowledge Vision Ltd., 02-23-2017


def merge2image(path, size):

    filelist = os.listdir(path)

    image = np.zeros(size, np.uint8)

    for filename in filelist:

        patch = cv2.imread(path + filename)

        height = patch.shape[0]
        width = patch.shape[1]

        ox, oy = re.findall(r"\d+\.?\d*", filename)

        ox, oy = int(ox), int(oy)

        image[ox: ox + width, oy: oy + height] = patch

    return image


def getimages(host, public_key, private_key, id_project, path):

    # Connection to Cytomine Core
    conn = Cytomine(host, public_key, private_key, base_path='/api/', working_path='/tmp/', verbose=True)

    # image_instances = ImageInstanceCollection()
    # image_instances.project = id_project
    # image_instances = conn.fetch(image_instances)
    # images = image_instances.data()

    url = conn.get_project_image_instances(id_project).data()[0].thumb

    print url

    # path = '../data/grab.png'

    # url1 = 'https://imgsa.baidu.com/forum/pic/item/b145d688d43f8794d3f1538adb1b0ef41bd53a03.jpg'
    url1 = 'http://cytomine-core/api/abstractimage/2073/thumb.png'
    urllib.urlretrieve(url1, '../data/grab.png')

    image = cv2.imread(path)

    return image


def uploadimage(core_path, IMS_path, public_key, private_key, id_project, id_storage, file_path, protocol):

    # check connection to the Cytomine instance
    core_conn = Cytomine(core_path, public_key, private_key, verbose=False)

    # check that the storage exists
    storage = core_conn.get_storage(id_storage)

    assert storage.id == id_storage

    if id_project:

        project = core_conn.get_project(id_project)

        assert project.id == id_project

    # create the connection to the image management system (where you upload the images)
    ims_conn = Cytomine(IMS_path, public_key, private_key, verbose= False)

    # the properties/metadata you want to attach to the image
    properties = {'key1': 'value1', 'key2': 'value2'}

    ##################
    # OPTION 1 (SYNC UPLOAD)
    # With Sync = True, the server will answer once everything (copy, convert, deploy) is done the server
    # Therefore, you receive directly the UPLOADED_FILE with the ID of the created image
    # END OF OPTION 1
    ##################
    sync = True
    response = ims_conn.upload_image(file_path, id_project, id_storage, "%s%s" % (protocol, core_path), sync, properties)  # sync True
    uploaded_file_info = response.get('uploaded_file')
    uploaded_file_id = uploaded_file_info.get('id')
    uploaded_file = core_conn.get_uploaded_file(uploaded_file_id)
    assert uploaded_file.image
    image_properties = core_conn.get_abstract_image_properties(uploaded_file.image)
    print "OK (sync)"


