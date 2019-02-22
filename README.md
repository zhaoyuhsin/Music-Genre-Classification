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
2.main.py中调用calculate("a.mp3")，返回大小为10的列表ans,其中ans[i]代表属于第i个流派的概率



