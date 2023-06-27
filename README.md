1. 프로젝트 생성

2. 프로젝트 폴더 이동
```bash
cd<project name>
```

3. vscode 실행

4. 가상환경 설정
```bash
python -m venv venv
```

5. 가상환경 활성화
```bash
source venv/Scripts/activate
```

6. 가상환경 비활성화
```bash
deactivate
```

7. 가상환경 내부에 django 설치
```bash
pip install django
```

8. 서버 실행
```bash
python manage.py runserver
```

9. 앱 생성
```bash
django-admin startapp <app name>
```

10. 앱등록
- 'settings.py의
'INSTALLED_APPS에 등록

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]