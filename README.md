Evaluacion 3 Back End   C2
Integrantes
            Bryan Martinez Ruiz
            Hans Vidal Rivera



Requisitos del software
    -python 3.11.0
    -pip
    -Visual studio code

Pasos para abrir y ejecutar el software

    1. Abre una nueva carpeta desde el Visual Studio Core.

    2. Desde la terminal, clonar el repositorio.

        git clone https://github.com/port4folio/evaluacion-sumativa-3-grupo1488.git

    3. Activar el entorno virtual

        python -m venv env

            En windows:
                .\env\Scripts\activate

            En linux / macOS
                source env/bin/activate

    4. Instalar requirements.txt

        pip install -r requirements.txt

    5. Crear archivo .env para credenciales de la base de datos(o configurar directamente desde settings.py):

    6. Crear migraciones y migrar en tu base de datos mysql
        python manage.py makemigrations
        python manage.py migrate

    7. Crear superusuario
        python manage.py createsuperuser

    8. Ejecutar el servidor
        python manage.py runserver

        el proyecto estará disponible en http://127.0.0.1:8000
