# Music-Genre-Classification
from https://github.com/despoisj/DeepAudioClassification
## Abstract
将MP3文件转成频谱图，切成若干片段，送到CNN中训练
## Dataset
GTZAN
10个类别，每个列别100首歌曲(au格式)
## requirement
eyed3
sox --with-lame
tensorflow
tflearn
libid3tag(由于sox不支持MP3格式)
## format
训练数据集路径：Data/Dataset/
待加载模型路径：/
待MP3文件输入路径：/
## How to use？
1.Create folder Data/Raw/
  将数据集MP3数据集放到Raw内，命名格式为blues_0.mp3,blues_1.mp3,....,rock_99.mp3
2. run:python main.py slice，检查是否Data下有slice文件夹
3.

## train
-> https://github.com/despoisj/DeepAudioClassification
## use
1.将 模型文件(3个,index,meta,data)放入 / 下
2.执行python try.py ，输出当前路径下tt.mp3的概率



