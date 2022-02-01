You can:
1) Create course
2) See list courses or some detailed course
3) Delete course
4) Edit\update course


```
(python manage.py makemigrations english)

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

127.0.0.1:8000/admin/

```
- for celery queries:
```
start rabbitmq (user\bitnami)
docker-compose up
```
- for add users and courses:
```python manage.py fill_db```
- superuser login/password is: 
```admin/admin```
- for test drf api:
```python3 api_requests.py```