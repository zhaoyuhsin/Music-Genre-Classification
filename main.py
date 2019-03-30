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

from songToData import createSlicesFromAudio

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("mode", help="Trains or tests the CNN", nargs='+', choices=["train","test","slice"])
args = parser.parse_args()

print("--------------------------")
print("| ** Config ** ")
print("| Validation ratio: {}".format(validationRatio))
print("| Test ratio: {}".format(testRatio))
print("| Slices per genre: {}".format(filesPerGenre))
print("| Slice size: {}".format(sliceSize))
print("--------------------------")

if "slice" in args.mode:
	createSlicesFromAudio()
	sys.exit()

#List genres
genres = os.listdir(slicesPath)
genres = [filename for filename in genres if os.path.isdir(slicesPath+filename)]
nbClasses = len(genres)

#Create model 
model = createModel(nbClasses, sliceSize)
def Cal(rs):
	tot = 0
	for i in range(len(rs)):
		if (rs[i] == 1):
			tot = i
	return tot
if "train" in args.mode:

	#Create or load new dataset
	print("Hi, Tom")
	print(genres)
	train_X, train_y, validation_X, validation_y = getDataset(filesPerGenre, genres, sliceSize, validationRatio, testRatio, mode="train")

	#Define run id for graphs
	run_id = "MusicGenres - "+str(batchSize)+" "+''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(10))
	model.load('musicDNN_5.0_80epoch.tflearn')
	#Train the model
	print("[+] Training the model...")
	model.fit(train_X, train_y, n_epoch=nbEpoch, batch_size=batchSize, shuffle=True, validation_set=(validation_X, validation_y), snapshot_step=100, show_metric=True, run_id=run_id)
	print("    Model trained! ✅")

	#Save trained model
	print("[+] Saving the weights...")
	model.save('musicDNN_6.0.tflearn')
	print("[+] Weights saved! ✅💾")

if "test" in args.mode:

	#Create or load new dataset
	test_X, test_y = getDataset(filesPerGenre, genres, sliceSize, validationRatio, testRatio, mode="test")
	#train_X, train_y, validation_X, validation_y = getDataset(filesPerGenre, genres, sliceSize, validationRatio, testRatio, mode="train")
    #Load weights
	print("[+] Loading weights...")
	model.load('musicDNN_5.0_80epoch.tflearn')

	num = len(test_X)
	pred = model.predict(test_X)
	corr = 0
	a = [0 for i in range(10)]
	ct = [0 for i in range(10)]
	for i in range(num):
		tot = 0
		ans = 0
		for j in range(10):
			if (test_y[i][j] == 1):
				ct[j] += 1
				ans = j
			if (pred[i][j] > pred[i][tot]):
				tot = j
		if (tot == ans):
			corr += 1
			a[tot] += 1
		#print("{}:ans={},tot={}".format(i, ans, tot))
	print("corr={}").format(corr)
	for i in range(10):
		print("a[{}]={},{}").format(i, a[i],1.0*a[i]/110)
	testAccuracy = model.evaluate(test_X, test_y)[0]
	print("[+] Test accuracy: {} ".format(testAccuracy))



