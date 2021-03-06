# assignment
원티드x위코드 백엔드 프리온보딩 과제
- 과제 출제 기업 정보
  - 기업명 : 카닥

## 과제 내용

- 사용자 생성 API
    - ID/Password로 사용자를 생성하는 API.
    - 인증 토큰을 발급하고 이후의 API는 인증된 사용자만 호출할 수 있다.
- 사용자가 소유한 타이어 정보를 저장하는 API
    - 자동차 차종 ID(trimID)를 이용하여 사용자가 소유한 자동차 정보를 저장한다.
    - 한 번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있도록 해야한다. 즉 사용자 정보와 trimId 5쌍을 요청데이터로 하여금 API를 호출할 수 있다는 의미이다.
- 사용자가 소유한 타이어 정보 조회 API
    - 사용자 ID를 통해서 2번 API에서 저장한 타이어 정보를 조회할 수 있어야 한다.
- 🔍 **상세구현 가이드**
    - 자동차 정보 조회 API의 사용은 아래와 같이 5000, 9000부분에 trimId를 넘겨서 조회할 수 있다.
    - **자동차 정보 조회 API 사용 예제** → 
       - 📄[https://dev.mycar.cardoc.co.kr/v1/trim/5000](https://dev.mycar.cardoc.co.kr/v1/trim/5000)
       - 📄[https://dev.mycar.cardoc.co.kr/v1/trim/9000](https://dev.mycar.cardoc.co.kr/v1/trim/9000) 
       - 📄[https://dev.mycar.cardoc.co.kr/v1/trim/11000](https://dev.mycar.cardoc.co.kr/v1/trim/11000) 
       - 📄[https://dev.mycar.cardoc.co.kr/v1/trim/15000](https://dev.mycar.cardoc.co.kr/v1/trim/15000)
    - 조회된 정보에서 타이어 정보는 spec → driving → frontTire/rearTire 에서 찾을 수 있다.
    - 타이어 정보는 205/75R18의 포맷이 정상이다. 205는 타이어 폭을 의미하고 75R은 편평비, 그리고 마지막 18은 휠사이즈로써 {폭}/{편평비}R{18}과 같은 구조이다. 위와 같은 형식의 데이터일 경우만 DB에 항목별로 나누어 서로다른 Column에 저장하도록 한다.

</aside>

### [필수 포함 사항]
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 서버 구조 및 디자인 패턴에 대한 개략적인 설명
    - 완료된 시스템이 배포된 서버의 주소
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

✔️ **API 상세설명**
---
  
## 구현 기능
### 사용자 생성 API
- userid와 password를 입력하여 사용자 생성하는 API
- is_staff의 값을 주어 true면 관리자, false면 일반 유저로 생성
- 로그인 시 인증토큰을 발급하여 인증된 사용자에 한하여 API 호출 가능 (권한에 따른 API 호출 제한)

### 타이어 정보를 DB에 저장하는 API
- 자동차 정보 조회 API에서 타이어에 해당하는 정보만 추출하여 데이터베이스에 저장
- 중복 저장 방지(API 호출 시 기존에 저장된 정보는 또 다시 저장되지 않음)

### 사용자가 소유한 타이어 정보를 저장하는 API
- 권한: 회원가입 시 관리자 권한을 부여받은 사용자만 저장 가능(is_staff=true)
- id와 trimid를 입력 시 입력된 사용자에게 입력된 trim에 해당하는 타이어 정보가 저장됨
- 한번에 최대 5명까지의 사용자에 대한 요청을 받을 수 있음
- 5명 초과의 요청, 아이디가 존재하지 않을 경우, trimid가 존재하지 않을 경우 에러 반환
- 원자성을 고려하여 도중에 에러 시 rollback 수행

### 사용자가 소유한 타이어 정보 조회 API
- 권한: 로그인 시 인증토큰을 통해 인증된 사용자 이상 조회 가능
- Query Params로 ID 검색 시 해당 ID에 저장된 타이어 정보 조회
- ID 검색 시 유저 없는 경우 에러 반환

## 기술 스택
- Back-End : python, django-rest-framework, sqlite3
- Tool     : Git, Github, slack, postman

## 실행 방법(endpoint 호출방법)

### ENDPOINT

| Method | endpoint | Request Header|Request body | Remark |
|:------:|-------------|-----|-------|--------|
|POST|/user||userid, password, is_staff|회원가입|
|POST|/token||userid, password|로그인|
|POST|/tire|token|user, tire|유저-타이어 저장|
|GET|/tire|token||유저-타이어 조회|


## API 명세(request/response)
  - [Postman API Document](https://documenter.getpostman.com/view/17228955/UVJcjvpy)

## 폴더 구조
```
├── config
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── data_uploader.py
├── db.sqlite3
├── manage.py
├── my_settings.py
├── requirements.txt
├── tires
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── users
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_user_is_staff.py
│   │   ├── 0003_alter_user_is_staff.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── venv

```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 카닥에서 출제한 과제를 기반으로 만들었습니다.
