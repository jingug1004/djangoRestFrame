# 백엔드를위한 Django REST Framework with 파이썬 

## Chapter 2. Django 기본 컨셉 익히기

### python local server 명령어

#### 기본 명령어

- Django 설치: pip install django~=3.2.10
- Django 프로젝트 생성: django-admin startproject myweb .
- photo 폴더 생성: python manage.py startapp photo
- 로컬 서버 실행: python manage.py runserver

#### Model 명령어

- migratins 에러 고치기: python manage.py migrate
- 어드민 페이지 슈퍼 유저 생성: python manage.py createsuperuser
- 모델 변경 내용을 기록하여 파일로 만듦: python manage.py makemigrations
- 생성된 파일을 실제로 실행시켜 실제 데이터베이스에 변경 사항을 적용: python manage.py migrate