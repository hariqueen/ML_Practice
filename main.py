from model import FeatureExtractor
from model import process_image
from model import calculate_similarity
import pandas as pd

# 이미지가 있는 폴더 경로
directory = "/Users/haribo/Desktop/Pokemon_ prediction/features/images/images"
target_image_path = "/Users/haribo/Desktop/Pokemon_ prediction/features/images/images/abomasnow.png"

euclidean_score = calculate_similarity(directory, target_image_path)

euclidean_df = pd.DataFrame(euclidean_score, columns=['Distance','Image_Path'])
euclidean_df.to_csv('distance.csv',index=False)