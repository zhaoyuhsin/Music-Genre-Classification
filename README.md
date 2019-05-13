# Music-Genre-Classification
 >https://github.com/despoisj/DeepAudioClassification

 
## Abstract
将MP3文件转成频谱图，切成若干片段，送到CNN中训练
## Dataset
**GTZAN**
10个类别，每个类别100首歌曲(au格式)
## requirement
* eyed3
* sox --with-lame
* tensorflow
* tflearn
* libid3tag(由于sox不支持MP3格式)
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
* 通过predict.py中的calculate()
* 将模型文件放到model/下，与predict.py对应起来(确保load成功)
* calculate()中input为待预测新文件路径，输出为0~9的数字，分别代表十个风格，详见predict.py注释
* 想获得预测每个风格的概率，可以返回predict.py中的add数组，需要再正则化一下

## tips
 * MP3文件经处理变成数据库文件，后放入Data/Dataset中
 * 预处理数据集的数据库文件之后会上传到百度网盘上(包括train好的网络)
 
 ## Result of some examples
* Input为输入文件路径
* add为predict.py中add数组的值,每个下标代表一种风格的音乐, 权重越大，概率越高,可正则化
* Output为音乐风格预测结果
#### Sample 1 
Input:  music/blue1.mp3:

add:    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Output: 0
#### Sample 2
Input:  music/blue2.mp3:

add:    [11, 0, 0, 0, 0, 0, 0, 0, 0, 0]

Output: 0
#### Sample 3
Input:  music/tt.mp3:

add:    [3, 72, 1, 1, 2, 2, 5, 1, 5, 4]

Output: 1
#### Sample 4
Input:  music/country1.mp3:

add:    [0, 0, 9, 0, 0, 0, 0, 1, 1, 0]

Output: 2
#### Sample 5
Input:  music/metal1.mp3:

add:    [0, 0, 0, 0, 0, 0, 11, 0, 0, 0]

Output: 6
