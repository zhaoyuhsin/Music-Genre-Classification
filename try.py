# -*- coding: utf-8 -*-
import random
import string
import os
import sys
import numpy as np

from model import createModel
from datasetTools import getDataset
from config import slicesPath
from config import batchSize
from config import filesPerGenre
from config import nbEpoch
from config import validationRatio, testRatio
from config import sliceSize
from imageFilesTools import getImageData
from songToData import createSlicesFromAudio, mp3topng
def getmax(rt):
    ans = 0
    for i in range(len(rt)):
		if (rt[ans] < rt[i]):
			ans = i
    return ans
def calculate(filename):
	mp3topng(filename)
	data = []
	ct = 0
	path = "Generate/"
	for file in os.listdir(path):
		if file.endswith(".png"):
			imgdata = getImageData(path+file, sliceSize)
			data.append(imgdata)
			ct += 1
	pred = model.predict(data)
	add = [0 for i in range(10)]
	for i in range(ct):
		tt = getmax(pred[i])
		#print("max={}".format(tt))
		add[tt] += 1
	print(add)
	return getmax(add) 
model = createModel(10, sliceSize)
model.load('musicDNN_1.0.tflearn')
calculate("tt.mp3")






