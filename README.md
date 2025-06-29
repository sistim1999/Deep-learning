# 说明

本项目基于 `ultralytics` 开源项目，提供了 **train.py\detect.py** 入口文件以更利于您使用。除此之外，我们还新增了 **train.ipynb\detect.ipynb** 两个 Jupyter 格式的代码文件，以方便您逐步执行。
并且我们提供了示例的 YOLO 格式杂草数据集，以及杂草训练权重文件，配置完成环境后可直接跑通本项目，使您更快速的体验深度学习项目。

# 环境配置

在 [**Python>=3.8**](https://www.python.org/) 环境中安装 `ultralytics` 包，包括所有**依赖项**，并确保 [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/)。

## Anaconda 安装

进入 [**Anaconda**](https://www.anaconda.com/) 官方网站，下载并安装所需版本。

安装完成后，进入 **Anaconda Prompt** 终端，可按需 create 新环境，如：`conda create -n yolo python=3.10`，需确保 [**Python>=3.8**](https://www.python.org/) 。

## PyTorch 安装

进入 [**PyTorch**](https://pytorch.org/get-started/locally/) 官网，选择符合本机版本，在 **Anaconda Prompt** 终端，激活您新建的环境，如：`conda activate yolo`，执行快捷安装命令。

命令参考示例：

```bash
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 包安装

在 [**Python>=3.8**](https://www.python.org/) 环境中安装 `ultralytics` 包，在 [**Python>=3.8**](https://www.python.org/) 环境中安装 `ultralytics` 包，包括所有**依赖项**。依赖项如本文件夹 pyproject.toml 文件所示。

```bash
pip install ultralytics
```



# 使用方法

## 训练

配置完成环境后，可在 **Anaconda Prompt** 终端，确保激活您的个人环境后，置于本项目根目录，执行：

```python
python train.py
```

## 推理

同训练，在训练完成后，执行：

```bash
python detect.py
```



# Jupyter 使用方法

## 安装环境

在配置好前置环境后，在 **Anaconda Prompt** 终端激活您的环境，安装 Jupyter 包：

```bash
pip install ipykernel
```

## 启动 JupyterLab

```bash
jupyter lab
```

执行后会自动打开浏览器，或者在终端中给出一个本地 URL（通常是 `http://localhost:8888`），复制到浏览器即可。

## 打开深度学习代码文件夹

在网页界面，打开`Deep-learning-main`文件夹（根据实际情况更改），打开我们的`.ipynb`后缀的文件。

## 在 Notebook 中运行代码

单个 cell：选中后按 **Shift + Enter**。

所有 cell：菜单 **Kernel → Restart & Run All**，或者点击工具栏里对应按钮。

## 相关说明

相关**训练\推理**参数配置及说明，可参见 **train.py\detect.py** 文件。

结果默认保存在此文件根目录：

1. 训练结果保存位置：runs/train/exp
2. 推理结果保存位置：runs/detect/exp

可在 Python 文件中自定义。


# 示例数据

示例杂草数据我们存放在次项目根目录 datasets 文件夹下，并且我们提供了杂草预训练权重文件 **weeds.pt**，可根据需求更换您个人杂草数据以及使用预训练权重。

数据配置在 **datasets/weeds.yaml** 文件中，可根据需求配置 **train、val、test** 文件夹及其数据。

## 公开杂草数据集

下载链接：https://www.kaggle.com/datasets/swish9/weeds-detection

可将下载的数据集，替换原本的数据，注意文件树结构：

```bash
├─datasets
│  └─weeds
│      ├─images		# 图片文件夹
│      │  ├─test	# 测试集
│      │  ├─train	# 训练集
│      │  └─val		# 验证集
│      └─labels		# 标签文件夹
│          ├─test	# 测试集
│          ├─train	# 训练集
│          └─val	# 验证集
```

并且，修改 **datasets/weeds.yaml** 文件为新数据集配置，若您下载数据是我们提供链接中数据集，文件内容参考如下：

```yaml
# dataset path
path: datasets/weeds/images/  # 数据集路径
train: train  # 训练集
val: val    # 验证集
test: test   # 测试集

# number of classes
nc: 2

# class names
names:
  0: crop
  1: weed
```

