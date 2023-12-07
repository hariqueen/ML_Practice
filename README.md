# 이미지 유사도 구현

<pre><code>사전에 학습된 keras 속의 CNN 모델을 이용하여 포켓몬의 유사도 구하기</code></pre>
![Python 3.10.13](https://img.shields.io/badge/python-3.13.7-blue.svg) ![TensorFlow 2.10.0](https://img.shields.io/badge/TensorFlow-2.10.0-orange.svg)

📥 데이터셋 - [Pokemon Image Dataset](https://www.kaggle.com/datasets/vishalsubbiah/pokemon-images-and-types)

***

### 이미지 특징 추출 (FeatureExtractor.py)
> VGG16 모델을 사용하여 이미지의 특징을 추출하는 클래스 FeatureExtractor를 정의. 해당 클래스는 이미 학습된 가중치('imagenet')를 사용하며, 모델의 'fc1' 레이어에서 특징을 추출함. extract 메소드는 입력된 이미지를 전처리하고, VGG16 모델을 통해 특징을 추출한 후 정규화 진행

### 이미지 처리 및 특징 저장 (ImageProcessing.py)
> 주어진 디렉토리의 이미지들에 대한 처리 및 특징 추출을 수행. process_image 함수는 FeatureExtractor 클래스를 활용해 각 이미지의 특징을 추출하고, 이를 .npy 형식으로 저장 후 추출된 특징과 이미지 경로반환

### 이미지 유사도 계산 (similarity.py)
> 대상 이미지와 다른 이미지 간의 유사도를 계산하는 함수 calculate_similarity를 정의. 먼저 process_image 함수를 사용해 디렉토리 내의 이미지 특징을 추출한 후,다른 이미지들의 특징과 비교하여 유사도(유클리드 거리)를 계산하고, 가장 유사도가 낮은 이미지들을 선택하여 반환

