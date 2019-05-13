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
from glob import glob

def getmax(rt):
    ans = 0
    for i in range(len(rt)):
		if (rt[ans] < rt[i]):
			ans = i
    return ans
'''
     input : filename  the path of input, such as 'music/blue1.mp3'
     output: number (0 ~ 9)
     0 -> blues;  1 -> classical; 2 -> country; 3 -> disco ;
     4 -> hiphop; 5 -> jazz     ; 6 -> metal  ; 7 -> pop   ;
     8 -> reggae; 9 -> rock     ;
'''
def calculate(filename):
	path = os.path.join(os.getcwd(), 'Generate/*')
	print(path)
	files = glob(path)
	for file in files:
		os.remove(file)
	model = createModel(10, sliceSize)
	model.load('model/musicDNN_4.0_60epoch.tflearn')
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
calculate("music/blue1.mp3")
