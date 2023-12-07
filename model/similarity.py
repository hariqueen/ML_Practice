from tensorflow.keras.preprocessing import image
from model.ImageProcessing import process_image
from PIL import Image
import numpy as np

__all__ = ["calculate_similarity"]

# Target 이미지
def calculate_similarity(directory, target_image_path):
    features, img_path = process_image(directory)
    img = Image.open(target_image_path)
    query = features[0]
    # 유사도 계산
    dists = np.linalg.norm(features - query, axis=1)
    # Extract 30 images that have lowest distance
    ids = np.argsort(dists)
    euclidean_score = [(dists[id], img_path[id]) for id in ids]

    return euclidean_score