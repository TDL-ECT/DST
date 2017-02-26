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

import os.path
import shutil

import kv

# # Cytomine connection parameters
# cytomine_host = "http://cytomine-core"
#
# cytomine_public_key = "51b4407a-97cc-4b3a-a098-ff06e066f588"
#
# cytomine_private_key = "65bf35e0-0d89-41b3-a275-2cc265aed9ad"
#
# id_project = 1723
#
# loadPath = '../data/'
# loadName = 'pathology.png'
#
# patchPath = '../patch/'
#
# kv.getimages(cytomine_host, cytomine_public_key, cytomine_private_key, id_project, loadPath + loadName)
#
# if os.path.exists(patchPath):
#
#     shutil.rmtree(patchPath)
#
# os.mkdir(patchPath)
#
# patch_size = 8
# thresh_percent = 0.8
#
# imageRGB = cv2.imread(loadPath + loadName)    # load image
#
# imageMask = kv.getmask(imageRGB)
# kv.split2patch(imageRGB, imageMask, patch_size, thresh_percent, True, patchPath)
# imageRes = kv.merge2image(patchPath, imageRGB.shape)
#
# cv2.imshow('imageRGB', imageRGB)
# cv2.imshow('imageMask', 255 * imageMask)
# cv2.imshow('imageRes', imageRes)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()



protocol = 'http://'
cytomine_core_path = "cytomine-core"
cytomine_public_key = "51b4407a-97cc-4b3a-a098-ff06e066f588"
cytomine_private_key = "65bf35e0-0d89-41b3-a275-2cc265aed9ad"
#the web url of cytomine upload server, always without the  protocol
cytomine_IMS_path = 'cytomine-core/data/33/'

# the storage_id of your user, see http://$CORE_URL/api/storage.json
id_storage = 56

# if you want that images be linked automatically with a project, set the ID of the project otherwise use None
id_project = 1723   # optional

file_path = '../data/merge_class0_prob.bmp'

kv.uploadimage(cytomine_core_path, cytomine_IMS_path, cytomine_public_key, cytomine_private_key, id_project, id_storage, file_path, protocol)
