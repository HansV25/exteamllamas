

Requisitos del software
    -python 3.11.0
    -pip
    -Visual studio code
    -APPSERV
    
    
Pasos para abrir y ejecutar el software

1. Abre una nueva carpeta desde el Visual Studio Core.

2. Desde la terminal, clonar o Descargar el software.

        git clone https://github.com/HansV25/exteamllamas.git

3. Activar el entorno virtual
   3.1: Ctrl + Shift + P >venv > requirements.txt

       python -m venv env

   En windows:
   
       .\env\Scripts\activate

   En linux / macOS
   
       source env/bin/activate

5. Instalar requirements.txt

        pip install -r requirements.txt


6. (una vez descargado e instalado APPSERV),Crear archivo .env para credenciales de la base de datos(o configurar directamente desde settings.py):

    

8. Crear migraciones y migrar en tu base de datos mysql
   
        python manage.py makemigrations
        python manage.py migrate

9. Crear superusuario
   
       python manage.py createsuperuser

10. Ejecutar el servidor
   
       python manage.py runserver

   el proyecto estará disponible en http://127.0.0.1:8000
