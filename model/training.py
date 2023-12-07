from sklearn.model_selection import train_test_split
from deepctr.feature_column import SparseFeat, get_feature_names
from deepctr.models import DeepFM

__all__ = ["train_model"]

def train_model(data, sparse_features):
    # 특성 컬럼 정의
    fixlen_feature_columns = [SparseFeat(feat, vocabulary_size=data[feat].nunique(), embedding_dim=4) 
                              for feat in sparse_features]
    dnn_feature_columns = fixlen_feature_columns
    linear_feature_columns = fixlen_feature_columns
    feature_names = get_feature_names(linear_feature_columns + dnn_feature_columns)

    # 데이터 분할
    train, test = train_test_split(data, test_size=0.2, random_state=2023)
    train_model_input = {name: train[name] for name in feature_names}
    test_model_input = {name: test[name] for name in feature_names}

    # 모델 정의 및 컴파일
    model = DeepFM(linear_feature_columns, dnn_feature_columns, task='binary')
    model.compile("adam", "binary_crossentropy", metrics=['binary_crossentropy'])

    # 모델 훈련
    model.fit(train_model_input, train['target'].values, 
              batch_size=256, epochs=10, verbose=2, validation_split=0.2)

    return model, test_model_input, test
