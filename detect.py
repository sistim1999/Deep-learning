from ultralytics import YOLO

# 推理参数详解链接：https://docs.ultralytics.com/modes/predict/#inference-sources:~:text=of%20Results%20objects-,Inference%20Arguments,-model.predict()

if __name__ == '__main__':
    model = YOLO('runs/train/exp4/weights/best.pt') # 加载权重文件
    model.predict(
                source='datasets/weeds/images/train',   # 加载需推理文件夹
                imgsz=640,    # 训练图像尺寸
                project='runs/detect',    # 保存推理结果的项目目录名称
                name='exp',   # 推理运行的名称
                save=True,    # 保存开关
                )
