# YOLO
yolo是速度最快的图片ai模型，支持目标检测，图片分类等最常用的功能，开箱即用，有成熟的cli和python库，方便调用。

- [代码](https://github.com/ultralytics/ultralytics)
- [ultralytics官网](https://ultralytics.com/)

yolo最主要的场景就是detect目标检测。以下文档都是基于v8版本进行的研究。

## 基础知识

### 安装
```shell
pip install ultralytics

# 检查
yolo

# 开箱即用的测试
yolo predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
image 1/1 bus.jpg: 640x480 4 persons, 1 bus, 1 stop sign, 52.5ms
Speed: 6.2ms preprocess, 52.5ms inference, 6.2ms postprocess per image at shape (1, 3, 640, 480)
Results saved to runs/detect/predict
```
关于`yolov8n.pt`或者`yolov8n.yaml`都是会自动下载安装的，不用手动处理。

## 任务

### 完成一个点选验证码的实验

#### 生成数据集

主要任务是生成一个可用于训练的训练数据集，分为两个步骤：
一）下载图片：通过脚本打开网页，模拟人工不断的刷新验证码获取图片，参考[代码](download_images.py)
二）手工标注：用rectlable工具标注图片，导出训练集文件夹，**只做一个分类，先做目标识别再做分类识别**

#### 目标识别和切割

##### 训练目标识别
```shell
cd <训练集文件夹>
# 修改data.yaml里面的路径为绝对路径
# 训练
yolo train data=./data.yaml model=yolov8n.pt imgsz=512 
```
- 是不是不用现成的`yolov8n.pt`，全新训练也可以？？？ 可以的：`yolo train data=./data.yaml model=./yolov8n.yaml`
- 如何用mps？`yolo train data=./data.yaml model=yolov8n.pt epochs=10 lr0=0.01 device=mps`，注意，截止目前，用mps训练detect模型会有问题，classify没有问题。
- 如何看训练效果图？ `tensorboard --logdir=./runs/detect/train3`
- 是不是不用管没有标签的文件，或者缺少的txt？未测试，暂时人工确保labels和images是一一对应。

##### 预测
```shell
yolo predict data=./datasets/detect/data.yaml model=./res/detect.onnx source=./datasets/detect_images/bgImg_20240124001543.png device=mps imgsz=512
```
这时候会把预测的结果保存`Results saved to runs/detect/predict3`，这是一个做好目标识别并且标注了区块的图片。

如果想要把结果存为txt文件，可以用`save_txt=True`参数，会在预测的目录下多了一个labels子目录，有一个txt文件是预测结果，跟标注的格式一样，也是xc,yc,w,h。

### 训练分类
把上一步的结果，把识别的目标切割出来，作为训练分类模型的输入。比如cls目录下有一堆子目录（名称作为分类名），每个目录下有若干图片，每个图片都是这个类别。
```shell
# 重新训练
yolo classify train data=./cls model=yolov8n-cls.pt epochs=100 imgsz=48
# 继续训练
yolo classify train data=./cls model=runs/classify/train6/weights/best.pt epochs=100 imgsz=48
# 预测
yolo classify predict source=char.png model=./res/classify.pt imgsz=48 device=mps
```

## 常见问题
### 有哪些预置的模型？
模型是针对任务来的，比如对应检测模型有：

| 模型                                                                                        | 尺寸<br><sup>(像素) | mAP<sup>验证<br>50-95 | 速度<br><sup>CPU ONNX<br>(毫秒) | 速度<br><sup>A100 TensorRT<br>(毫秒) | 参数<br><sup>(M) | 浮点运算<br><sup>(B) |
| ----------------------------------------------------------------------------------------- | --------------- | ------------------- | --------------------------- | -------------------------------- | -------------- | ---------------- |
| [YOLOv8n](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n-oiv7.pt) | 640             | 18.4                | 142.4                       | 1.21                             | 3.5            | 10.5             |
| [YOLOv8s](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8s-oiv7.pt) | 640             | 27.7                | 183.1                       | 1.40                             | 11.4           | 29.7             |
| [YOLOv8m](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8m-oiv7.pt) | 640             | 33.6                | 408.5                       | 2.26                             | 26.2           | 80.6             |
| [YOLOv8l](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8l-oiv7.pt) | 640             | 34.9                | 596.9                       | 2.43                             | 44.1           | 167.4            |
| [YOLOv8x](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8x-oiv7.pt) | 640             | 36.3                | 860.6                       | 3.56                             | 68.7           | 260.6            |

### 有哪些任务？
- 'detect' 目标检测（Detection）：这是 YOLOv8 的核心功能之一，用于识别和定位图像中的物体，并在其周围绘制边界框。
- 'segment' 实例分割（Segmentation）：这种任务不仅检测物体，而且还要对每个物体进行像素级的分割，区分不同的实例。
- 'classify' 分类（Classification）：虽然 YOLOv8 主要用于检测任务，但它也支持图像分类，即确定图像属于哪个预定义类别。
- 'pose' 姿态估计（Pose Estimation）：用于识别和定位图像中的人体关键点，可用于各种应用，如动作识别、健身追踪等。
- 'obb' 定向物体检测比常规物体检测更进一步，引入了额外的角度来更准确地定位图像中的物体。YOLOv8 可以高精度、高速度地检测图像或视频帧中的旋转物体。

#### 在命令行中不指定task默认是什么？
如果没有指定具体的task，通常默认进行的是目标检测任务。这意味着它会尝试识别和定位图像中的物体，并为每个检测到的物体输出一个边界框以及相应的类别标签。
命令行可以看到输出包含：`Results saved to runs/detect/predict`，说明是detect任务。

### 有哪些模式？
- train 训练
- val 验证
- predict 预测
- export 导出
- track 追踪
- benchmark

### 模型的配置文件格式
参考：https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8.yaml
```yaml
path: ./datasets/coco128  # dataset root dir
train: images/train2017  # train images (relative to 'path') 4 images
val: images/val2017  # val images (relative to 'path') 4 images
test:  # test images (optional)

# Classes (80 COCO classes)
names:
  0: person
  1: bicycle
  2: car
  # ...
  77: teddy bear
  78: hair drier
  79: toothbrush
```
对应的目录可以看到结构如下：
```shell
$ tree -aC datasets/coco128 # brew install tree
datasets/coco128
├── LICENSE
├── README.txt
├── images
│   └── train2017
│       ├── 000000000009.jpg
│       ├── 000000000025.jpg
│       ├── 000000000030.jpg
│       ├── 000000000034.jpg
└── labels
    ├── train2017
    │   ├── 000000000009.txt
    │   ├── 000000000025.txt
    │   ├── 000000000030.txt
    │   ├── 000000000034.txt
    └── train2017.cache
```
可以看到lables目录下有对应的txt文件，文件名和图片名一致，内容如下：
```shell
$ cat ./datasets/coco128/labels/train2017/000000000009.txt
45 0.479492 0.688771 0.955609 0.5955
45 0.736516 0.247188 0.498875 0.476417
50 0.637063 0.732938 0.494125 0.510583
45 0.339438 0.418896 0.678875 0.7815
49 0.646836 0.132552 0.118047 0.0969375
49 0.773148 0.129802 0.0907344 0.0972292
49 0.668297 0.226906 0.131281 0.146896
49 0.642859 0.0792187 0.148063 0.148062
```
第一列是类别，通过查找配置文件可以得到类别名。

### 如何获取到onnx的元数据
```python
# ultralytics/nn/autobackend.py 180行
metadata = session.get_modelmeta().custom_metadata_map  # metadata

# Return the metadata. See :class:`onnxruntime.ModelMetadata`.
```

```
__init__, autobackend.py:180
decorate_context, _contextlib.py:115
setup_model, predictor.py:341
predict, model.py:399
<module>, test.py:7
```
golang通过`github.com/yalue/onnxruntime_go`来获取：`session.GetModelMetadata()`

### 训练要多长时间？
一般100轮就可以得到比较好的效果：
- 如果是detect模型的话，一般数据有1000张图片，按照640的大小来算，100轮用CPU训练时间在10小时左右。
- 如果是classify模型的话，一般数据有1000张图片，按照64的大小来算，100轮用mps GPU训练时间在1小时左右。
