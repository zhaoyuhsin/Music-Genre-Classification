# Music-Genre-Classification
from https://github.com/despoisj/DeepAudioClassification
## Abstract
将MP3文件转成频谱图，切成若干片段，送到CNN中训练
## Dataset
GTZAN
10个类别，每个列别100首歌曲(au格式)
## install
eyed3
sox --with-lame
tensorflow
tflearn
## format
训练数据集路径：Data/Dataset/
待加载模型路径：/
待MP3文件输入路径：/
## train
-> https://github.com/despoisj/DeepAudioClassification
## use
1.将 模型文件(3个,index,meta,data)放入 / 下
2.执行python try.py ，输出当前路径下tt.mp3的概率



