# Blog Django From Scratch

Blog creado en django para practicar. Ejercicios del libro Django for beginners. Web basica que se pueden añadir post desde el admin o desde la propia web mediante formularios. La base de datos es sqlite3 ya que es algo básico y no necesitamos postgres. 

- v0.1    Añadido modelo para los posts y creación. OK
- v0.2    Añadido CRUD completo con creacion, lectura, edicion y borrado de posts. OK
- v0.2.1  Fix statics, dont load. OK

## Instalación en local

Requisitos:

- Python 3.7

```mkdir blog
cd blog
git clone https://github.com/YintaoBtc/blog_django.git blog
cd blog

pipenv shell
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Con esto la web deberia estar funcionando en local. Para acceder a la web principal:
<http://127.0.0.1:8000>

Para acceder al panel de admin con los datos del superusuario:
<http://127.0.0.1:8000/admin>
