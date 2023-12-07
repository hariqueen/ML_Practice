# 영화 추천 모델 구현

<pre><code>DeepFM 라이브러리를 이용하여 영화 추천 모델 만들기</code></pre>


|column name|설명|
|---	|---	|
|userId|사용자ID (총 1000명)|
|title|영화제목 (총 100개)|
|genres|영화 장르|
|tag|영화 태그|
|rating|영화 평점|
|target|영화를 봤는지 안봤는지 (0=안봄, 1=영화를 봄)|


> ### 데이터 전처리 (data_preprocessing.py)

>  > 이 모듈은 데이터를 불러오고 (pd.read_csv), 범주형 특성(userId, title, genres, tag)에 대해 결측값을 '-1'로 채우며 (fillna('-1')), 라벨 인코딩 수행. 라벨 인코딩은 범주형 데이터를 모델이 이해할 수 있는 수치형 데이터로 변환하는 과정

> 모델 훈련 (model_training.py)

>  > 이 모듈에서는 DeepFM 모델의 특성 컬럼을 정의하고, 데이터를 훈련 세트와 테스트 세트로 분할 (train_test_split). DeepFM 모델은 선형 특성과 DNN 특성을 결합한 구조로, 이진 분류 작업을 수행하기 위해 컴파일되고 훈련 됨 (DeepFM, compile, fit).

> 모델 평가 및 결과 저장 (model_evaluation.py)

>  > 이 모듈에서는 훈련된 모델을 사용하여 테스트 데이터에 대한 예측을 수행하고, 로그 손실(LogLoss)과 AUC를 계산하여 모델의 성능을 평가(predict, log_loss, roc_auc_score). 이후 예측 결과를 movie_recommendations.csv 파일에 저장 (to_csv).

### userId가 title인 영화를 볼 확률
