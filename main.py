from model import load_and_preprocess_data
from model import train_model
from model import evaluate_and_save_results

file_path = '/Users/haribo/Desktop/movie_ prediction/movielens.csv'

# 데이터 전처리
data = load_and_preprocess_data(file_path)

# 모델 훈련
model, test_model_input, test = train_model(data, ['userId', 'title', 'genres', 'tag'])

# 모델 평가 및 결과 저장
evaluate_and_save_results(model, test_model_input, test)
