# 영화 추천 모델 구현

<pre><code>DeepFM 라이브러리를 이용하여 영화 추천 모델 만들기</code></pre>

### userId가 title인 영화를 볼 확률
|column name|설명  |
|---	|---	|
|userId|사용자ID (총 1000명)|
|title|영화제목 (총 100개)|
|genres|영화 장르|
|tag|영화 태그|
|rating|영화 평점|
|target|영화를 봤는지 안봤는지 (0=안봄, 1=영화를 봄)|

