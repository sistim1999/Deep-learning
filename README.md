# 环境配置

在 [**Python>=3.8**](https://www.python.org/) 环境中安装 `ultralytics` 包，包括所有**依赖项**，并确保 [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/)。

## Anaconda 安装

进入 [**Anaconda**](https://www.anaconda.com/) 官方网站，下载并安装所需版本。

安装完成后，进入 **Anaconda Prompt** 终端，可按需 create 新环境，需确保 [**Python>=3.8**](https://www.python.org/) 。

## PyTorch 安装

进入 [**PyTorch**](https://pytorch.org/get-started/locally/) 官网，选择符合本机版本，在 **Anaconda Prompt** 终端，执行快捷安装命令。

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

配置完成环境后，可在 **Anaconda Prompt** 终端，置于本项目根目录，执行：

```python
python train.py
```

## 推理

同训练，在训练完成后，执行：

```bash
python detect.py
```

## 相关说明

相关**训练\推理**参数配置及说明，可参见 **train.py\detect.py** 文件。

结果默认保存在此文件根目录：

1. 训练结果保存位置：runs/train/exp
2. 推理结果保存位置：runs/detect/exp

可在 Python 文件中自定义。


# 示例数据

示例杂草数据我们存放在次项目根目录 datasets 文件夹下，并且我们提供了杂草预训练权重文件 **weeds.pt**，可根据需求更换您个人杂草数据以及使用预训练权重。

数据配置在 **weeds.yaml** 文件中，可根据需求配置 **train、val、test** 文件夹及其数据。



