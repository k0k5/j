Ознакомьтемь с проектом, установите виртуальное окружение и джанго. 
Рекомендуется использовать python 3.9 и django 3.2
Затем примените миграции и запустите сервер.



python -m venv venv            

source venv/Scripts/activate     

pip install Django==3.2

python manage.py migrate    

python manage.py makemigrations 

python manage.py runserver




                Применить миграции  (Применение созданных миграций или "пуш" для БД)

python manage.py makemigrations             Сделать миграции    (черновик/чертеж/"коммит" для БД)

python manage.py runserver
