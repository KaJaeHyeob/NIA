# NIA
한국정보화진흥원 인턴 업무 | 개방데이터 크롤링 & 워드클라우드 제작 | OPEN API 활용

-----

## 목차
[1. 개방데이터 크롤링 & 워드클라우드 제작](https://github.com/KaJaeHyeob/NIA/blob/master/README.md#1-%EA%B0%9C%EB%B0%A9%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%81%AC%EB%A1%A4%EB%A7%81-feat%EA%B5%AD%EB%AF%BC%EC%B2%AD%EC%9B%90--%EA%B5%AD%EB%AF%BC%EC%A0%9C%EC%95%88)

[2. OPEN API 활용](https://github.com/KaJaeHyeob/NIA#2-open-api-%ED%99%9C%EC%9A%A9-feat%EA%B3%B5%EA%B3%B5%EB%8D%B0%EC%9D%B4%ED%84%B0-%ED%8F%AC%ED%84%B8)

-----

## 1. 개방데이터 크롤링 & 워드클라우드 제작 (feat.국민청원 & 국민제안)

### 1) 목적
- '청와대 국민청원 데이터'와 '국민신문고 국민제안 데이터'를 크롤링하여, 제목 토큰을 연계함으로써 청원 해결을 위한 정책 수립 도움
- 토큰에 대한 워드클라우드 시각화를 진행하여, 현황 파악을 쉽게 하도록 함

### 2) 용어 정리
- 스크래핑 : 데이터를 수집하는 모든 과정 (크롤링의 상위 개념)
- 크롤링 : 웹 페이지의 데이터를 수집하고 저장하는 과정
- 파싱 : 데이터를 가공하는 과정
- 워드클라우드 : 데이터의 중요도에 따라 크기를 다르게 설정하여 시각화하는 기법

### 3) 데이터 목록
- 국민청원 : 국민들이 청와대에게 답변을 요구하는 어떠한 사안
- 국민제안 : 어떠한 사안을 해결하기 위해 국민들이 제시하는 정책 방향

### 4) 과정

#### 쥬피터 랩(Jupyter Lab) 설치 및 실행
주의) 인터프리터 기능을 편하게 사용하기 위해 쥬피터 랩을 사용함 (사용하지 않아도 무관함)
```
pip install jupyterlab
jupyter lab
```

#### 데이터 크롤링 (BeautifulSoup, celenium 사용)
주의) celenium 사용할 웹 브라우저의 드라이버 필요함 (구글에서 제공하는 크롬드라이버 사용함)
- [국민청원 데이터 크롤링](https://github.com/KaJaeHyeob/NIA/blob/master/app_BlueHouse/BlueHouse1_Crawling.ipynb)
- [국민제안 데이터 크롤링](https://github.com/KaJaeHyeob/NIA/blob/master/app_SinMoonGo/SinMoonGo1_Crawling.ipynb)

#### 토큰화 (konlpy 사용)
- [국민청원 데이터 토큰화](https://github.com/KaJaeHyeob/NIA/blob/master/app_BlueHouse/BlueHouse2_Tokenizing.ipynb)
- [국민제안 데이터 토큰화](https://github.com/KaJaeHyeob/NIA/blob/master/app_SinMoonGo/SinMoonGo2_Tokenizing.ipynb)

#### 워드클라우드 제작
- [국민청원 데이터 워드클라우드 제작](https://github.com/KaJaeHyeob/NIA/blob/master/app_WordCloud/BlueHouse3_WordCloud.ipynb)
- [국민제안 데이터 워드클라우드 제작](https://github.com/KaJaeHyeob/NIA/blob/master/app_WordCloud/SinMoonGo3_WordCloud.ipynb)

-----

## 2. OPEN API 활용 (feat.공공데이터 포털)

### 1) 목적
- 공공데이터 포털에서 제공하는 '전기자동차 충전소 현황' OPEN API 데이터를 활용하여, 전기자동차 충전소 입지 선정 및 재선정을 위한 모델 생성
- 전기자동차 충전소 입지 선정에 대한 표준분석모델일 이미 존재하기 때문에, 한계점을 밝히고 개선된 모델을 생성하는 것이 최종 목표

### 2) 용어 정리
- OPEN API : 누구나 사용 가능하도록 개방한 웹 API로써, 일반적으로 XML, JSON 형식으로 제공됨 (HTTP 통신으로 요청 및 응답)

### 3) 데이터 목록
- 전기자동차 충전소 현황 : 전국의 전기자동차 충전소 현황이 저장된, 한국환경공단에서 제공하는 표준데이터 (XML 형식)
- 평일/주말 교통량 : 전국 고속도로의 평일, 주말 교통량이 저장된, 한국도로공사에서 제공하는 공공데이터 (엑셀 파일)

### 4) 과정

#### 공공데이터 포털 OPEN API 데이터 불러오기
- [HTTP 통신으로 XML 데이터 파싱](https://github.com/KaJaeHyeob/NIA/blob/master/app_EleCar/EleCarCharge_API.ipynb)

