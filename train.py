from ultralytics import YOLO

# 训练参数详解链接：https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings:~:text=a%20training%20run.-,Train%20Settings,-The%20training%20settings

if __name__ == '__main__':
    model = YOLO('ultralytics/cfg/models/yolo11s.yaml')      # 加载模型文件
    model.load('datasets/weeds/weeds.pt') # 加载预训练权重文件（可选）
    model.train(
            data='datasets/weeds.yaml',  # 数据集配置文件路径
            imgsz=640,  # 训练图像尺寸
            epochs=100,   # 训练周期数
            batch=8,    # 批量大小设置
            workers=8,  # Windows 下出现莫名其妙卡主的情况可以尝试把 workers 设置为 0
            device='0', # 运行设备（例如 'cpu', 0, [0,1,2,3]）
            project='runs/train',       # 保存训练结果的项目目录名称
            name='exp', # 训练运行的名称
            )
