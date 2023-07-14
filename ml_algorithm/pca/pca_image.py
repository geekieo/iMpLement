import pca
import numpy as np

def reshape(images: np.ndarray) -> np.ndarray:
    """
    将输入图像集合的形状从 [N, H, W] 调整为 [N, H*W]。
    
    参数：
    images: 输入图像集合，形状为 [N, H, W] 的 ndarray。
    
    返回值：
    调整形状后的图像集合，形状为 [N, H*W] 的 ndarray。
    """
    # 获取输入图像集合的形状信息
    N, H, W = images.shape

    # 调整形状为 [N, H*W] 的输出数组
    reshaped_images = np.reshape(images, (N, H*W))

    return reshaped_images

