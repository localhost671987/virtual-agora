rmdir /s /q users\migrations
rmdir /s /q virtual_agora\migrations
rmdir /s /q virtual_agora_api\migrations

del db.sqlite3 

pip install -r requirements.txt
python manage.py makemigrations users virtual_agora
python manage.py migrate

python manage.py createsuperuser
