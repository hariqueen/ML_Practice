from model.FeatureExtractor import FeatureExtractor
import os
import warnings
warnings.filterwarnings(action="ignore")
from PIL import Image
import numpy as np 

__all__ = ["process_image"]

def process_image(directory):
    fe = FeatureExtractor()
    features = []
    img_paths = []
    
    img_files = [f for f in os.listdir(directory) if f.endswith('.png')]

    for img_name in img_files:
        try:
            image_path = os.path.join(directory, img_name)
            img_paths.append(image_path)
            # Extract Features
            feature = fe.extract(img=Image.open(image_path))
            features.append(feature)
            # Save the Numpy array (.npy) on designated path
            # feature_path = "/Users/haribo/Desktop/Pokemon_ prediction/features/" + os.path.splitext(img_name)[0] + ".npy"
            feature_path = os.path.join("/Users/haribo/Desktop/Pokemon_ prediction/features/"+ os.path.splitext(img_name)[0] + ".npy")
            np.save(feature_path, feature)
            
        except Exception as e:
            print('예외가 발생했습니다.', e)

    return features, img_paths

