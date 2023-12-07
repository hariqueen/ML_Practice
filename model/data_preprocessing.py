import pandas as pd
from sklearn.preprocessing import LabelEncoder

__all__ = ["load_and_preprocess_data"]

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)

    # 범주형 특성 정의
    sparse_features = ['userId', 'title', 'genres', 'tag'] 
    data[sparse_features] = data[sparse_features].fillna('-1')

    # Label Encoding
    for feat in sparse_features:
        lbe = LabelEncoder()
        data[feat] = lbe.fit_transform(data[feat])

    return data
