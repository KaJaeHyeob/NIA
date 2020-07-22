# NIA
한국정보화진흥원 인턴 업무 | 개방데이터 크롤링 | OPEN API 활용

-----

## 목차
[1. 개방데이터 크롤링]

[2. OPEN API 활용]

-----

## 1. 개방데이터 크롤링 (feat.국민청원 & 국민제안)

### 1) 목적
- '청와대 국민청원 데이터'와 '국민신문고 국민제안 데이터'를 크롤링하여, 제목 토큰을 연계함으로써 청원 해결을 위한 정책 수립 도움

### 2) 용어 정리
- 스크래핑 : 데이터를 수집하는 모든 과정 (크롤링의 상위 개념)
- 크롤링 : 웹 페이지의 데이터를 수집하고 저장하는 과정
- 파싱 : 데이터를 가공하는 과정

### 3) 데이터 정리
- 국민청원 : 국민들이 청와대에게 답변을 요구하는 어떠한 사안
- 국민제안 : 어떠한 사안을 해결하기 위해 국민들이 제시하는 정책 방향

### 4) 과정

#### 쥬피터 랩(Jupyter Lab) 설치 및 실행
```
pip install jupyterlab
jupyter lab
```

#### 데이터 크롤링

#### 토큰화

#### 워드 클라우드 생성

-----

## 2. OPEN API 활용 (feat.전기자동차 충전소 현황)

### 1) 목적
- 공공데이터 포털에서 제공하는 '전기자동차 충전소 현황' OPEN API 데이터를 활용하여, 전기자동차 충전소 입지 선정 및 재선정을 위한 모델 생성

### 2) 용어 정리
- OPEN API : 누구나 사용 가능하도록 개방한 웹 API로써, 일반적으로 XML, JSON 형식으로 제공됨

### 3) 데이터 정리
- 전기자동차 충전소 현황 : 한국환경공단에서 제공하는 전국의 전기자동차 충전소 현황이 저장된 표준데이터 (XML 형식)

### 4) 과정

#### HTTP 통신으로 XML 데이터 파싱

