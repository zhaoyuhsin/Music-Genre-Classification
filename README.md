# Music-Genre-Classification
 >https://github.com/despoisj/DeepAudioClassification

 
## Abstract
将MP3文件转成频谱图，切成若干片段，送到CNN中训练
## Dataset
**GTZAN**
10个类别，每个类别100首歌曲(au格式)
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
## train & test

 1. Create folder Data/Raw/, 将数据集MP3数据集放到Raw内，命名格式为blues_0.mp3,blues_1.mp3,.
 2. 执行 python main.py slice，检查是否Data下有slice文件夹
  若没有，安装sox & lame & libsox-fmt-mp3(具体安装步骤见下面)

 3. 执行 python main.py train,训练的一些参数在config.py中更改，比如batch size、epoch等
 4. 执行 python main.py test，使用a[]存储的是每个类别的正确率，
```
   sudo apt-get install lame
   sudo apt-get install sox
   sudo apt-get install libsox-fmt-mp3
```
## train
-> https://github.com/despoisj/DeepAudioClassification
## Predict New File
1.将 模型文件(3个,index,meta,data)放入 / 下
2.执行python try.py ，输出当前路径下tt.mp3的概率


## tips
 1. MP3文件经处理变成数据库文件，后放入Data/Dataset中
 2. 预处理数据集的数据库文件之后会上传到百度网盘上(包括train好的网络)
 3. 之后更新&
 